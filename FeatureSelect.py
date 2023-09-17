import pandas as pd
from scipy.stats import ttest_ind, levene, chi2_contingency

# 读取两个时期的特征值CSV文件

feature_file_1 = 'SegmentRadiomics/group_6_0.csv'
feature_file_2 = 'SegmentRadiomics/group_6.csv'

# 读取CSV文件
features_1 = pd.read_csv(feature_file_1)
features_2 = pd.read_csv(feature_file_2)

# 获取病人ID的前6位
ids_1 = features_1.iloc[:, -1].str[:6]
ids_2 = features_2.iloc[:, -1].str[:6]

# 确定共同的病人ID前缀
common_prefixes = set(ids_1) & set(ids_2)

# 筛选出共同的病人ID
common_ids_1 = ids_1[ids_1.isin(common_prefixes)].tolist()
common_ids_2 = ids_2[ids_2.isin(common_prefixes)].tolist()

# 从特征数据中选取共同的病人ID对应的特征，并将特征值解析为数值类型
common_features_1 = features_1[features_1.iloc[:, -1].str[:6].isin(common_ids_1)].iloc[:, 1:-1]
common_features_1 = common_features_1.apply(pd.to_numeric, errors='coerce')

common_features_2 = features_2[features_2.iloc[:, -1].str[:6].isin(common_ids_2)].iloc[:, 1:-1]
common_features_2 = common_features_2.apply(pd.to_numeric, errors='coerce')

# 计算特征差异
feature_diff = common_features_2 - common_features_1

# 进行t检验
t_test_results = []
for column in feature_diff.columns:
    t_statistic, p_value = ttest_ind(common_features_1[column], common_features_2[column])
    t_test_results.append((column, t_statistic, p_value))

# 进行Levene检验
levene_test_results = []
for column in feature_diff.columns:
    stat, p_value = levene(common_features_1[column], common_features_2[column])
    levene_test_results.append((column, stat, p_value))

# 创建DataFrame来保存检验结果
t_test_df = pd.DataFrame(t_test_results, columns=['Feature', 'T_Statistic', 'P_Value'])
levene_test_df = pd.DataFrame(levene_test_results, columns=['Feature', 'Levene_Statistic', 'P_Value'])

# 保存结果为CSV文件
t_test_df.to_csv('06_t_test_results.csv', index=False)
levene_test_df.to_csv('06_levene_test_results.csv', index=False)