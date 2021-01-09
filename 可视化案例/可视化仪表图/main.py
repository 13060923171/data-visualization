#导入仪表盘
from pyecharts.charts import Gauge
from pyecharts import options as opts
from pyecharts.globals import ThemeType as tt
#若是要显示在仪表盘内的文字，则应该写在第二个格式为[(数据项名,值),(数据项名,值)]的字典里
gauge = (
    #改变背景颜色
    Gauge(init_opts=opts.InitOpts(theme=tt.LIGHT))
    # #is_clock_wise为改变是顺着还是逆着，split_number：仪表盘分割的段数，min_，max_：最大值，最小值
    # .add('完成率',[('',7777)],is_clock_wise=True,split_number=10,min_=1000,max_=10000,radius="100%")
    # .render()
    #配置仪表盘的
    .add('完成率',[('',66.66)],radius='80%',detail_label_opts=opts.GaugeDetailOpts(
        font_style='italic',#字体的样式，可选的有normal,italic,oblique
        font_family='serif',#字体
        font_size=20,#字号
        font_weight='lighter',#文字粗细，bord,border,lighter
        offset_center=[0,'-60%']#距离中心的偏移值，第一个是水平偏移，第二个是垂直偏移
    ),  #配置指针的
         pointer=opts.GaugePointerOpts(
        length=100,#length指的是指针长度
        width=8#宽度，可以是绝对值也可以是相对数值
    ))
    #改变仪表盘的颜色
    .set_series_opts(
        axisline_opts=opts.AxisLineOpts(
            linestyle_opts=opts.LineStyleOpts(
                color=[[0.3, "#67e0e3"], [0.7, "#37a2da"], [1, "#fd666d"]], width=30
            )
        )
    )


    .render()
)