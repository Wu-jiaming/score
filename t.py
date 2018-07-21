from itertools import groupby
from operator import itemgetter
import xlsxwriter
import os

#把原有的格式list[(1,2,3)]转化成dict，{'key':1,'value':(1,2,3)}
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
#迭代，分别将key和value保存到list
def groupLists(lists):
	gLists = []
	dLists = getLists(lists)
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
检查结果存放目录的的路径是否正确
"""
def makeDir(dirPath):
	path = dirPath.strip()
	path = path.rstrip("\\")

	isExist = os.path.exists(path)
	if(isExist):
		print("path has existed")
		return os.getcwd()
	else:
		print("path create successful")
		return os.makedirs(path)

"""
检查资源文件是否存在
"""
def isExistFilePath(filePath):
	path = filePath.strip()
	path = path.rstrip("\\")

	isExist = os.path.exists(path)
	if(isExist):
		print("file has existed")
	else:
		print("file did not exists, ple reinput")
		return None
"""
保存txt格式
result.write(str(list), '\n')这种写法是错误的
result.writelines(str(list))这种是没法换行的,这种写法只是自动迭代，譬如列表，元组
"""
def fileWrite(headerLists, valueLists, newFilePath):
    with open(newFilePath, 'w') as result:
        # for headerList in headerLists:
        #     result.write(str(headerList) + '\n')
        result.write(str(headerLists) + '\n')

        for list in valueLists:
            result.write(str(list)+ '\n')
            #result.write(repr(list)+ '\n')
            #result.writelines(list)

def xlsxChart(fileName, type, headerLists, valueLists):
	#新建一个xlsx文件
	workBook = xlsxwriter.Workbook(fileName)
	#新建一个sheet,名字为SheetName
	workSheet = workBook.add_worksheet('SheetName')
	#Style为粗体，非0为粗体
	bold = workBook.add_format({'bold': 1})
	#标题数据
	header = headerLists
	# 真实数据
	data = valueLists
	#写入横向数据，一行，'A1'表示位置
	workSheet.write_row('A1', header, bold)
	#print("data:", data)
	for index,dataLine in enumerate(data):
		#print("index:", index, "dataLine:",dataLine)
		#注意！如果写入的数据为字符串类型，则无法画出相对应的图表！elsx文件里的数据左上角会有小绿点
		workSheet.write_row('A'+str(index+2), dataLine)
		print("dataLine:",dataLine)
		
	#写入竖行数据，一竖
	# workSheet.write_column('A2', data[0])
	# workSheet.write_column('B2', data[1])
	# workSheet.write_column('C2', data[2])
	type = type
	endIndex = index + 2
	print("endIndex", endIndex)
	chart_col = chartType(type, workBook, endIndex)
	#插入图表
	workSheet.insert_chart('A'+str(endIndex), chart_col, {'x_offset': 25, 'y_offset': 30})
	workBook.close()


def chartType(type, workBook, endIndex):
	#xlsx文件添加一个图表，类型是折线图
	chart_col = workBook.add_chart({'type':type})
	chartAddSeries(chart_col, endIndex)

	#图表的标题，x轴的标题，y轴的标题
	chart_col.set_title({'name': 'The test site Bug Analysis'})
	chart_col.set_x_axis({'name': 'Test Num'})
	chart_col.set_y_axis({'name': 'Sample length(mm)'})
	#图表的格式
	chart_col.set_style(1)
	return chart_col

"""
添加不同图表的series
不同图表有不同图表series参数
"""
def chartAddSeries(chart_col, endIndex):
	#添加第一个折线图
	chart_col.add_series(
	{
		'name': '=SheetName!$B$1',
		'categories': '=SheetName!$A2:$A$'+str(endIndex),
		'values': '=SheetName!$B2:$B$'+str(endIndex),
		'line': {'color': 'red'},

	}	
	)
	# 第二个
	chart_col.add_series({
		'name': '=SheetName!$C$1',
		'categories': '=SheetName!$A$2:$A$'+str(endIndex),
		'values': '=SheetName!$C$2:$C$'+str(endIndex),
		'line': {'color': 'blue'},

		})	
	return chart_col




def xlsxFilesWrite(group):
	#group[1]代表着dict的数据
	#group[0]代表list文件名
	for a in range(len(group[1])):
		#表示每个xlsx文件名
		print("a", group[1][a])
		#表示每个xlsx文件里的数据
		print("b", group[0][a])
		#print(str(1)+'.xlsx')
		xlsxFileName = str(group[0][a])+'.xlsx'
		valueLists = group[1][a]
		print("========")
		print("valueLists:", valueLists)
		print("------------")
		xlsxChart(xlsxFileName, 'line' , headerLists, valueLists)

lists=[(1,2,3),(1,2,3),(1,2,3),(2,3,4),(2,3,4),(2,3,4),(2,3,4)]
headerLists = (('point'), ('opt1'), ('opt2'))
path="xxi.txt"
p2 = r"E:\python_code\numpy\xxi.txt"
resultPath = r"E:\python_code\numpy\resultPath"

#判断是否是当前目录

res = makeDir(resultPath)
print("res:", res)

isExistFilePath(p2)

group = groupLists(lists)
print("-------1233333333-----")
print(group)
print("-------1233333333-----")

fileWrite(headerLists, lists, path)
xlsxFilesWrite(group)


#print("-------------")
#print(group[1][0][0])

# print(groupLists())
# lists = getLists()
# print("lists:", lists)

# name = str(1111)
# varName = 'name'
# s = locals()[varName]
# print('s:', s)
def isExistFilePath(filePath):
	path = filePath.strip()
	path = path.rstrip("\\")
	isExist = os.path.exists(path)
	if(isExist):
		print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
		print("file has existed")
		#print("path:", path)
		return "aaaaaaaaaaaaaa"
	else:
		#print("file did not exists, ple reinput")
		path = input("file did not exists, ple reinput filePath:")
		print("path:", path)
		return isExistFilePath(path)			

p='a'

path1 = isExistFilePath(p)
print("path:", path1)