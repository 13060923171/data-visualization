import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line


df = pd.read_excel('副本组合净值.xlsx').loc[6:,['Unnamed: 0','Unnamed: 1','Unnamed: 2']]

time_list = []
for t in df['Unnamed: 0']:
    t = str(t)
    time_list.append(t[:-9])

moni_list = []
for m in df['Unnamed: 1']:
    m = str(m)
    moni_list.append(m)

ben_list = []
for b in df['Unnamed: 2']:
    b = str(b)
    ben_list.append(b)

(
    Line(init_opts=opts.InitOpts(width="1300px", height="600px"))
    .add_xaxis(xaxis_data=time_list)
    .add_yaxis(
        series_name="组合净值走势模拟",
        symbol="emptyCircle",
        is_symbol_show=False,
        color="#d14a61",
        y_axis=moni_list,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=2)
    )
    .add_yaxis(
        series_name="benchmark——非标",
        symbol="emptyCircle",
        is_symbol_show=False,
        color="#6e9ef1",
        y_axis=ben_list,
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=2)
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="股票走势"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,axisline_opts=opts.AxisLineOpts(
                is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#d14a61")
            )),
    )
    .render("股票走势.html")
)

