import pandas as pd
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType

df = pd.read_csv('pd_CityU.csv')
amount_2015 = []
amount_2016 = []
amount_2017 = []
amount_2018 = []
amount_2019 = []
amount_2020 = []
for t in range(len(df['发布日期'])):
    try:
        df['发布日期'][t] = df['发布日期'][t][:-3]
        if '2015' in df['发布日期'][t]:
            if '万' in df['播放量'][t]:
                df['播放量'][t] = df['播放量'][t].replace('万','')
                df['播放量'][t] = int(float(df['播放量'][t]) * 10000)
                amount_2015.append(df['播放量'][t])
            else:
                amount_2015.append(df['播放量'][t])
        if '2016' in df['发布日期'][t]:
            if '万' in df['播放量'][t]:
                df['播放量'][t] = df['播放量'][t].replace('万', '')
                df['播放量'][t] = int(float(df['播放量'][t]) * 10000)
                amount_2016.append(df['播放量'][t])
            else:
                amount_2016.append(df['播放量'][t])
        if '2017' in df['发布日期'][t]:
            if '万' in df['播放量'][t]:
                df['播放量'][t] = df['播放量'][t].replace('万','')
                df['播放量'][t] = int(float(df['播放量'][t]) * 10000)
                amount_2017.append(df['播放量'][t])
            else:
                amount_2017.append(df['播放量'][t])
        if '2018' in df['发布日期'][t]:
            if '万' in df['播放量'][t]:
                df['播放量'][t] = df['播放量'][t].replace('万','')
                df['播放量'][t] = int(float(df['播放量'][t]) * 10000)
                amount_2018.append(df['播放量'][t])
            else:
                amount_2018.append(df['播放量'][t])
        if '2019' in df['发布日期'][t]:
            if '万' in df['播放量'][t]:
                df['播放量'][t] = df['播放量'][t].replace('万','')
                df['播放量'][t] = int(float(df['播放量'][t]) * 10000)
                amount_2019.append(df['播放量'][t])
            else:
                amount_2019.append(df['播放量'][t])
        if '2020' in df['发布日期'][t]:
            if '万' in df['播放量'][t]:
                df['播放量'][t] = df['播放量'][t].replace('万','')
                df['播放量'][t] = int(float(df['播放量'][t]) * 10000)
                amount_2020.append(df['播放量'][t])
            else:
                amount_2020.append(df['播放量'][t])
    except:
        pass

sum_2015 = 0
for j in amount_2015:
    sum_2015 += int(j)
avg_2015 = int(sum_2015/len(amount_2015))

sum_2016 = 0
for j in amount_2016:
    sum_2016 += int(j)
avg_2016 = int(sum_2016/len(amount_2016))

sum_2017 = 0
for j in amount_2017:
    sum_2017 += int(j)
avg_2017 = int(sum_2017/len(amount_2017))

sum_2018 = 0
for j in amount_2018:
    sum_2018 += int(j)
avg_2018 = int(sum_2018/len(amount_2018))

sum_2019 = 0
for j in amount_2019:
    sum_2019 += int(j)
avg_2019 = int(sum_2019/len(amount_2019))

sum_2020 = 0
for j in amount_2020:
    sum_2020 += int(j)
avg_2020 = int(sum_2020/len(amount_2020))

x_data = ['2015','2016','2017','2018','2019','2020']
y_data = [avg_2015,avg_2016,avg_2017,avg_2018,avg_2019,avg_2020]
c = (
    Bar({"theme": ThemeType.MACARONS})
    .add_xaxis(x_data)
    .add_yaxis("年度播放平均值", y_data)
    .set_global_opts(
        title_opts={"text": "发布时间与播放量关系图"}
    )
    .render("bar_config.html")
)