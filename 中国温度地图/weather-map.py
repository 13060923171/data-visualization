from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.faker import Faker
from pyecharts.globals import ChartType,CurrentConfig,NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB
from openpyxl import load_workbook
import requests

city_code = {}
sheet = load_workbook('AMap_adcode_citycode.xlsx').active
for row in sheet.rows:
    city,code, _ = row
    city = city.value
    code = code.value
    try:
        if city[-1] == '市' or city[-3] == '自治区':
            list.append(city)
            city_code[city] = code
    except:
        pass
city_weather = []
for city,code in city_code.items():
    req = requests.get('https://restapi.amap.com/v3/weather/weatherInfo?key=e151ce35ee68dca653fa2a301b9f5050&city={}'.format(code))
    result = req.json()
    city_weather.append([city,result['lives'][0]['temperature']])

c = (
    Geo(is_ignore_nonexistent_coord=True)
    .add_schema(maptype="china")
    .add(
        "geo",
        city_weather,
        type_=ChartType.HEATMAP,
        label_opts=opts.LabelOpts(is_show=False)
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="Geo-HeatMap"),
    )
    .render('weather_map.html')
)
