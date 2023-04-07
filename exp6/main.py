import seaborn as sns
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']  # 指定默认字体为“文泉驿正黑”
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


# 要求1：练习以下例子，用Seaborn进行风格设置，查看其结果。
def sinplot(flip=2):
    x = np.linspace(0, 20, 50)
    for i in range(1, 5):
        plt.plot(x, np.cos(x + i * 0.8) * (9 - 2 * i) * flip)


# sinplot()
# plt.show()
# sns.set(style='darkgrid',font_scale=1.5)
# sinplot()
# plt.show()

# 要求2：在要求1的基础上进行主题设置。
# sinplot()
# sns.set_style("darkgrid", {"axes.facecolor": ".9"})
# plt.show()

# 要求3：在要求1的基础上移除绘图中顶部和右侧的轴线。
# sinplot()
# sns.despine()
# plt.show()

# 要求4：绘制iris数据集中Petal.Width的分布图。
# df_iris=pd.read_csv('iris.csv')
# sns.set(color_codes=True)
# sns.histplot(df_iris['Petal.Width'],kde=True)
# plt.show()

# 要求5：练习以下例子
# sns.set(palette="muted",color_codes=True)
# rs=np.random.RandomState(10)
# d=rs.normal(size=100)
# f,axes=plt.subplots(2,2,figsize=(7,7),sharex=True)
# sns.histplot(d,kde=False,color="b",ax=axes[0,0])
# sns.distplot(d,hist=False,rug=True,color="r",ax=axes[0,1])
# sns.distplot(d,hist=False,color="g",kde_kws={"fill":True},ax=axes[1,0])
# sns.histplot(d,color="m",ax=axes[1,1],kde=True)
# plt.show()

# 要求6：在iris数据集中，显示Petal.Width在Species上值的分布
# df_iris=pd.read_csv('iris.csv')
# sns.set(style="white",color_codes=True)
# sns.stripplot(x=df_iris["Species"],y=df_iris["Petal.Width"],data=df_iris)
# sns.despine()
# plt.show()

# 要求7：练习以下例子，分析其结果。
# df_iris=pd.read_csv('iris.csv')
# sns.boxplot(x=df_iris['Species'],y = df_iris['Petal.Width'])
# plt.show()

# 要求8
# 二选一
# titanic = sns.load_dataset('titanic')
# titanic =pd.read_csv("titanic.csv")
# 1）查看有无缺失值。
# print(titanic.isnull().sum())

# 2）用年龄的均值进行缺失值的填充。
# mean =titanic['age'] .mean()
# titanic['age'] = titanic['age'].fillna(mean)
# print(titanic.isnull().sum())

# 3）利用Seaborn绘制年龄的直方图和密度图。
# 直方图
# df = titanic
# df.dropna(subset=['age'], inplace=True)
# plt.hist(df["age"],bins = 20,label = '直方图' )
# plt.legend()
# plt.show()

# 密度图
# sns.scatterplot(x='age', y='fare', data=titanic)
# plt.title('Age vs. Fare')
# plt.show()


# 4）显示登船地点（S,C,Q）的人数。
# print(titanic['embarked'].value_counts())

# 5）用柱状图可视化乘客的性别分布。
# sns.countplot(x="sex",data=titanic)
# plt.show()

# 6）基于性别，绘制乘客年龄分布箱线图。
# sns.boxplot(x="sex", y="age",data=titanic)
# plt.show()

# 7）对年龄进行分级，分开老人和小孩的数据。
# def agelevel(age):
#     if age<=16:
#         return 'child'
#     elif age>=60:
#         return 'old'
#     else:
#         return 'middle'
# titanic['age_level']=titanic['age'].map(agelevel)
# print(titanic.head())
