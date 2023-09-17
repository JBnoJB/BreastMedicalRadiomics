import pandas as pd

# 读取CSV文件
df = pd.read_csv('ZJ_ADC_0.csv')

# 初始化一个空列表来存储浮点数列名
float_columns = []

# 遍历DataFrame的列
for column in df.columns:
    # 尝试将列转换为浮点数，如果成功则添加到float_columns列表中
    try:
        df[column] = df[column].astype(float)
        float_columns.append(column)
    except ValueError:
        # 转换失败，列不是浮点数
        pass

# 打印所有浮点数列名
print("浮点数列名:")
print(float_columns)
