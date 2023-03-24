import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

# 要求1：用pandas读取sunspots文件,并随机抽取5行进行显示。
# df = pd.read_csv('sunspots.csv')
# print(df.sample(n=5))

# 要求3：创建以下两张表DataFrame，将两张表进行内连接，并输出。
# dict1={"key":["x","y","z"],
#        "lval":[1,2,3]}
# dict2={"key":["x","y"],
#        "lval":[4,5]}
# df1=DataFrame(dict1)
# df2=DataFrame(dict2)
#
# result = pd.merge(df1, df2, on="key", how="inner")
# print(result)

# 要求2：练习以下例子，查看结果
data1=pd.DataFrame(np.arange(6).reshape(2,3),columns=list("abc"))
data2=pd.DataFrame(np.arange(20,26).reshape(2,3),columns=list("ayz"))
data=pd.concat([data1,data2],axis=0)
print(data1)
print(data2)
print(data)

# 要求4：创建以下DataFrame，用combine_first方法进行合并，查看其结果。
# dict1 = {"A": [None, "A0", "A1", "A2"],
#          "B": [None, "B1", None, "B3"],
#          "Key": ["K0", "K1", "K2", "K3"]}
# dict2 = {"A": ["C0", "C1", "C2"],
#          "B": ["D0", "D1", "D2"]}
# df1 = DataFrame(dict1)
# df2 = DataFrame(dict2)
# result = df2.combine_first(df1)
# print(result)

# 要求5：练习以下例子，比较isnull.sum与info的区别。
# df = pd.DataFrame(np.arange(12).reshape(3, 4), columns=["A", "B", "C", "D"])
# df.iloc[2, :] = np.nan
# df[3] = np.nan
# print(df)
# print(df.isnull().sum())
# print(df.info())

# 要求6:创建以下有缺失值的dataframe，并用每一列的均值填充。
# dict = {
#     0: [-1.180338, -0.219780, -2.169303, 0.139349, 1.327619, 0.834232],
#     1: [-0.663622, -1.356420, None, None, None, None],
#     2: [0.952264, 0.742720, 1.129426, -1.463485, None, None]
# }
#
# df = DataFrame(dict)
# means = df.mean()
# df = df.fillna(means)
#
# print(df)

# 要求7：创建下表，k2,k3列重复时进行去重,并保留最后一个出现的记录。
# data = pd.DataFrame({"k1": ["one", "two"] * 3 + ["two"], "k2": [1, 1, 2, 3, 1, 4, 4], "k3": [1, 1, 5, 2, 1, 4, 4]})
# df = DataFrame(data)
# df = df.drop_duplicates(subset=["k2", "k3"], keep="last")
# print(df)

# 要求8：练习例子，查看结果。
# 1.利用散点图检测异常值。
# wdf=DataFrame(np.arange(20),columns=["W"])
# wdf["Y"]=wdf["W"]*1.5+2
# wdf.iloc[3,1]=128
# wdf.iloc[18,1]=150
# wdf.plot(kind="scatter",x="W",y="Y")
# plt.show()

# 2.利用箱线图分析异常值。
# wdf = DataFrame(np.arange(20), columns=["W"])
# wdf["Y"] = wdf["W"] * 1.5 + 2
# wdf.iloc[3, 1] = 128
# wdf.iloc[18, 1] = 150
# plt.boxplot(wdf["Y"].values, notch=True)
# plt.show()

# 要求9：使用replace替换数据值
# data = {"姓名": ['李红', '小明', '马芳', '国志'], "性别": ["0", "1", "0", "1"], "籍贯": ["北京", "甘肃", "", "上海"]}
# df = DataFrame(data)
# df = df.replace("", "不详")
# print(df)

# 要求10：练习例子：
# 要求11如下：
# （1）读取数据，并显示前5行数据。
# fdata=pd.read_excel('tips_mod.xls')
# print(fdata.head())

# （2）显示用餐时间time的不重复值。
# print(fdata['time'].unique())

# （3）从结果中发现有两个拼写错误”Diner”和’Dier’，修改拼写错误的字段值。
# fdata.loc[fdata['time']=='Diner','time']='Dinner'
# fdata.loc[fdata['time']=='Dier','time']='Dinner'
# print(fdata['time'].unique())

# （4）检测数据中的缺失值
# print(fdata.isnull().sum())

# （5）删除一行内有两个缺失值的数据。
# fdata.dropna(thresh=6,inplace=True)
# print(fdata.isnull().sum())

# （6）删除sex或time为空的行
# fdata.dropna(subset=['sex','time'],inplace=True)
# print(fdata.isnull().sum())

# （7）对剩余有空缺的数据用平均值替换。
# fdata.fillna(fdata.mean(numeric_only=True),inplace=True)
# print(fdata.isnull().sum())

