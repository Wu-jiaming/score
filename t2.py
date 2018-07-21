
import re
import operator
import xlwt

"""
获取相关节点
"""
def get_point(sourcePath):
    fR = open(sourcePath, 'r+' , encoding='utf-8')
    lines = fR.readlines()
    pointList = []
    pointLists = []
    temp = []
    allLists = {}
    for line in lines:
        pointPattern = re.compile(r'.*?Point.(.*?)s.*?opt1:"(.*?)"f.*?opt2:"(.*?)"')
        pointList = re.match(pointPattern, line)
        if pointList is not None:
            #pointLists.append(())
            point = pointList.group(1)
            opt1 = pointList.group(2)
            opt2 = pointList.group(3)

            pointLists.append((point, opt1, opt2))
            #print("point:", point , "opt1:", opt1)

            if temp==point:
                allLists.append((point, opt1, opt2))
            else:
                temp = point
        #pointList.append()
        #print(line)
        #return line
    fR.close()
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
    for i in range(len(lists)):
        print(i+1, lists[i])
    return lists

"""
保存txt格式
result.write(str(list), '\n')这种写法是错误的
result.writelines(str(list))这种是没法换行的,这种写法只是自动迭代，譬如列表，元组
"""
def fileWrite(headerLists, valueLists, newFilePath):
    with open(newFilePath, 'w') as result:
        for headerList in headerLists:
            result.write(str(headerList) + '\n')

        for list in valueLists:
            result.write(str(list)+ '\n')
            #result.write(repr(list)+ '\n')
            #result.writelines(list)

"""
书写xls
"""
def xlsxWrite(lists, sheet ,header):
    #判断是否头标题,enumerate有点迭代的意思，row为key，rValue为值
    if(header is True):
        for row,rValue in enumerate(lists):
            for col,Value in enumerate(rValue):
                sheet.write(row, col, Value)
    else:
        for row,rValue in enumerate(lists):
            for col,Value in enumerate(rValue):
                sheet.write(row+1, col, Value)        

"""
保存为xls格式
"""
def xlsSave(headerLists, valueLists, newXlsPath):
    headerLists = headerLists#[(('point'), ('opt1'), ('opt2'))]
    wb = xlwt.Workbook('encoding=utf-8')
    sheet = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)
    xlsxWrite(headerLists, sheet,True)
    xlsxWrite(valueLists, sheet, False)
    wb.save(newXlsPath)


"""
读取文件
"""
def fileRead(filePath):
    result = open(filePath, 'r')
    lines = result.readlines()
    for line in lines:
        print(line)


def main():
    sourcePath = 'source.txt'
    Pointlists = get_point(sourcePath)#获取已经排序好的列表
    headerLists = [(('point'), ('opt1'), ('opt2'))]
    valueLists = listSort(Pointlists)

    newTxtPath = 'result.txt'
    newXlsPath = 'point.xls'
    fileWrite(headerLists, valueLists, newTxtPath)
    xlsSave(headerLists, valueLists, newXlsPath)

if __name__ == '__main__':
    main()