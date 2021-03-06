"""
获取结点信息，保存为【()，()】格式，
对数据进行排序
格式转换为[{key:value}]格式，目的是分组
分组之后，自个组的key，value保存成[[key],[key]],[[value],[value]]
"""
import re
from operator import itemgetter
from itertools import groupby
import time
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
            #for i in range(30000):
            #for i in range(1000):

            pointLists.append([score, s1, s2])
                #pointLists.append([float(score), s1, s2])
            previous_s1 = s1
            previous_s2 = s2
            #pointList.append()
        #print(line)
        #return line
    fR.close()
    #print("pointLists:", pointLists)
    #print("np_pointLists:", np.array(pointLists))
    return pointLists


"""
排序
如果是所个关键词比较，可以用一下方法，先比较第一关键词，相等再比较第二个
    #lists.sort(key=operator.itemgetter(0，1))
    lists.sort(key=lambda x:(x[0],x[1]))
"""
def listSort(lists):
    #operator.itemgetter排序，0表示第一个维度，1表示第二维度
    #lists.sort(key=operator.itemgetter(0))
    lists.sort(key=lambda x:(x[0]))
    #print("lists:", lists)
    return lists

#把原有的格式list[(1,2,3)]转化成dict，{'key':1,'value':(1,2,3)}
#目的是为了进行分组，分组需要key
def getLists(lists):
	dLists=[]
	for i,value in enumerate(lists):
		d={}
		flag = value[0]
		d['key'] = flag
		d['value'] = value
		dLists.append(d)
	return dLists

#把dict分组，使用了groupby的方法分组之前，得先排序sort
#迭代，分别将key和value保存到2个list(groupName,groupValue)
def groupLists(lists):
	dLists = getLists(lists)
    #分组之前最好先排序
	dLists.sort(key = itemgetter('key'))
	groupLists = groupby(dLists, itemgetter('key'))
	#组名 组的值
	groupName = []
	groupValue = []
	for key,group in groupLists:
		groupName.append(key)
		v = []
		for value in group:
			v.append(value['value'])
			#print("value:", value['value'])
		groupValue.append(v)		
	return (groupName,groupValue)

"""
比较opt1和opt2的变化的差
"""
def get_diff(lists):
    previous_s1 = lists[0][1]
    previous_s2 = lists[0][2]
    abnormal_lists = []
    for list in lists:
        #print(list)
        #插入前一个值
        #取出s1,s2的值
        s1 = list[1]
        s2 = list[2]
        #相减取差
        diff_s1 = s1 - previous_s1
        diff_s2 = s2 - previous_s2

        #输出验证differ的结果
        #print("diff_s1:", diff_s1)
        #print("diff_s2:", diff_s2)
        #插入s1,s2相减取差的值
        list.append(diff_s1)
        list.append(diff_s2)

        #把不正常的值的列表取出来
        diff_s1_abs = abs(diff_s1)
        diff_s2_abs = abs(diff_s2)
        if(diff_s1_abs > 5 or diff_s2_abs > 5):
            #print("diff_s1_abs:", diff_s1_abs)
            #print("diff_s2_abs:", diff_s2_abs)
            abnormal_lists.append(list)
            abnormal_lists.append(list)
            #print("abnormal_lists:", abnormal_lists)

        #将上次的s1,s2赋值给diff_s1,diff_s2
        previous_s1 = s1
        previous_s2 = s2
    print(lists)
    return (lists,abnormal_lists)

def get_diff_np(np_points):
    temp_np_points = np.array(np_points)
    #其实还是指向原本的内存，只是获取不同的内容
    #opt1&opt2
    #print(type(temp_np_points))
    opt_np_points = temp_np_points[:,1:].astype(float)
    #每个point的第一个维度
    first_list = opt_np_points[:1]
    #assert 0, first_list
    opt_np_points_v = np.vstack((first_list, opt_np_points))
    #print("================")
    #获取opt1&opt2的差值, opt1-opt1_previous, opt2-opt2_previous
    #print("opt_np_points:", opt_np_points)
    #print("opt_np_points_v[:-1]:", opt_np_points_v[:-1])
    diff_opt = opt_np_points - opt_np_points_v[:-1]
    #把2个数组拼起来，vstack((a,b))是竖着拼，hstack((a,b))是横着拼
    np_points = np.hstack((temp_np_points, diff_opt))
    #print("np_points:", np_points)
    #print("temp_np_points:", temp_np_points)
    #print("np_points:", np_points)
    print("np_points:", np_points)
    return np_points

if __name__ == '__main__':
    start = time.clock()
    lists = get_point('source.txt')
    sort_lists = listSort(lists)
    get_diff(sort_lists)#0.63,0.722,0.74,0.57
    #get_diff_np(sort_lists)#2.43,2.59,2.24,2.55
    end = time.clock()
    #程序运行的时间
    print("程序运行的时间:",end-start)
