import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']  # 指定默认字体为“文泉驿正黑”
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

# （1）查看数据类型、表结构，并统计各个字段空缺值的个数：
df = pd.read_excel("testdata.xls")
# print(df.head())

# print(df.info())

# print(df.dtypes)

# print(df.shape)

# print(df.isnull().sum())

df.dropna(axis=1, how='all',inplace= True)#将全部项都是nan的列删除
# print(df.head())
# 删除“身份证号”为空的数据，并查看结果。
df.dropna(how='any',subset=['身份证号'],inplace= True)
# print(df.isnull().sum())

df1 = df
# print(df.shape)

# 将“开始从事某工作年份”规范为4位数字年份，如“2018”，并将列明修改为“参加工作时间”。
df.开始从事某工作年份 = df.开始从事某工作年份.str[0:4]
df.rename(columns={"开始从事某工作年份": "参加工作时间"},inplace=True)
# print(df.head())

# print(df.isnull().sum())

# （2）增加“工龄”（体检年份-参加工作时间）和“年龄”（体检年份-出生年份）两列。
df1 = df.dropna(subset=['参加工作时间'],how='any')
# print(df1.isnull().sum())


# 删除“体检年份”缺失的数据：
df2 = df1.dropna(subset=['体检年份'],how='any')
# print(df2.isnull().sum())

# print(df2.shape)

# print(df2.dtypes)

data = df2.copy()
# print(data.dtypes)

#参加工作时间转换为int64类型
data.参加工作时间 = data.参加工作时间.astype('int64')
#首先将体检年份转换为str类型
data['体检年份'] = data.体检年份.astype('str')
#切片取前4位值之后再将体检年份转换为int64类型
data.体检年份 = data.体检年份.str[0:4].astype("int64")
#取身份证的第4位-第7位，并转换为int64类型
data["出生年份"] = data.身份证号.str[4:8].astype('int64')
# print(data.head())

# 增加“工龄”和“年龄”这两列。
data = data.eval('工龄 = 体检年份-参加工作时间')
data = data.eval("年龄= 体检年份- 出生年份")
# print(data.head())

data.参加工作时间 = data.参加工作时间.astype('int64')
data['体检年份'] = data.体检年份.astype('str')
data.体检年份 = data.体检年份.str[0:4].astype("int64")
data["出生年份"] = data.身份证号.str[4:8].astype('int64')
# print(data.head())

# 统计不同性别的白细胞计数均值，并画出柱状图。
mean = data.groupby("性别")["白细胞计数"].mean()
# print(mean)

group = data.groupby("性别")
mean = group["白细胞计数"].mean()
# print(mean)

mean.plot.bar()
plt.xticks(rotation=0)
plt.ylabel("白细胞均值")
# plt.show()

data['年龄段'] = pd.cut(data.年龄, bins=[0,30,40,50, 100])
count = data.groupby('年龄段')['白细胞计数'].mean()
# print(count)

# 绘制不同年龄段的白细胞计数均值图：
count.plot(kind = "bar")
plt.xticks(rotation=30)
plt.ylabel("白细胞计数均值")
# plt.show()