#导入可视化雷达的库
from pyecharts.charts import Radar,Timeline
from pyecharts import options as opts
from pyecharts.faker import Faker

list_name = ['MPG','HP','FGM','AM','WT','MIN','FGA']
time = ['1999','2002','2005','2009','2012']
l1 = ['0.110532','0.227481','0.787654','38.598485','5.378788','4.651515','1.530303']
l2 = ['0.13099','0.22083','0.83492','42.827236','5.980691','5.510163','1.686992']
l3 = ['0.124582','0.236655','0.810325','42.921607','5.799107','4.821429','1.490179']
l4 = ['0.117158','0.228567','0.826495','39.479244','5.678082','5.23913','1.447886']
l5 = ['0.108108','0.231348','0.819672','38.623077','5.551282','6.012821','1.358974']
l6 = [l1,l2,l3,l4,l5]

print(l6[1])

def index():
    schema = [
        opts.RadarIndicatorItem(name="MPG", max_=1),
        opts.RadarIndicatorItem(name="HP", max_=1),
        opts.RadarIndicatorItem(name="FGM", max_=2),
        opts.RadarIndicatorItem(name="AM", max_=45),
        opts.RadarIndicatorItem(name="WT", max_=7),
        opts.RadarIndicatorItem(name="MIN", max_=7),
        opts.RadarIndicatorItem(name="FGA", max_=3),
    ]
    # sc = [{'name':x} for x in list_name]
    tl = Timeline()
    for i in range(len(time)):
        radar = (
            Radar(init_opts=opts.InitOpts(width='1000px'))
                #雷达各个角的名字
                .add_schema(
                schema,
                #改变整个雷达的形状
                shape='circle',
                radius='80%'
            )
                #销量的x，y值
            .add(
                '',
                [l6[i]],
                #改变节点的形状
                symbol='roundRect',
                #改变线的粗细
                linestyle_opts=opts.LineStyleOpts(
                    type_='dash'
                )
            )
            .set_global_opts(title_opts=opts.TitleOpts("{}年".format(time[i])))
        )
        tl.add(radar,"{}年".format(time[i]))
    return tl.render("timeline_pie.html")

if __name__ == '__main__':
    index()
