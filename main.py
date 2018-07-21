import excelPoint_xlsWriter as ew

def main():
	#源文件
	sourcePath = 'source.txt'
	#print("path:::", isExistFilePath(sourcePath))
	sourcePath = ew.isExistFilePath(sourcePath)

	print("sourcePath::", sourcePath)
	#获取的相对应的数据
	PointLists = ew.getPointData.get_point(sourcePath)

	#对获取的数据进行排序，必须为数字类型
	valueLists = ew.getPointData.listSort(PointLists)

	#xlsx文件的标题
	headerLists = (('point'), ('opt1'), ('opt2'))

	#输出结果文件的目录
	dirPath = r"E:\python_code\numpy\resultPath"
	dirPath = input("ple input the result path:")
	dirPath = ew.isMakeDir(dirPath) + r'\\'
	
	#文本文件result.txt
	newFilePath = dirPath + r'result.txt'
	print("newFilePath:", newFilePath)
	
	#将数据写入新文件
	ew.fileWrite(headerLists, valueLists, newFilePath)

	#xlsx文件
	#xlsxFileName = r'E:\python_code\slsx\numpychart.xlsx'

	#xlsx文件里头的图表类型
	chartType = "line"

	#写入xlsx文件
	#xlsxChart(xlsxFileName, chartType, headerLists, valueLists)
	ew.xlsxFilesWrite(dirPath, chartType, headerLists, valueLists)
	print(valueLists)

if __name__ == '__main__':
	main()