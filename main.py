import excelPoint_xlsWriter as ew
import os
import numpy as np
def main():
	#源文件
	sourcePath = 'source.txt'
	#print("path:::", isExistFilePath(sourcePath))
	sourcePath = ew.isExistFilePath(sourcePath)

	print("sourcePath::", sourcePath)
	#获取的相对应的数据
	PointLists = ew.getPointData.get_point(sourcePath)

	#对获取的opt1，opt2的值进行比较，获取其差
	diff_lists = ew.getPointData.get_diff(PointLists)

	#xlsx文件的标题
	headerLists = np.array([('point'), ('opt1'), ('opt2'), ('diff_op1'), ('diff_opt2')])

	#输出结果文件的目录
	dirPath = r"E:\python_code\numpy\resultPath"
	dirPath = input("ple input the result path:")
	#dirPath = ew.isMakeDir(dirPath) + r'\\'
	
	#文本文件result.txt
	newFilePath = os.path.join(dirPath, 'result.txt')
	print("newFilePath:", newFilePath)
	
	#将数据写入新文件
	ew.fileWrite(headerLists, diff_lists, newFilePath)

	#xlsx文件
	#xlsxFileName = r'E:\python_code\slsx\numpychart.xlsx'

	#xlsx文件里头的图表类型
	chartType = "line"

	#写入xlsx文件
	#xlsxChart(xlsxFileName, chartType, headerLists, diff_lists)
	ew.xlsxFilesWrite(dirPath, chartType, headerLists, diff_lists)
	print(diff_lists)

if __name__ == '__main__':
	main()