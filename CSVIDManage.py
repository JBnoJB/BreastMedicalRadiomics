import pandas as pd

# 读取CSV文件
df = pd.read_csv('SegmentRadiomics/group_0.csv')

# 处理File列，将值截取前六位，并将列名改为ID
df['ID'] = df['File'].str[:6]

# 删除原来的File列
df.drop(columns=['File'], inplace=True)

# 将ID列移动到最前面
df = df[['ID'] + [col for col in df.columns if col != 'ID']]

# 保存到新的CSV文件
df.to_csv('ZJ_ADC_0.csv', index=False)
