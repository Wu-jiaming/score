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

            pointLists.append([float(score), s1, s2])
            previous_s1 = s1
            previous_s2 = s2
            #pointList.append()
        #print(line)
        #return line
    fR.close()
    np_pointLists = np.array(pointLists)
    #按列排序，不会修改原数组，按第1列进行排序
    # X[:,0]就是取所有行的第0个数据,
    #如果要按行排序，可以先进行转置，如：np_pointLists.T[np_pointLists.T[:, 0].argsort()].T
    np_pointLists2 = np_pointLists[np_pointLists[:, 0].argsort()]
    return np_pointLists2


def get_diff(np_points):
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
    print("np_points:", np_points)
    print("temp_np_points:", temp_np_points)
    print("np_points:", np_points)
    return np_points