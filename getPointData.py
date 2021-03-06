"""
获取结点信息，保存为【()，()】格式，
对数据进行排序
格式转换为[{key:value}]格式，目的是分组
分组之后，自个组的key，value保存成[[key],[key]],[[value],[value]]
"""
import re
from operator import itemgetter
from itertools import groupby
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import time
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
from datetime import datetime
"""
获取相关节点
"""
def get_point(sourcePath):
    print("sourcepath:", sourcePath)
    fR = open(sourcePath, 'r+' , encoding='utf-8')
    lines = fR.readlines()
    pointList = []
    pointLists = []
    for line in lines:
        pointPattern = re.compile(r'(.*?) point:(.*?) opt1:(.*?) opt2:(.*?)\n')
        pointList = re.match(pointPattern, line)
        #print(pointList.group(4))
        if pointList is not None:
            #pointLists.append(())
            score = pointList.group(2)
            date = pointList.group(1)
            s1 = pointList.group(3)
            s2 = pointList.group(4)
            s1 = float(s1)
            s2 = float(s2)
            #2次score的差
            #if(score)
            #diff_s1 = s1 - previous_s1
            #diff_s2 = s2 - previous_s2
            #for i in range(30000):
            pointLists.append([score, date, s1, s2])
            previous_s1 = s1
            previous_s2 = s2
            #pointList.append()
        #print(line)
        #return line
    fR.close()
    #groupLists = groupby(pointLists, itemgetter('key'))
    #print("pointLists:", pointLists)
    #np_pointLists = np.array(pointLists)
    # print("type:", np_pointLists.dtype.name)
    # np_pointLists = np_pointLists.astype(float)
    # print("np_pointLists:", np_pointLists)

    #按列排序，不会修改原数组，按第1列进行排序
    # X[:,0]就是取所有行的第0个数据,
    #如果要按行排序，可以先进行转置，如：np_pointLists.T[np_pointLists.T[:, 0].argsort()].T
    #np_pointLists2 = np_pointLists[np_pointLists[:, 0].argsort()]
    #return np_pointLists2
    #print(np_pointLists)
    df = DataFrame(pointLists, columns=['point', 'date', 'opt1', 'opt2'])
    #print(df)
    #print("===========")
    df = df.groupby(df.point)
    # for name,group in df:
    #    print("name:", name)
    #    print("group:", group)

    # print("list(df):", list(df))
    # df = dict(list(df))
    # print(df)
    # print("-------------")
    # print(DataFrame(df['1.1']))
    return df

def get_diff_pd(pd_points_groups):
    pd_lists = []
    for name, group in pd_points_groups:
        #print(type(np.array(group)))
        #print(np.array(group).astype(float))
        #raise ("=========")
        np_points = np.array(group)
        np_points = get_diff_np(np_points)

        df = DataFrame(np_points, columns=['point', 'date', 'opt1', 'opt2', 'diff_opt1', 'diff_opt2'])
        #print(df)
        pd_lists.append(df)
    return pd_lists

def get_diff_np(np_points):
    #print(np_points)
    temp_np_points = np_points
    #其实还是指向原本的内存，只是获取不同的内容
    #opt1&opt2
    opt_np_points = temp_np_points[:,2:]
    #每个point的第一个维度
    first_list = opt_np_points[:1]
    #assert 0, first_list
    opt_np_points_v = np.vstack((first_list, opt_np_points))
    #print("================")
    #获取opt1&opt2的差值, opt1-opt1_previous, opt2-opt2_previous
    diff_opt = opt_np_points - opt_np_points_v[:-1]
    #把2个数组拼起来，vstack((a,b))是竖着拼，hstack((a,b))是横着拼
    np_points = np.hstack((temp_np_points, diff_opt))
    #print("np_points:", np_points)
    #print("temp_np_points:", temp_np_points)
    #print("np_points:", np_points)
    #print(np_points)
    #print("np_points:", type(np_points))
    return np_points

def makePlt(pd_list):
    df = pd_list.loc[:, ['opt1', 'opt2']]
    df = DataFrame(df)
    plt.figure()
    y = df
    # 生成横纵坐标信息
    dates = pd_list.loc[:, ['date']]
    np_dates = np.array(dates)
    list_dates = np_dates.tolist()
    # 生成横纵坐标信息
    dates = ['2018-08-31 18:24:32', '2018-08-31 18:26:32', '2018-08-31 18:28:32']
    xs = [datetime.strptime(d[0], '%Y-%m-%d %H:%M:%S') for d in np_dates]
    #xs = [d[0] for d in np_dates]#如果只有这个，而没有对字符串进行date格式的转换，生成的图表x轴为空
    # print("xs:", xs)
    # print("xs:", xs)
    ys = range(len(xs))
    # 配置横坐标
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
    #以天为时间间隔
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
    #plt.xticks(pd.date_range(list_dates[0][0], list_dates[-1][0], freq='1440min'))
    # Plot
    plt.title('opt1&opt2 values')
    plt.xlabel('time')
    plt.ylabel('opt')
    plt.plot(xs, y)
    plt.gcf().autofmt_xdate()  # 自动旋转日期标记
    plt.show()

    raise

if __name__ == '__main__':
    #程序开始
    start = time.clock()
    np_points_group = get_point('source2.txt')
    pd_lists = get_diff_pd(np_points_group)
    for pd_list in pd_lists:
        print("df:", pd_list)
        print("df:", pd_list.at[0, 'point'])
        point = pd_list.at[0, 'point']
        makePlt(pd_list)

        csv_file_name = os.getcwd() + '\csv\\'+ point + '.csv'
        pd_list.to_csv(csv_file_name)
    #print(type(pd_lists))

    #print(a)
    #程序结束
    end = time.clock()
    #程序运行的时间
    print("程序运行的时间:",end-start)