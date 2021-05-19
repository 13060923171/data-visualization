import pandas as pd
import pyecharts.options as opts
from pyecharts.charts import Line,Timeline

#读取文件
df = pd.read_csv('ecg.csv').loc[:,['time','voltage']]

#生成X轴数据
x_data = []
for i in df['time']:
    i = float(i)
    x_data.append("{:.3}".format(i))

#生成Y轴数据
y_data = []
for i in df['voltage']:
    y_data.append(i)

#生成时间轴
tl = Timeline()

for j in range(len(x_data[:-100])):
    c = (
        #设置画布的宽和长
        Line(init_opts=opts.InitOpts(width="1300px", height="600px"))
            #把变量的X轴传入到图表里面
            .add_xaxis(xaxis_data=[x_data[j+k] for k in range(0,100)])
            # .add_xaxis(xaxis_data=[x_data[j],x_data[j+1],x_data[j+2],x_data[j+3],x_data[j+4],x_data[j+5],x_data[j+6],x_data[j+7],x_data[j+8],x_data[j+9],x_data[j+10],x_data[j+11],x_data[j+12],x_data[j+13],x_data[j+14],x_data[j+15],x_data[j+16],x_data[j+17],x_data[j+18],x_data[j+19],x_data[j+20],x_data[j+21],x_data[j+22],x_data[j+23],x_data[j+24],x_data[j+25],x_data[j+26],x_data[j+27],x_data[j+28],x_data[j+29]])
            .add_yaxis(
            #Y轴的名称
            series_name="心电信号",
            #类型
            symbol="emptyCircle",
            #是否显示数据
            is_symbol_show=False,
            #颜色
            color="#d14a61",
            #变量的Y轴数据
            y_axis=[y_data[j+k] for k in range(0,100)],
            # y_axis=[y_data[j],y_data[j+1],y_data[j+2],y_data[j+3],y_data[j+4],y_data[j+5],y_data[j+6],y_data[j+7],y_data[j+8],y_data[j+9],y_data[j+10],y_data[j+11],y_data[j+12],y_data[j+13],y_data[j+14],y_data[j+15],y_data[j+16],y_data[j+17],y_data[j+18],y_data[j+19],y_data[j+20],y_data[j+21],y_data[j+22],y_data[j+23],y_data[j+24],y_data[j+25],y_data[j+26],y_data[j+27],y_data[j+28],y_data[j+29]],
            label_opts=opts.LabelOpts(is_show=False),
            #线的宽度
            linestyle_opts=opts.LineStyleOpts(width=3)
        )
            .set_global_opts(
            #标题
            title_opts=opts.TitleOpts(title="心电信号"),

            tooltip_opts=opts.TooltipOpts(trigger="axis"),
            #Y轴的上面内容
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name="毫伏(mV)",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            #X轴轴的颜色和一些其他的参数
            xaxis_opts=opts.AxisOpts(type_="category", boundary_gap=False,axisline_opts=opts.AxisLineOpts(
                is_on_zero=False, linestyle_opts=opts.LineStyleOpts(color="#d14a61")
            )),

        )
    )
    #把生成好的折线图传入到时间轴里面
    tl.add(c,'{}年'.format(j))
    #时间轴的参数配置
    tl.add_schema(
        # 播放速度
        play_interval=100,
        # 是否显示timeline组件
        is_timeline_show=False,
        # 是否自动播放
        is_auto_play=True,
    )
    #最后生成HTML文件
tl.render('time_line.html')
