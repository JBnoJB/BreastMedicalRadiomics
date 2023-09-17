import pandas as pd




file1 = pd.read_csv('Segment01.csv')
file2 = pd.read_csv('10mm01.csv')

# 使用merge函数将两个文件合并，基于ID列
merged_data = pd.merge(file1, file2, on='ID', suffixes=('', ''))
print(merged_data.columns)

# 保存结果到新的CSV文件
merged_data.to_csv('01Merged.csv', index=False)