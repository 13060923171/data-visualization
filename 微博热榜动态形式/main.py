import requests
from bs4 import BeautifulSoup
import time
import csv
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
}
def get_parse(url):
    html = requests.get(url,headers = headers)
    if html.status_code ==200:
        get_html(html)
    else:
        print(html.status_code)
def get_html(html):
    content = html.text
    soup = BeautifulSoup(content,'lxml')
    for i in range(10):
        result = []
        ranktop = soup.select('tr td.td-01.ranktop')[i].text
        title = soup.select('tr td.td-02 a')[i+1].text
        num = soup.select('tr td.td-02 span')[i].text
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        result.append(t)
        result.append(ranktop)
        result.append(num)
        result.append(title)
        print(ranktop, title, num)
        with open('微博热榜.csv',"a+",newline='')as f:
            f_csv = csv.writer(f)
            f_csv.writerow(result)


if __name__ == '__main__':
    url = 'https://s.weibo.com/top/summary'
    while True:
        get_parse(url)
        time.sleep(60)