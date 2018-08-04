"""
1.新建xlsx文件
2.新建一个sheet
3.写入数据
4.添加图表，类型
5.添加图标的折线，数据
6.设置图表的标题，x，y轴的标题
7.插入图表
8.关闭xlsx文件
"""
import xlsxwriter
import getPointData
import os

"""
检查结果存放目录的的路径是否正确,
不填，回车都是当前目录
填了之后，有则用，没有则创建目录
"""
def isMakeDir(dirPath):
	path = dirPath.strip()
	path = path.rstrip("\\")

	isExist = os.path.exists(path)
	if(isExist):
		print("path has existed")
		return path
	else:
		if(path == None or path == ' ' or path == '' or path == '\n'):
			print("path::", path)
			return os.getcwd()
		else:
			try:
				print("path create successful")
				os.makedirs(path)
				return path
			except:
				print("mkdir failed！")
				input("ple reinput the path:")

"""
检查资源文件是否存在
存在则通过，不存在则继续迭代input，直到输入正确的资源文件
"""
def isExistFilePath(filePath):
	path = filePath.strip()
	path = path.rstrip("\\")
	isExist = os.path.exists(path)
	if(isExist):
		print("file has existed")
		#print("path:", path)
		return path
	else:
		#print("file did not exists, ple reinput")
		path = input("file did not exists, ple reinput filePath:")
		print("path:", path)
		return isExistFilePath(path)			

"""
保存txt格式
result.write(str(list), '\n')这种写法是错误的
result.writelines(str(list))这种是没法换行的,这种写法只是自动迭代，譬如列表，元组
"""
def fileWrite(headerLists, valueLists, newFilePath):
    with open(newFilePath, 'w') as result:
        result.write(str(headerLists) + '\n')
        for list in valueLists:
            result.write(str(list)+ '\n')
            #result.write(repr(list)+ '\n')
            #result.writelines(list)

"""
根据dict的key值相同，而value值不同，保存多个xlsx文件
"""
def xlsxFilesWrite(xlsxDir, type, headerLists, valueLists):
	#group[1]代表着dict的数据
	#group[0]代表list文件名
	group = getPointData.groupLists(valueLists)
	print("-------1233333333-----")
	print(group)
	print("-------1233333333-----")
	for a in range(len(group[1])):
		#表示每个xlsx文件名
		print("a", group[1][a])
		#表示每个xlsx文件里的数据
		print("b", group[0][a])
		#print(str(1)+'.xlsx')

		xlsxFileName = str(group[0][a])+'.xlsx'
		xlsxFilePath = os.path.join(xlsxDir, xlsxFileName)
		valueL = group[1][a]
		print("========")
		print("valueL:", valueL)
		print("------------")
		xlsxChart(xlsxFilePath, type , headerLists, valueL)


"""
新建xlsx文件，保存数据到excel
"""
def xlsxChart(fileName, type, headerLists, valueLists):
	#新建一个xlsx文件
	workBook = xlsxwriter.Workbook(fileName)
	#新建一个sheet,名字为SheetName
	workSheet = workBook.add_worksheet('SheetName')
	#设置Cell的width,设置格式一定要'B:D'之类的，不能没有':', 第二个参数为宽度
	workSheet.set_column('B:B', 30)
	#设置cell的height，第一行为0，以此为推， 参数1为行数， 参数2为高度
	workSheet.set_row(2, 60)
	#Style为粗体，非0为粗体
	bold = workBook.add_format({'bold': 1})
	#标题数据
	header = headerLists
	# 真实数据
	data = valueLists
	#写入横向数据，一行，'A1'表示位置
	workSheet.write_row('A1', header, bold )
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
	chart_col.set_legend({'delete_series': [2, 3]})
	#插入图表
	workSheet.insert_chart('A'+str(endIndex), chart_col, {'x_offset': 25, 'y_offset': 30})
	workBook.close()

"""
在excel表中插入图标的样式
"""
def chartType(type, workBook, endIndex):
	#xlsx文件添加一个图表，类型是折线图
	chart_col = workBook.add_chart({'type':type})
	chartAddSeries(chart_col, endIndex)

	#图表的标题，x轴的标题，y轴的标题
	chart_col.set_title({'name': 'The test site Bug Analysis'})
	chart_col.set_x_axis({'name': 'Test Num'})
	chart_col.set_y_axis({'name': 'Sample length(mm)'})
	chart_col.set_y2_axis({'name': 'aaaaaaaaaaaaaa'})
	#chart.set_y2_axis({'name': 'Laser wounds'})
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
		'name': '',
		'categories': '=SheetName!$A2:$A$'+str(endIndex),
		'values': '=SheetName!$B2:$B$'+str(endIndex),
		'line': {'color': 'red'},
		'y2_axis' : 1,

	}	
	)
	# 第二个折线图
	chart_col.add_series({
		'name': '',
		'categories': '=SheetName!$A$2:$A$'+str(endIndex),
		'values': '=SheetName!$C$2:$C$'+str(endIndex),
		'line': {'color': 'blue'},
		'y2_axis' : 1,


		})	

#------------------------------
	#添加第一个折线图
	chart_col.add_series(
	{
		'name': '=SheetName!$B$1',
		'categories': '=SheetName!$A2:$A$'+str(endIndex),
		'values': '=SheetName!$B2:$B$'+str(endIndex),
		'line': {'color': 'red'},

	}	
	)
	# 第二个折线图
	chart_col.add_series({
		'name': '=SheetName!$C$1',
		'categories': '=SheetName!$A$2:$A$'+str(endIndex),
		'values': '=SheetName!$C$2:$C$'+str(endIndex),
		'line': {'color': 'blue'},
		})	
	return chart_col



