# encoding=utf-8
import logging
import pandas as pd
import datetime
import numpy as np
import os
import sys
import json
import math

fn = sys.argv[0].split('/')[-1].split('.')[0]
filename = 'log/' + sys.argv[0].split('/')[-1].split('.')[0] + '.log'

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(filename=filename, level=logging.INFO, format=LOG_FORMAT)


def exec():
    list = ['项目整体管理', '项目范围管理', '项目风险管理', '项目成本管理', '项目进度管理',
            '项目质量管理', '项目采购管理', '项目沟通管理', '项目人力资源管理', '项目干系人管理']
    _ = np.random.choice(list, 1)

    print(_)

def E_c_random_test():
    infnf = r'D:\program\data\软考\data\英文'
    df = pd.read_csv(infnf,encoding='gbk')
    aim_dict = df.set_index('英文名')['中文名'].to_dict()
    # print(aim_dict)
    _ = np.random.choice(list(aim_dict.keys()), 1)
    print(_)
    print('请输入中文名：')
    cn = input()
    if aim_dict[_[0]] == cn:
        print('pass')
    else:
        print(aim_dict[_[0]])




if __name__ == '__main__':
    exec()
    # E_c_random_test()
