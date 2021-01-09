from makerbean import web_crawler_bot as wbot
from makerbean import excel_bot as ebot
from makerbean import data_analysis_bot as dbot
from makerbean import pdf_bot as pbot
from makerbean import word_bot
import pandas as pd

#读取这个CVS文件
df = pd.read_csv("分省年度数据.csv",encoding='gbk')
ls =[]
d={}
l = []
for i in df['地区']:
    ls.append(i)
for j in df['平均数']:
    l.append(j)
#为每个字典的城市添加相应的数据
for h in range(len(ls)):
    d[ls[h]] = l[h]
#分析数据，自动生成一个这个的3D地区模型
dbot.generate_3d_map(d)
