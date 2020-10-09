from pyecharts.charts import Line,Bar
from pyecharts.faker import Faker
from pyecharts import options as opts

x = Faker.choose()
y = Faker.values()
line = (
    Line()
    .add_xaxis(x)
    .add_yaxis('销量',y)

)
bar = (
    Bar()
    .add_xaxis(x)
    .add_yaxis('销量',y,label_opts=opts.LabelOpts(is_show=False))
)
line.overlap(bar)
line.render()