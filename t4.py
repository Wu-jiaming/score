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
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.rc('figure', figsize=(5, 3))#设置图片大小
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()
plt.figure();
ts.plot(style='k--', label='Series');
plt.legend()