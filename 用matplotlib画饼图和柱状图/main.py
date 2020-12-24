import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
df = pd.read_csv('xtrain.csv').loc[:,['body_type']]
df1 = df['body_type'].value_counts()
data_pair_1 = [(i, int(j)) for i, j in zip(df1.index, df1.values)]
labels = []
sizes = []
for data in data_pair_1:
    labels.append(data[0])
    sizes.append(data[1])
sums = 0
for s in sizes[5:]:
    sums += s
plt.figure(figsize=(6,9)) #调节图形大小
labels = labels[:5] #定义标签
labels.append('others')
sizes = sizes[:5] #每块值
sizes.append('3216')
colors = ['mediumspringgreen','mediumaquamarine','aquamarine','turquoise','lightseagreen','mediumturquoise'] #每块颜色定义
explode = (0,0,0.02,0,0,0) #将某一块分割出来，值越大分割出的间隙越大
patches,text1,text2 = plt.pie(sizes,
                      explode=explode,
                      labels=labels,
                      colors=colors,
                      labeldistance = 1.2,#图例距圆心半径倍距离
                      autopct = '%3.2f%%', #数值保留固定小数位
                      shadow = False, #无阴影设置
                      startangle =90, #逆时针起始角度设置
                      pctdistance = 0.6) #数值距圆心半径倍数距离
#patches饼图的返回值，texts1饼图外label的文本，texts2饼图内部文本
# x，y轴刻度设置一致，保证饼图为圆形
plt.axis('equal')
plt.legend()
plt.savefig('data/test1.jpg')
plt.show()
