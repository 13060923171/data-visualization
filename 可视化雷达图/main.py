#导入可视化雷达的库
from pyecharts.charts import Radar
from pyecharts import options as opts
from pyecharts.faker import Faker

#雷达各方面的数值
sc = [{'name':x} for x in Faker.choose()]
radar = (
    Radar(init_opts=opts.InitOpts(width='1000px'))
    #雷达各个角的名字
    .add_schema(
        sc,
        #改变整个雷达的形状
        shape='circle',
        radius='80%'

    )
    #销量的x，y值
    .add(
        '销量',
        [Faker.values(),Faker.values()],
        #改变节点的形状
        symbol='roundRect',
        #改变线的粗细
        linestyle_opts=opts.LineStyleOpts(
            type_='dash'
        )
    )
    # .set_global_opts(legend_opts=opts.LegendOpts(selected_mode='single'))
    #给雷达添加填充
    .set_series_opts(areastyle_opts=opts.AreaStyleOpts(opacity=0.1))
    .render()
)