import pandas as pd
mydata = pd.read_excel('mydata.xlsx',index_col='姓名')
mydata1 = mydata.copy()
print(mydata1.isnull().sum())
#使用平均值填充
mydata1['体重'].fillna(mydata1['体重'].mean(),inplace=True)
#删除空行
mydata1.dropna(how='any',inplace=True)
print(mydata1.isnull().sum())
#小结：一定要先执行空值填充，再执行删除空行的代码，否则含有空值的行都会被删除。
#把身高改成统一值
mydata1.loc[mydata1['身高']<100,'身高'] = mydata1[mydata1['身高']<100]['身高']*100
#改变不合理的值
mydata1.loc['张飞','年龄'] = 27
#用正则表达式，替换存在的K
mydata1['年龄'].replace({r'[K]':''},regex=True,inplace=True)
mydata1.drop_duplicates(inplace=True)#删除重复的行
mydata1.drop('年龄.1',axis=1,inplace=True)#删除不需要的列
print(mydata1)
mydata1.to_csv('data.csv',encoding='gbk')
