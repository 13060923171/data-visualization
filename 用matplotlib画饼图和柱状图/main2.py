import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_csv('xtrain_automatic.csv').loc[:,['body_type']]
df1 = df['body_type'].value_counts()


data = pd.read_csv('xtrain_mechanical.csv').loc[:,['body_type']]
df2 = data['body_type'].value_counts()


data_pair_1 = [(i, int(j)) for i, j in zip(df1.index, df1.values)]
labels1 = []
sizes1 = []
for data in data_pair_1:
    labels1.append(data[0])
    sizes1.append(data[1])

data_pair_2 = [(i, int(j)) for i, j in zip(df2.index, df2.values)]
labels2 = []
sizes2 = []
for data in data_pair_2:
    labels2.append(data[0])
    sizes2.append(data[1])

body_type = labels1
number1 = sizes1
number2 = sizes2
bar_width = 0.3  # 条形宽度
index_mechanical = np.arange(len(body_type))
index_automatic = index_mechanical + bar_width

# 使用两次 bar 函数画出两组条形图
plt.bar(index_automatic, height=number1, width=bar_width, color='springgreen', label='automatic')
plt.bar(index_mechanical, height=number2, width=bar_width, color='darkcyan', label='mechanical')

plt.legend()  # 显示图例
plt.xticks(index_automatic + bar_width/2, body_type)  # 让横坐标轴刻度显示 waters 里的饮用水， index_male + bar_width/2 为横坐标轴刻度的位置
plt.ylabel('price_uid')  # 纵坐标轴标题
plt.rcParams['savefig.dpi'] = 640  # 图片像素
plt.rcParams['figure.dpi'] = 480  # 分辨率
plt.rcParams['figure.figsize'] = (20.0, 10.0)  # 尺寸
plt.title('transmission')  # 图形标题

plt.show()