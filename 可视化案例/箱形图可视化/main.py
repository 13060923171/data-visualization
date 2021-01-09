import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Boxplot


df = pd.read_excel('11.xlsx').loc[:,['slope','height']]

list_5 = []
list_10 = []
list_15 = []
list_20 = []
list_30 = []

for i in range(len(df['slope'])):
    slope = float(df['slope'][i])
    slope = "{:0.2f}".format(slope)
    if slope <= str(0.1):
        list_5.append(df['height'][i])
    if str(0.1) < slope <= str(0.5):
        list_10.append(df['height'][i])
    if str(0.5) < slope <= str(0.9):
        list_15.append(df['height'][i])
    if str(0.9) < slope <= str(1.3):
        list_20.append(df['height'][i])
    if slope > str(1.3):
        list_30.append(df['height'][i])

sum_list = []
sum_list.append(list_5)
sum_list.append(list_10)
sum_list.append(list_15)
sum_list.append(list_20)
sum_list.append(list_30)


c = Boxplot()
c.add_xaxis(["0-0.1", "0.1-0.5","0.5-0.9", "0.9-1.3","1.3以上"])
c.add_yaxis("ATLAS Elevation-Airborne LiDAR Elevation(m)", c.prepare_data(sum_list))

c.set_global_opts(title_opts=opts.TitleOpts(title="All data"),xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),)
c.render("boxplot.html")
