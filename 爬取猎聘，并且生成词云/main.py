from makerbean import web_crawler_bot as wbot
from makerbean import excel_bot as ebot
from makerbean import data_analysis_bot as dbot
from makerbean import pdf_bot as pbot
from makerbean import word_bot

for i in range(10):
    data = wbot.get_liepin('数据分析',i)
    for d in range(len(data)):
        ebot.add_row(data[d])
ebot.save("数据分析","csv")

col2 = ebot.get_col(2)
word_freq = dbot.get_word_frequency(col2)
dbot.generate_word_cloud(word_freq)