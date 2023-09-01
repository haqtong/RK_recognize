# encoding=utf-8
import logging
import pandas as pd
import datetime
import numpy as np
import os
import sys
import json
import math

np.random.seed(804)
fn = sys.argv[0].split('/')[-1].split('.')[0]
filename = 'log/' + sys.argv[0].split('/')[-1].split('.')[0] + '.log'

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename=filename, level=logging.INFO, format=LOG_FORMAT)

def paper_item():
    '''
    论文专题
    :return:
    '''
    manag_10() # 10大管理 输入输出工具

def exec():



if __name__ == '__main__':
    exec()