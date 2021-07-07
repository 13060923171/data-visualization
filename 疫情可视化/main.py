import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


def the_new_diagnosis(df):
    x_data = [str(x)[5:-9] for x in df['日期']]
    y_data = [int(y) for y in df['新增确诊']]
    plt.figure(figsize=(15, 8), dpi=100)
    plt.scatter(x_data,y_data,marker='o',color='Tomato')
    plt.xticks(rotation=60)
    plt.ylabel('单位:人数')
    plt.xlabel('单位:时间')
    plt.title('1月到3月-新增确诊人数')
    plt.savefig('新增确诊.png')
    plt.show()

def the_cumulative_confirmed(df):
    x_data = [str(x)[5:-9] for x in df['日期']]
    y_data = [int(y) for y in df['累计确诊']]
    plt.figure(figsize=(15, 8), dpi=100)
    plt.plot(x_data, y_data, marker='*', color='Violet')
    plt.xticks(rotation=60)
    plt.ylabel('单位:人数')
    plt.xlabel('单位:时间')
    plt.title('1月到3月-累计确诊人数')
    plt.savefig('累计确诊.png')
    plt.show()

def cumulative_death(df):
    x_data = [str(x)[5:-9] for x in df['日期']]
    y_data = [int(y) for y in df['累计死亡']]
    plt.figure(figsize=(15, 8), dpi=100)
    plt.bar(x_data, y_data, color='Red')
    plt.xticks(rotation=60)
    plt.ylabel('单位:人数')
    plt.xlabel('单位:时间')
    plt.title('1月到3月-累计死亡人数')
    plt.savefig('累计死亡.png')
    plt.show()

def the_cumulative_cure(df):
    x_data = [str(x)[5:-9] for x in df['日期']]
    y_data = [int(y) for y in df['累计治愈']]
    plt.figure(figsize=(15, 8), dpi=100)
    plt.plot(x_data, y_data, marker='v', color='Lime')
    plt.xticks(rotation=60)
    plt.ylabel('单位:人数')
    plt.xlabel('单位:时间')
    plt.title('1月到3月-累计治愈人数')
    plt.savefig('累计治愈.png')
    plt.show()


def lethallty_rate(df):
    x_data = [str(x)[5:-9] for x in df['日期']]
    y_data = [float(y) * 100 for y in df['致死率']]
    plt.figure(figsize=(15, 8), dpi=100)
    plt.scatter(x_data, y_data, marker='*', color='OrangeRed')
    plt.ylim(0.00, 4.50)
    plt.xticks(rotation=60)
    plt.ylabel('单位:%)')
    plt.xlabel('单位:时间')
    plt.title('1月到3月-致死率')
    plt.savefig('致死率.png')
    plt.show()





if __name__ == '__main__':
    df = pd.read_excel('国内疫情数据.xls').loc[:,['日期','新增确诊','累计确诊','累计死亡','累计治愈','致死率']]
    the_new_diagnosis(df)
    the_cumulative_confirmed(df)
    cumulative_death(df)
    the_cumulative_cure(df)
    lethallty_rate(df)