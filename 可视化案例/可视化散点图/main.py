from pyecharts.charts import Scatter
from pyecharts import options as opts
from pyecharts.faker import Faker

scatter = (
    Scatter()
    #在所有直角坐标里面都需要添加这两步，确定Y轴和X轴
    .add_xaxis(Faker.choose())
    .add_yaxis('销量',
               Faker.values(),
               #图像形状
               symbol='diamond',
               #节点的大小，颜色
               itemstyle_opts=opts.ItemStyleOpts(border_width=10,border_color='green',color='blue',opacity=0.8))
    #set_global_opts设定配置项，VisualMapOpts是全局变量中的视觉映射配置项，也就是说是用来调整颜色区间和大小区间的
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(type_='color',max_=200),
        #显示分割线
        xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
        yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
        # visualmap_opts=opts.VisualMapOpts(type_="color",pieces=[
        #     {"min":10,"max":100,"color":"red"},
        #     {"min":100,"max":1000,"color":"orange"},
        #     {"min":1000,"max":10000,"color":"blue"},
        #     {"min":10000,"max":100000,"color":"green"}
        # ])
    #pieces：自定义的颜色区间，一个元素为字典的列表

    )
)
scatter.render()