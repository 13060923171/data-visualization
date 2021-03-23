import pandas as pd

from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline
from pyecharts.charts import Line
from pyecharts.charts import Page
from pyecharts.globals import ThemeType

df = pd.read_excel('World.xlsx').loc[:,['year','CO2 emissions from residential buildings and commercial and public services (% of total fuel combustion)','CO2 emissions from transport (% of total fuel combustion)','CO2 emissions from electricity and heat production, total (% of total fuel combustion)','CO2 emissions from manufacturing industries and construction (% of total fuel combustion)','CO2 emissions from other sectors, excluding residential buildings and commercial and public services (% of total fuel combustion)','CO2 emissions (kt)','Forest area (sq. km)','GDP per capita (constant 2010 US$)']]

list_year = []
for i in df['year']:
    list_year.append(i)

list_residential = []
for i in df['CO2 emissions from residential buildings and commercial and public services (% of total fuel combustion)']:
    list_residential.append(i)

list_transport = []
for i in df['CO2 emissions from transport (% of total fuel combustion)']:
    list_transport.append(i)

list_electricity = []
for i in df['CO2 emissions from electricity and heat production, total (% of total fuel combustion)']:
    list_electricity.append(i)

list_manufacturing = []
for i in df['CO2 emissions from manufacturing industries and construction (% of total fuel combustion)']:
    list_manufacturing.append(i)

list_other = []
for i in df['CO2 emissions from other sectors, excluding residential buildings and commercial and public services (% of total fuel combustion)']:
    list_other.append(i)

x_data = ['CO2 emissions from residential buildings and commercial and public services','CO2 emissions from transport','CO2 emissions from electricity and heat production, total','CO2 emissions from manufacturing industries and construction','CO2 emissions from other sectors, excluding residential buildings and commercial and public services']

x_data1 = []
for i in list_year:
    i = str(i)
    i = i + '年'
    x_data1.append(i)


list_kt = []
for i in df['CO2 emissions (kt)']:
    list_kt.append(i)

list_sq = []
for i in df['Forest area (sq. km)']:
    list_sq.append(i)

list_constant = []
for i in df['GDP per capita (constant 2010 US$)']:
    list_constant.append(i)


def pie_basic() -> Pie:
    tl = Timeline()
    for i in range(len(list_year)):
        pie = (
            Pie(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
            .add(
                "",
                [list(z) for z in zip(x_data,[list_residential[i],list_transport[i],list_electricity[i],list_manufacturing[i],list_other[i]])],
                center=["50%", "50%"],
                label_opts=opts.LabelOpts(is_show=False, position="center")
            )
            .set_global_opts(legend_opts=opts.LegendOpts(pos_left="left", orient="vertical"))
            .set_series_opts(tooltip_opts=opts.TooltipOpts(trigger='item',formatter='{a} <br/>{b}: {c} ({d}%)'))
        )
        tl.add(pie, "{}年".format(list_year[i]))
    return tl


def line_basic() -> Line:
    c = (
        Line(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
        .add_xaxis(xaxis_data=x_data1)
        .add_yaxis(
            series_name="CO2 emissions (kt)",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#d14a61",
            y_axis=list_kt,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=2)
        )
        .add_yaxis(
            series_name="Forest area (sq. km)",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#6e9ef1",
            y_axis=list_sq,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=2)
        )
        .add_yaxis(
            series_name="GDP per capita (constant 2010 US$)",
            symbol="emptyCircle",
            is_symbol_show=False,
            color="#145A32",
            y_axis=list_constant,
            label_opts=opts.LabelOpts(is_show=False),
            linestyle_opts=opts.LineStyleOpts(width=2)
        )
        .set_global_opts(
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
    )
    return c


def page_draggable_layout():
    page = Page(layout=Page.SimplePageLayout)
    page.add(
        pie_basic(),
        line_basic(),

    )
    page.render()

if __name__ == '__main__':
    page_draggable_layout()
