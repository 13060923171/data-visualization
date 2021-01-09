from pyecharts.charts import Line
#导入随机数据库，方便我们写代码测试
from pyecharts.faker import Faker
from pyecharts import options as opts
#创建一个折线图
line = (Line()
        #添加X轴,X轴的数据采用faker数据，Faker.choose得到的是一个字符串列表，一般用在x轴
        .add_xaxis(xaxis_data=Faker.choose())
        #添加Y轴，采用Faker数据，Faker.values返回整形列表，一般用在y轴,is_smooth美化功能
        .add_yaxis(
        #设置名字
        series_name='',
        #Y轴上面的数据
        y_axis=[120, 200, 150, 80, 70, 110, 130],
        #数据点的形状:'circle', 'rect', 'roundRect', 'triangle',     'diamond', 'pin', 'arrow', 'none'
        symbol='arrow',
        #形状的大小
        symbol_size=15,
        #连接线条的颜色，宽度和类型,type_表示线的类型，一般默认为实线
        linestyle_opts=opts.LineStyleOpts(color='blue',width=3),
        #是否显示数据
        label_opts=opts.LabelOpts(is_show=True),
        #改变数据点外形，border_color指的是外层，color里面
        itemstyle_opts=opts.ItemStyleOpts(
                border_width=3,color='red'
        ),
)
        # .add_yaxis("水位",Faker.values(),is_smooth=True,areastyle_opts=opts.AreaStyleOpts(opacity=0.8))
        #添加多条Y轴就写多一行即可,areastyle_opts则是填充的意思
        # .add_yaxis("宽度",Faker.values(),is_smooth=True,areastyle_opts=opts.AreaStyleOpts(opacity=0.8))
        #生成可视化html文件
        )
line.render()

