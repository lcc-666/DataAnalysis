import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# df=pd.DataFrame({"key1":["a","a","b","b","a"],
#                  "key2":["yes","no","yes","yes","no"],
#                  "data1":np.random.randn(5),
#                  "data2":np.random.randn(5)})
# grouped=df["data1"].groupby(df["key1"])
# print(grouped.size())
# print(grouped.mean())

# 要求6：
# （1）读取testdata文件，利用agg函数统计数据中‘淋巴细胞计数’的和与均值、‘白细胞计数’的和与均值。
# （2）统计不同性别人群的血小板计数
# （3）同时输出淋巴细胞计数的均值、血小板计数的均值与标准差。

# df = pd.read_excel('testdata.xls')
#
# lymphocyte_count_sum = df['淋巴细胞计数'].sum()
# lymphocyte_count_mean = df['淋巴细胞计数'].mean()
# white_blood_cell_count_sum = df['白细胞计数'].sum()
# white_blood_cell_count_mean = df['白细胞计数'].mean()
#
# print(f"淋巴细胞计数的和为：{lymphocyte_count_sum}，均值为：{lymphocyte_count_mean}")
# print(f"白细胞计数的和为：{white_blood_cell_count_sum}，均值为：{white_blood_cell_count_mean}")
#
# platelet_count_by_gender = df.groupby('性别')['血小板计数'].mean()
# print("不同性别人群的血小板计数为：\n", platelet_count_by_gender)
#
# lymphocyte_count_mean = df['淋巴细胞计数'].mean()
# platelet_count_mean = df['血小板计数'].mean()
# platelet_count_std = df['血小板计数'].std()
#
# print(f"淋巴细胞计数的均值为：{lymphocyte_count_mean}")
# print(f"血小板计数的均值为：{platelet_count_mean}，标准差为：{platelet_count_std}")

# 要求7：利用series绘制线形图

# s = pd.Series(np.random.normal(size=10))
#
# plt.plot(s)
#
# plt.xlabel('Index')
# plt.ylabel('Value')
#
# plt.show()

# 要求8：利用dataframe绘制柱状图，查看其结果。

# stu = {"name":["xm","wf","zp","lh","lh"],
#        "sex":["male","female","female","female","male"],
#        "year":[1996,1997,1994,1999,1996]}
#
# df = pd.DataFrame(stu)
# df.plot(kind='bar', x='name', y='year')
# plt.show()

# 要求9：利用dataframe绘制散点图
# wd=pd.DataFrame(np.arange(10),columns=["A"])
# wd["B"]=2*wd["A"]+4
# wd.plot(kind='scatter', x='A', y='B')
# plt.show()


# 7.小费数据分析
# （1）读取数据，并查看数据的描述信息。
fdata=pd.read_excel("tips.xls")
# print(fdata.describe().head())

# （2）将列名修改为汉字，并显示前5行数据。
# fdata.rename(columns=({'total_bill':'消费总额','tip':'小费','sex':'性别','smoker':'是否抽烟',
#                        'day':'星期','time':'聚餐时间段','size':'人数'}),inplace=True)
# print(fdata.head())

# （3）分析男性顾客与女性顾客谁更慷慨。（将数据按照性别进行分组，查看分组后小费的情况）
# print(fdata.groupby('性别')['小费'].mean())

# （4）分析日期与小费之间的关系。（将数据按照星期分类，查看分类后的小费情况）
# print(fdata['星期'].unique())
# r=fdata.groupby('星期')['小费'].mean()
# fig=r.plot(kind='bar',x='星期',y='小费',fontsize=12,rot=36)
# plt.show()

# （5）性别+抽烟的组合因素对慷慨度的影响。（将数据按照性别和是否抽烟进行分组，查看分组后小费的情况）
# r=fdata.groupby(['性别','是否抽烟'])['小费'].mean()
# fig=r.plot(kind='bar',x=['性别','是否抽烟'],y='小费',fontsize=12,rot=30)
# fig.axes.title.set_size(16)
# plt.show()





# fdata.plot(kind='scatter',x='消费总额',y='小费')
#
# print(fdata.groupby('性别')['小费'].mean())
# print(fdata['星期'].unique())
# r=fdata.groupby('星期')['小费'].mean()
#
# fig=r.plot(kind='bar',x='星期',y='小费',fontsize=12,rot=36)
#
# r=fdata.groupby(['性别','是否抽烟'])['小费'].mean()
# fig=r.plot(kind='bar',x=['性别','是否抽烟'],y='小费',fontsize=12,rot=30)
# fig.axes.title.set_size(16)
# r=fdata.groupby('聚餐时间段')['小费'].mean()
# fig=r.plot(kind='bar',x='聚餐时间',y='小费')
# fig.axes.title.set_size(16)
