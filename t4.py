import numpy as np

# a = np.array([[3, 4], [1, 9]])
# # print(a)
# #assert a is not None, 'n is zero!'
# print(a)
# b = np.array([[3, 4], [1, 9]])
# print("b1",b)
# b = b[:,1:]
# c = a-b
# print("a", a)
# print("b2", b)
# print(c)
#
# print("===================")
# a = np.floor(10 * np.random.random((3, 4)))
# print("a:", a)
# b= a
# print("b:", b[1:])
#
# print("....")
# #print(np.random.random(3))
# arr1 = np.array([[0, 0, 0],[1, 1, 1],[2, 2, 2], [3, 3, 3]])  #arr1.shape = (4,3)
# arr2 = np.array([1, 2, 3]) #arr2.shape = (3,)
# arr3 = np.array([[1], [2], [3]]) #arr2.shape = (3,1)
# arr4 = np.array([[1, 2, 3]]) #arr2.shape = (1,3)
# print("4:" , arr4.shape)
# print(arr1.shape)
# print(arr2)
# print(arr3)
# print(arr3.shape)
# print(arr2.shape)
# arr_sum = arr1 + arr4
# print(arr_sum)
#
# print("-=-=-=-=-=-")
# arr1 = np.array([[0, 0, 0],[1, 1, 1],[2, 2, 2], [3, 3, 3]])  #arr1.shape = (4,3)
# arr2 = np.array([[1],[2],[3],[4], [5]])    #arr2.shape = (4, 1)
#
#
#
#
# a =np.array( [ [1,2,3] , [3,2,1] ] )
#
# b= np.array( [ [2] , [3] ] )
# print(a+b)

# a = np.arange(5)
# print(a)
# a[[0,0,2]] += 1
# print(a)
# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd
# plt.rc('figure', figsize=(5, 3))#设置图片大小
# ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
# ts = ts.cumsum()
# ts.plot()
# plt.show()
# plt.figure();
# ts.plot(style='k--', label='Series');
# plt.legend()
import random
year = 2018
month = 8
day = 1
hour = 14
minute = 55
second = 10
dates = []
for i in range(1000):
    second = second + 10
    minute = minute + 30
    if(second >= 60):
        second = 0
        minute = minute + 1
    if(minute >= 60):
        minute = 1
        hour = hour + 1
    if(hour >= 24):
        hour = 1
        day = day + 1
    if(day > 30):
        day = 1
        month = month + 1
    if(month > 12):
        month = 1
        year = year + 1
    #日期
    date = str(year) + '-' + str(month) + '-' + str(day) + ' ' + str(hour) + ':' + str(minute) + ':' + str(second)
    dates.append(date)

#point值
point = 1
points = []
for i in range(len(dates)):
    #print("i:", i)
    points.append(dates[i] + " point:" +  str(point))
    point = float(point) + 0.1
    if(str(point).split(',') != None):
        point = str(point).split(',')[0]
        #print("point:", point)

#opt
logs =[]
for i in range(len(points)):
    opt1 = random.randint(69, 99)
    opt2 = random.randint(49, 89)
    logs.append(points[i] + ' opt1:' + str(opt1) + ' opt2:' + str(opt2))

with open('source2.txt','w', encoding='utf-8') as f:
    #for i in range(len(logs)):

    f.writelines(line + '\n' for line in logs)
#print("logs：", logs)