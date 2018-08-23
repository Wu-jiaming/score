import re
import numpy as np

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
    print("pointLists:", pointLists)
    print("np_pointLists:", type(np_pointLists))
    print("np_pointLists:", np_pointLists)
    #按列排序，不会修改原数组，按第1列进行排序
    # X[:,0]就是取所有行的第0个数据,
    #如果要按行排序，可以先进行转置，如：np_pointLists.T[np_pointLists.T[:, 0].argsort()].T
    np_pointLists2 = np_pointLists[np_pointLists[:, 0].argsort()]
    print("===========================================")
    print("修改之后：", np_pointLists2)
    #print("===========================================")
    #print("修改之后原来列表：",np_pointLists)
    return pointLists

if __name__ ==  '__main__':
    get_point(sourcePath='source.txt')