import tushare as ts
import time

#获取全部股票代码
st = ts.get_stock_basics()
print(st.head())
list = ['600519','300750','600987']
#不是指数
index = False
#复权类型为后复盘
autype = 'hfq'
#数据类型为日期
ktype= 'D'
#定义一个字符串
pp =''
#如果复权的类型为None
if autype == 'None':
    pp = pp+'none'
if autype == 'hfq':
    pp = pp+'hfq'
if index == True:
    pp = pp+'index'
kk = ''
if ktype == "D":
    kk = kk+'day'
if ktype == "W":
    kk = kk+'week'
if ktype == "M":
    kk = kk+"month"
if ktype == "5":
    kk = kk+'minute'
#开始时间为1991-01-01
ds = '1991-01-01'
#结束时间为当前日期
de = time.strftime('%Y-%m-%d',time.localtime(time.time()))
print(ds,de)
i = 0
#for ss in st.index:
#写一个循环列表
for ss in list:
    i +=1
    print(i,ss)
    #前复权，不复权，后复权
    for autype in ['qfq','None','hfq']:
        for ktype in ['D','W','M']:
            pp = ''
            if autype == 'None':
                pp = pp+'none'
            if autype == 'hfq':
                pp = pp +'hfq'
            if index == True:
                pp = pp+'index'
            kk = ''
            if ktype == 'D':
                kk = kk+'day'
            if ktype =='W':
                kk = kk+'week'
            if ktype == 'M':
                kk = kk+'month'
            if ktype == '5':
                kk = kk+'minute'
            #获取K线所需要的参数定义，股票代码，数据类型，开始时间，结束时间，定义类型，复权类型
            df1 = ts.get_k_data(ss,ktype=ktype,start=ds,end=de,index=index,autype=autype)
            ss1 = kk+pp+ss+'.csv'
            print(ss1)
            #保存成CSV文件
            df1.to_csv(ss1,encoding='gbk')