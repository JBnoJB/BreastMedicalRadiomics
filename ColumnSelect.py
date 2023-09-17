import pandas as pd

# 加载两个CSV文件
file1 = pd.read_csv('10mmGroup_1_0.csv')
file2 = pd.read_csv('10mmGroup_1.csv')

# 使用merge函数将两个文件合并，基于ID列
merged_data = pd.merge(file1, file2, on='ID', suffixes=('_file0', '_file1'))
print(merged_data.columns)

# 遍历浮点数列，执行相减操作
for col in ["original_shape_SurfaceVolumeRatio", "original_firstorder_Kurtosis", "original_firstorder_Minimum", "original_glcm_Idmn", "original_gldm_LowGrayLevelEmphasis", "original_glrlm_LowGrayLevelRunEmphasis", "original_glrlm_ShortRunLowGrayLevelEmphasis", "original_glszm_LargeAreaHighGrayLevelEmphasis", "original_glszm_LowGrayLevelZoneEmphasis", "original_glszm_SmallAreaLowGrayLevelEmphasis", "original_ngtdm_Strength"]:
    merged_data[col + '_10mm'] = merged_data[col + '_file0'] - merged_data[col + '_file1']

# 选择要保存的列
result_data = merged_data[['ID','original_shape_SurfaceVolumeRatio_10mm', 'original_firstorder_Kurtosis_10mm', 'original_firstorder_Minimum_10mm', 'original_glcm_Idmn_10mm', 'original_gldm_LowGrayLevelEmphasis_10mm', 'original_glrlm_LowGrayLevelRunEmphasis_10mm', 'original_glrlm_ShortRunLowGrayLevelEmphasis_10mm', 'original_glszm_LargeAreaHighGrayLevelEmphasis_10mm', 'original_glszm_LowGrayLevelZoneEmphasis_10mm', 'original_glszm_SmallAreaLowGrayLevelEmphasis_10mm', 'original_ngtdm_Strength_10mm']
]
# 保存结果到新的CSV文件
result_data.to_csv('10mm01.csv', index=False)
