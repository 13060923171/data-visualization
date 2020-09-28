#网络爬虫机器人
from makerbean import web_crawler_bot as wbot
#操作Excel表机器人
from makerbean import excel_bot as ebot
#数据分析机器人
from makerbean import data_analysis_bot as dbot
#操作PDF机器人
from makerbean import pdf_bot as pbot
#操作Word文档机器人
from makerbean import word_bot


#打开Excel表格
ebot.open('公司簿.xlsx')
for i in range(1,6):
    #打开Word文档
    word_bot.open('模板.docx')
    #定义这个Word文档的段落
    paragraphs = word_bot.paragraphs
    #读取Excel表格，并且开始历遍i行
    row = ebot.get_row(i)
    #这句话的意思是我去定位到Word文档的第一行的内容，然后用replace函数来替换内容，替换的内容就是我定位表格的内容的第几位
    p0 = paragraphs[0].replace('【公司名】', row[0])
    p1 = paragraphs[1].replace('【产品名】', row[1])
    p1 = p1.replace('【报价】',str(row[2]))
    #重写Word文档的第0行的内容，内容是p0
    word_bot.set_paragraph(0, p0)
    word_bot.set_paragraph(1, p1)
    #保存Word文档
    word_bot.save(row[0])