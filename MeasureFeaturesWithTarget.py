import pandas as pd
from scipy import stats
from scipy.stats import chi2_contingency

# 读取CSV文件
data = pd.read_csv('01Merged.csv')

# 将数据分为两个组，根据目标变量（0和1）
group_0 = data[data['target'] == 0]
group_1 = data[data['target'] == 1]

# 初始化空的字典来存储特征及其对应的t统计值和p值
t_statistics = {}
p_values = {}

# 遍历每个特征列
for feature in data.columns[2:]:  # 假设特征列从第三列开始
    t_stat, p_value = stats.ttest_ind(group_0[feature], group_1[feature])
    t_statistics[feature] = t_stat
    p_values[feature] = p_value

# 保存t统计值和p值到CSV文件
t_statistic_df = pd.DataFrame.from_dict(t_statistics, orient='index', columns=['t-statistic'])
p_value_df = pd.DataFrame.from_dict(p_values, orient='index', columns=['p-value'])
result_df = pd.concat([t_statistic_df, p_value_df], axis=1)
result_df.to_csv('t_test_results.csv')

# 初始化空的字典来存储特征及其卡方值和p值
chi2_statistics = {}
chi2_p_values = {}

# 遍历每个分类特征列
for feature in data.columns[2:]:  # 假设特征列从第三列开始
    contingency_table = pd.crosstab(data['target'], data[feature])
    chi2, p_value, _, _ = chi2_contingency(contingency_table)
    chi2_statistics[feature] = chi2
    chi2_p_values[feature] = p_value

# 保存卡方值和p值到CSV文件
chi2_statistic_df = pd.DataFrame.from_dict(chi2_statistics, orient='index', columns=['Chi-square statistic'])
chi2_p_value_df = pd.DataFrame.from_dict(chi2_p_values, orient='index', columns=['p-value'])
chi2_result_df = pd.concat([chi2_statistic_df, chi2_p_value_df], axis=1)
chi2_result_df.to_csv('chi2_test_results.csv')

# 打印特征及其t统计值、p值、卡方值和p值
for feature, t_stat in t_statistics.items():
    if(p_values[feature]<0.1):
        print(f'Feature: {feature}, t-statistic: {t_stat}, p-value: {p_values[feature]}')

for feature, chi2_stat in chi2_statistics.items():
    if (chi2_p_values[feature] < 0.1):
        print(f'Feature: {feature}, Chi-square statistic: {chi2_stat}, p-value: {chi2_p_values[feature]}')
