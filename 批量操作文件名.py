# -*- coding:utf8 -*-

import os
import pandas as pd
class BatchRename():
    '''
    批量重命名文件夹中的图片文件

    '''
    def __init__(self):
        self.path = 'C:/Users/96075/Desktop/微博评论加头像/上海外国语大学3000个头像/shisu1949'

    def rename(self):
        data = pd.read_excel('清华.xlsx')
        filelist = os.listdir(self.path)
        total_num = len(filelist)
        i =0
        for item in filelist:
            if item.endswith('.png'):
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path), str(data['name'][i]) + '.png')
                i = i + 1
                try:
                    os.rename(src, dst)
                    print('converting %s to %s ...' % (src, dst))

                except:
                    continue
        print('total %d to rename & converted %d jpgs' % (total_num, i))

if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()
