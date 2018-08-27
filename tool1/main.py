import excelPoint_xlsWriter as ew
import os
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

	#获取的相对应的数据
	PointLists = ew.getPointData.get_point(sourcePath)

	#对获取的opt1，opt2的值进行比较，获取其差
	points_tuple = ew.getPointData.get_diff(PointLists)
	print("points_tuple:", points_tuple)
	#raise("points_tuple:", points_tuple)
	#全部points值
	points_lists = points_tuple[0]
	print("points_tuple[0]", points_lists)

	#异常points值
	abnormal_lists = points_tuple[1]
	print("points_tuple[1]", abnormal_lists)


	#xlsx文件的标题
	headerLists = (('point'), ('opt1'), ('opt2'), ('diff_op1'), ('diff_opt2'))

	#输出结果文件的目录
	dirPath = r"E:\python_code\numpy\resultPath"
	dirPath = input("ple input the result path:")
	#dirPath = ew.isMakeDir(dirPath) + r'\\'
	
	#文本文件result.txt
	newFilePath = os.path.join(dirPath, 'result.txt')
	print("newFilePath:", newFilePath)

	#异常值存放abnormal.txt
	abnormal_txt = os.path.join(dirPath, 'abnormal.txt')
	print("abnormal_txt:", abnormal_txt)

	#将异常数据写入新文件
	ew.fileWrite(headerLists, points_lists, newFilePath)
	ew.fileWrite(headerLists, abnormal_lists, abnormal_txt)

	#xlsx文件
	#xlsxFileName = r'E:\python_code\slsx\numpychart.xlsx'

	#xlsx文件里头的图表类型
	chartType = "line"

	#写入xlsx文件
	#xlsxChart(xlsxFileName, chartType, headerLists, diff_lists)
	ew.xlsxFilesWrite(dirPath, chartType, headerLists, points_lists, True)
	ew.xlsxFilesWrite(dirPath, chartType, headerLists, abnormal_lists ,False)
	print(points_lists)

if __name__ == '__main__':
	main()