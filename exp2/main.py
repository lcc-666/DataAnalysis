import numpy as np
import csv

# 1、创建数组对象
# (1)使用array函数创建数组对象：首先创建序列，然后利用array()转换
# arr=np.array([1,2,3])
# print(arr)

# 要求：创建一个元素为从10到49的ndarray对象D1；
# D1=np.array(list(range(10,50)))
# print(D1)

# (2)专门创建数组的函数（可参考下面示例）linspace、arange、logspace
# 要求1：创建一个范围在(0,1)之间的长度为12的等差数列；
# arr=np.linspace(0,1,12)
# print(arr)

# 要求2：创建数组a=np.arange(15)并从中提取5到10之间的所有数字；
# a=np.arange(15)
# print(a[6:10])

# 要求3：使用np.random.random创建一个10*10的ndarray对象，并打印出最大最小元素；
# arr=np.random.random([10,10])
# print(arr)
# print("最大值{}\n最小值{}".format(np.amax(arr),np.amin(arr)))

# 要求1：创建一个一维数组，利用reshape改变数组的维度为二维数组。
# arr1=np.arange(8)
# print(arr1)
# a=arr1.reshape(4,2)
# print(a)

# 要求2：创建一个数组，利用reshape改变数组的维度，其中reshape的一个维度设置为-1，查看数组重塑后的结果。
# arr1=np.arange(12)
# print("arr1",arr1)
# arr2=arr1.reshape(2,-1)
# print("arr2",arr2)

# 要求1：两个数组的横向合并（可使用上述任意函数）
# arr1=np.arange(6).reshape(3,2)
# arr2=arr1*2
# arr3=np.hstack((arr1,arr2))
# print(arr3)

# 要求2：两个数组的纵向合并（可使用上述任意函数）
# arr1=np.arange(6).reshape(3,2)
# arr2=arr1*2
# arr3=np.vstack((arr1,arr2))
# print(arr3)

# 要求3：将数组a = np.arange(10).reshape(2,-1)和数组b = np.repeat(1,10).reshape(2,-1)水平堆叠
# a = np.arange(10).reshape(2,-1)
# b = np.repeat(1,10).reshape(2,-1)
# result = np.hstack((a,b))
# print(result)


# 要求：创建一个数组，实现数组的横向分割与纵向分割，分别查看其结果。（可选择任意函数实现）
# arr=np.arange(16).reshape(4,4)
# print("横向分割为：\n",np.hsplit(arr,2))
# print("纵向分割为：\n",np.vsplit(arr,2))

# 要求1：实现多维数组的索引。
# arr=np.arange(12).reshape(3,4)
# print(arr)
# print(arr[0,1:3])
# print(arr[:,2])
# print(arr[:1,:1])

# 要求2：使用布尔值索引访问多维数组，查看索引结果。
# arr = np.arange(12).reshape(3, 4)
# print(arr)
# print(arr[(0,1),(1,3)])
# print(arr[1:2,(0,2,3)])
# mask=np.array([1,0,1],dtype=np.bool_)
# print(mask)
# print(arr[mask,1])

# 要求3：创建一个10*10的ndarray对象，且矩阵边界全为1，里面全为0；
# arr=np.ones((10,10))
# arr[1:-1,1:-1]=0
# print(arr)

# 要求：实现不同形状数组即数组a与数组b相加的运算，查看其结果，理解ufunc广播机制的原理。
# a = np.arange(0,60,10).reshape(-1,1)
# b = np.arange(0,5)
# result = a + b
# print(result)

# 要求1：使用sort函数进行排序，使用argsort函数排序，查看其结果，说明两者区别。
# arr = np.array([7, 9, 5, 2, 9, 4, 3, 1, 4, 3])
# print(arr)
# arr.sort()
# print(arr)
#
# arr = np.array([7, 9, 5, 2, 9, 4, 3, 1, 4, 3])
# print(arr)
# print(arr.argsort())

# 要求2：使用lexsort排序，查看其结果，理解lexsort排序的内涵。
# a = np.array([7, 2, 1, 4])
# b = np.array([5, 2, 6, 7])
# c = np.array([5, 2, 4, 6])
# d = np.lexsort((a, b, c))
# print(d)
# print(list(zip(a[d], b[d], c[d])))

# 7.鸢尾花数据分析
# iris_data = []
# with open("iris.csv") as csvfile:
#     # 使用csv.reader读取csvfile中的文件
#     csv_reader = csv.reader(csvfile)
#     # 读取第一行每一列的标题
#     birth_header = next(csv_reader)
#     # 将csv 文件中的数据保存到birth_data中
#     for row in csv_reader:
#         iris_data.append(row)
#
# iris_list = []
# for row in iris_data:
#     iris_list.append(tuple(row[1:]))
#
# datatype = np.dtype([("Sepal.Length", np.str_, 40), ("Sepal.Width", np.str_, 40),
#                      ("Petal.Length", np.str_, 40), ("Petal.Width", np.str_, 40), ("Species", np.str_, 40)])
# print(datatype)
#
# iris_data = np.array(iris_list, dtype=datatype)
# PetalLength = iris_data["Petal.Length"].astype(float)
# ls = [
#     np.sort(PetalLength),
#     np.unique(PetalLength),
#     np.sum(PetalLength),
#     np.mean(PetalLength),
#     np.std(PetalLength),
#     np.var(PetalLength),
#     np.min(PetalLength),
#     np.max(PetalLength)]
# for i in ls:
#     print(i)
