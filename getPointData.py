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
        pointPattern = re.compile(r'.*?Point\.(.*?)s.*?opt1:"(.*?)".*?opt2:"(.*?)"')
        pointList = re.match(pointPattern, line)
        if pointList is not None:
            #pointLists.append(())
            score = pointList.group(1)
            s1 = pointList.group(2)
            s2 = pointList.group(3)
            s1 = float(s1)
            s2 = float(s2)
            #2次score的差
            #if(score)
            #diff_s1 = s1 - previous_s1
            #diff_s2 = s2 - previous_s2
            #for i in range(30000):
            pointLists.append([score, s1, s2])
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
    df = DataFrame(pointLists, columns=['point', 'opt1', 'opt2'])
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

        df = DataFrame(np_points, columns=['point', 'opt1', 'opt2', 'diff_opt1', 'diff_opt2'])
        #print(df)
        pd_lists.append(df)
    return pd_lists

def get_diff_np(np_points):
    #print(np_points)
    temp_np_points = np_points
    #其实还是指向原本的内存，只是获取不同的内容
    #opt1&opt2
    opt_np_points = temp_np_points[:,1:]
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
    return np_points

def makePlt(pd_list):
    #plt.rc('figure', figsize=(5,3))
    df = pd_list.loc[:, ['opt1', 'opt2']]
    df = DataFrame(df)
    #print("pd_list[1:2]:", pd_list.loc[:, ['opt1', 'opt2']])
    #print(pd_list.loc[2:3])
    #print()
    df.plot()
    df.plot(kind='bar')
    plt.show()
    raise

if __name__ == '__main__':
    #程序开始
    start = time.clock()
    np_points_group = get_point('source.txt')
    pd_lists = get_diff_pd(np_points_group)
    for pd_list in pd_lists:
        print("df:", pd_list)
        print("df:", pd_list.at[0, 'point'])
        makePlt(pd_list)
        point = pd_list.at[0, 'point']
        csv_file_name = 'point'+ point +'.csv'
        pd_list.to_csv(csv_file_name)
    #print(a)
    #程序结束
    end = time.clock()
    #程序运行的时间
    print("程序运行的时间:",end-start)