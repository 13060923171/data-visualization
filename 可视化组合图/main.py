from pyecharts.charts import Bar,Line,Grid,Page
from pyecharts import options as opts
from pyecharts.faker import Faker
x = Faker.choose()
y = Faker.values()

bar = (
    Bar()
    .add_xaxis(x)
    .add_yaxis("销量",y)
)

line = (
    Line()
    .add_xaxis(x)
    .add_yaxis("销量",y)
)
#grid,并行多图，它可以使得多个图表并行的排成一排
# grid = (
#     #设置页面的宽度
#     Grid(init_opts=opts.InitOpts(width='1200px'))
#     #GridOpts就是为grid布局而生的一个配置项,常用的几个参数pos_top，pos_bottom，pos_left，pos_right
#     .add(bar,grid_opts=opts.GridOpts(is_show=True,pos_top="50%",background_color='red',border_color='black'))
#     .add(line,grid_opts=opts.GridOpts(is_show=True,pos_bottom='50%',border_color='blue'))
#     .render()
# )
#page 顺序多图,有3种布局管理器：默认，SimplePageLayout，GraggablePageLayout
page = (
    #布局管理器会自动寻找最佳的布局方案并给与适当的间隔
    # Page(layout=Page.SimplePageLayout)
    #布局管理器可以拖拽
    Page(layout=Page.DraggablePageLayout)
    .add(bar,line)
    .render()
)