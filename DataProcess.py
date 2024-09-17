import pandas as pd
import codecs
import csv
import numpy as np
from tqdm import tqdm
import os
import re
import matplotlib.pyplot as plt

"""
Data Csv Process
"""
"""
BJ :
Label 1
sensor(NO) 453
pieces 8760

TJ :
Label 2
sensor(NO) 301
pieces 8760
"""
# BJ_position = pd.read_csv('./dataset/北京-天津气象数据集2022/北京-天津气象数据集2022/BJ_position.csv')
# TJ_position = pd.read_csv('./dataset/北京-天津气象数据集2022/北京-天津气象数据集2022/TJ_position.csv')
# dataset_location = pd.concat([BJ_position, TJ_position])
# print(dataset_location)
"""
The data is not paired with coordinates
"""
def get_data(path):
    dataset_list = []
    # print(os.listdir(path))
    # print(os.path.basename(path))
    for file in tqdm(os.listdir(path)):  ##进度条
        file_path = os.path.join(path, file)
        df = pd.read_csv(file_path)
        full_filename = os.path.basename(file_path) # 带后缀
        filename = full_filename.split('.')[0] # 不带后缀
        # print(re.findall(r"\d+", str(filename))[0])
        df['NO'] = int(re.findall(r"\d+", str(filename))[0])
        if os.path.basename(path) == 'BJ':
            df['label'] = 1
        else:
            df['label'] = 2
        dataset_list.append(df)
    df = pd.concat(dataset_list)
    return df

"""
The data is paired with coordinates
"""
def get_data2(path):
    dataset_list2 = []
    lat = []
    lon = []
    tem = []
    # print(os.listdir(path))
    # print(os.path.basename(path))
    for file in tqdm(os.listdir(path)):  ##进度条
        file_path = os.path.join(path, file)
        df = pd.read_csv(file_path)
        lat.append(df.loc[0,'lat'])
        lon.append(df.loc[0,'lon'])
        tem.append(df.loc[:,'TEM'].astype(str))
        # tem = np.vstack((tem,df.loc[:,'TEM'].values))
        #TEM_data = np.vstack((tem, np.transpose(df.loc[0,'lon'])))
    data_location = np.transpose(np.vstack((lat, lon)))
    # tem_data = np.asarray(tem)
    # print(type(df.loc[:,'TEM'].values))
    # print(tem)
    dff = pd.concat([pd.DataFrame({'{}'.format(index): labels}) for index, labels in enumerate(tem)], axis=1)
    # print(data_location)
    return dff.fillna(0).values.T,data_location





