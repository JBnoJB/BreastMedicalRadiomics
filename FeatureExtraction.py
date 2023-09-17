import os
import re
import SimpleITK as sitk
from radiomics import featureextractor
import csv

# 设置源文件和分割文件路径
image_folder = 'ZJ_ADC_Source'
mask_folder = 'ZJ_ADC_Seg'
output_folder = 'SegmentRadiomics'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# 获取文件列表
image_files = [f for f in os.listdir(image_folder) if f.endswith('.nii.gz')]

# 创建特征提取器
extractor = featureextractor.RadiomicsFeatureExtractor()

# 设置特征提取参数
extractor = featureextractor.RadiomicsFeatureExtractor()
settings = extractor.settings
settings['binWidth'] = 25
settings['verbose'] = True
settings['enable'] = ['firstorder', 'glcm', 'shape', 'glrlm', 'glszm']  # 添加更多特征类型


# 分组特征提取结果
grouped_features = {}

# 提取特征
for idx, image_file in enumerate(image_files, 1):
    if image_file.endswith('.nii.gz'):
        image_path = os.path.join(image_folder, image_file)
        mask_file = image_file.replace('.nii.gz', '_seg.nii.gz')
        mask_path = os.path.join(mask_folder, mask_file)

        image = sitk.ReadImage(image_path)
        mask = sitk.ReadImage(mask_path)

        # 将源文件与分割文件相乘，只保留分割出的区域
        segmented_image = sitk.Cast(image, sitk.sitkFloat32) * sitk.Cast(mask, sitk.sitkFloat32)

        feature_vector = extractor.execute(segmented_image, mask)
        feature_vector['File'] = image_file  # 添加一个键为'File'的项，值为文件名

        # 获取文件名中第七位数字
        digit = image_file[7]
        n = 7
        if (digit == '_'):
            digit = image_file[8]
            n = 8

        print(digit)
        # 将特征向量添加到相应的组中
        if digit in grouped_features:
            grouped_features[digit].append(feature_vector)
        else:
            grouped_features[digit] = [feature_vector]

        print(f"Processing file {idx}/{len(image_files)}: {image_file}")

# 保存分组的特征向量到CSV文件
for digit, features in grouped_features.items():
    output_csv_path = os.path.join(output_folder, f'group_{digit}.csv')

    with open(output_csv_path, 'w', newline='') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=features[0].keys())

        # 写入特征向量的标题行
        csv_writer.writeheader()

        # 写入每个样本的特征向量
        for feature_vector in features:
            csv_writer.writerow(feature_vector)
