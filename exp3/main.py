import pandas as pd
import numpy as np

# 要求1：分别用列表和字典创建Series数据结构，查看其输出。
# obj=pd.Series([1,-2,3,-4])
# print(obj)
#
# sdata={"Ohio":35000,"Texas:":71000,"Oregon":16000,"Utah":5000}
# obj3=pd.Series(sdata)
# print(obj3)

# 要求2：创建一个DataFrame，指定列名与索引，并输出。
# data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
#         'age': [25, 30, 35, 40],
#         'city': ['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen']}
#
# df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'], columns=['name', 'age', 'city'])
#
# print(df)

# 要求3：创建以下DataFrame，并筛选满足z列大于10小于20，输出结果
# data={
#     "W":[None,4.0,None,12.0,None,20.0],
#     "X":[1,5,9,12,17,21],
#     "Y":[None,6.0,None,14.0,None,22.0],
#     "Z":[3,7,11,15,19,23]
# }
# df=pd.DataFrame(data,index=["A","B","C","D","E","F"],columns=data.keys())
#
# filtered_df = df[(df['Z'] > 10) & (df['Z'] < 20)]
#
# print(filtered_df)


# 将水果价格表中的"元"去掉
# data={"fruit":["apple","grape","banana"],
#       "price":["30元","43元","28元"]}
# df1=pd.DataFrame(data)
# print(df1)
# def f(x:str):
#     return x.split("元")[0]
# df1["price"]=df1["price"].map(f)
# print("修改后的数据表：\n",df1)

# apply函数的使用方法
# applymap函数的用法
# df2=pd.DataFrame(np.random.randn(3,3),columns=["a","b","c"],index=["app","win","mac"])
# print(df2)
# print(df2.apply(np.mean))

# print(df2)
# print(df2.applymap(lambda x:"%.3f"%x))

df=pd.DataFrame({"key1":["a","a","b","b","a"],
                 "key2":["yes","no","yes","yes","no"],
                 "data1":np.random.randn(5),
                 "data2":np.random.randn(5)})
grouped=df["data1"].groupby(df["key1"])
print(grouped.size())
print(grouped.mean())

# 要求6：
# （1）读取testdata文件，利用agg函数统计数据中‘淋巴细胞计数’的和与均值、‘白细胞计数’的和与均值。
# （2）统计不同性别人群的血小板计数
# （3）同时输出淋巴细胞计数的均值、血小板计数的均值与标准差。
