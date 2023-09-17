import pandas as pd

# 加载两个CSV文件
file1 = pd.read_csv('ZJ_C_Diff_01.csv')
file2 = pd.read_csv('ZJ_ADC_01.csv')

# 使用merge函数将两个文件合并，基于ID列
merged_data = pd.merge(file1, file2, on='ID', suffixes=('', '_Segment'))
print(merged_data.columns)



merged_data.to_csv('ZJ_C_ADC_Diff_01.csv', index=False)
