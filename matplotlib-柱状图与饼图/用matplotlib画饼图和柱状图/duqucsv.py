from GetCsvColumn import CsvFile,EXCLUDE
import pandas as pd


def csvwenjian(id):
    list = []
    list.append(csvfile.get_column('body_type',transmission='{}'.format(id)))
    content = list[0]
    # list2 = []
    # list2.append(csvfile.get_column('面积',城市='{}'.format(id)))
    # context = list2[0]
    a = [x for x in content]
    # b = [x for x in context]
    dataframe = pd.DataFrame({'body_type':a})
    dataframe.to_csv(r"{}.csv".format(id),sep=',')
    print('执行完毕')

if __name__ == '__main__':
    #需要读取的csv的名字
    csvfilename = 'xtrain.csv'
    csvfile = CsvFile(csvfilename)
    csvwenjian(input("请输入你要搜索的id:"))









