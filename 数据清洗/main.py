import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv('titanic_data.csv')
#查看缺少值
df.isnull().sum()
#查看缺失值的比例
print('缺失占比 %.2f%%' %((df['age'].isnull().sum()/df.shape[0])*100))
#查看年龄分布
age = df['age'].hist(bins=15,color='teal',alpha=0.6)
#设置标题age
age.set(xlabel='age')
#从零开始
plt.xlim(0)
#显示图片
# plt.show()
# print(df['embarked'].value_counts())
# sns.countplot(x='embarked', data=df, palette='Set2')
# plt.show()
data = df.copy()
#使用中间值填补空缺年龄
data['age'].fillna(df['age'].median(skipna=True), inplace=True)
#删除某一列
data.drop(columns=['cabin'],inplace=True)
#使用众数来填充
data['embarked'].fillna(df['embarked'].value_counts().idxmax(),inplace=True)
#对于缺失的其他列，因为数量较少，这里直接采用删除缺失部分，不影响整体效果
data.dropna(axis=0,how='any',inplace=True)
data.isnull().sum()
data['alone'] = np.where((data['sibsp']+data['parch'])>0,0,1)
data.drop('sibsp',axis=1,inplace=True)
data.drop('parch',axis=1,inplace=True)
data.head()

#当都是字符串类型的数据的时候，我们该怎么办，我们可以用独热编码的方式来转换数据
data = pd.get_dummies(data,columns=['embarked','sex'])
print(data.head())
#独热编码（one-hot encoding），是一种常用的数据转换方式，对于每一个特征，
# 如果它有 m 个可能值，那么经过独热编码后，就变成了 m 个二元特征，这些特征互斥，每次只有一个激活。
#对于一些无用的数据我们可以选择删除
data.drop('name',axis=1,inplace=True)
data.drop('ticket',axis=1,inplace=True)

#查看比例
sex_sur_table = pd.pivot_table(df,index=['sex'],values='survived')
print(sex_sur_table)
pclass_sur_table = pd.pivot_table(df,index=['sex'],columns=['pclass'],values='survived')
print(pclass_sur_table)