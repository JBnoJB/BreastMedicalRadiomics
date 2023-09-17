import os
from radiomics import featureextractor
import SimpleITK as sitk
import csv

# 配置参数文件路径
params = None  # 或者 None 使用默认参数

# 初始化特征提取器
extractor = featureextractor.RadiomicsFeatureExtractor(params)

# 指定图像和掩码文件夹
image_folder = "ZJ_ADC_Source"
mask_folder = "ZJ_ADC_Seg"

# 输出 CSV 文件路径
output_csv = "output.csv"

# 初始化 CSV 文件
with open(output_csv, 'w', newline='') as outputFile:
    fieldnames = ["Image", "Mask"]
    for key in extractor.featureClassNames:
        fieldnames.extend(extractor.getFeatureNames(key))
    writer = csv.DictWriter(outputFile, fieldnames=fieldnames)
    writer.writeheader()

# 遍历文件夹并进行特征提取
for image_name in os.listdir(image_folder):
    if not image_name.endswith(".nii.gz"):
        continue

    base_name = os.path.splitext(os.path.splitext(image_name)[0])[0]
    mask_name = f"{base_name}_seg.nii.gz"

    image_path = os.path.join(image_folder, image_name)
    mask_path = os.path.join(mask_folder, mask_name)

    if not os.path.exists(mask_path):
        print(f"Mask for {image_name} not found. Skipping...")
        continue

    # 读取图像和掩码
    image = sitk.ReadImage(image_path)
    mask = sitk.ReadImage(mask_path)

    # 提取特征
    result = extractor.execute(image, mask)

    # 保存到 CSV 文件
    with open(output_csv, 'a', newline='') as outputFile:
        writer = csv.DictWriter(outputFile, fieldnames=fieldnames)
        row_data = {"Image": image_name, "Mask": mask_name}
        for key, value in result.items():
            if key.startswith("diagnostics"):
                continue
            row_data[key] = value
        writer.writerow(row_data)

    print(f"Features extracted from {image_name}")
