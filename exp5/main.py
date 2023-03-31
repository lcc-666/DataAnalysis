import pandas as pd
import numpy as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']  # 指定默认字体为“文泉驿正黑”
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


# 1.要求：输入以下代码，查看结果
# plt.rcParams['figure.figsize']=(10,5)
# plt.rcParams['figure.dpi']=200
# y=[1,2,3,4]
# scale_ls=range(4)
# index_ls=["富强","民主","文明","和谐"]
# plt.xticks(scale_ls,index_ls,fontsize=20)
# plt.yticks([1,2,3,3.5,4],fontsize=20)
# plt.plot(y)
# plt.show()

# 2.要求：输入以下代码，查看结果
# fig,axes=plt.subplots()
#
# def f(t):
#     return np.cos(2*np.pi*t)
# x1=np.arange(0.0,4.0,0.5)
# x2=np.arange(0.0,4.0,0.01)
# plt.figure(1)
# plt.subplot(2,2,1)
# plt.plot(x1,f(x1),"bo",x2,f(x2),"k")
# plt.title("子图1")
# plt.subplot(2,2,2)
# plt.plot(np.cos(2*np.pi*x2),"r--")
# plt.title("子图2")
# plt.show()

# 3.要求：练习以下例子
# x=np.linspace(0,1,500)
# y=np.sin(3*np.pi*x)*np.exp(-4*x)
# fig,ax=plt.subplots()
# plt.plot(x,y)
# plt.fill_between(x[15:300],0,0.4,facecolor="green",alpha=0.3)
# plt.show()

# 4.要求：练习以下例子
# x=np.linspace(0,1,500)
# y1=np.sin(3*np.pi*x)*np.exp(-4*x)
# y2=y1+0.2
# plt.plot(x,y1,"b")
# plt.plot(x,y2,"r")
# plt.fill_between(x,y1,y2,facecolor="green",alpha=0.3)
# plt.show()

# 5.要求：绘制气温柱状图并标注温度，并在图中标注指出哪个城市最凉快，可用annotate()
# data=[25,30,32,34,34,23]
# label=['青海','兰州','北京','上海','广州','拉萨']
# plt.xticks(range(len(data)),label)
# plt.xlabel("城市")
# plt.ylabel("温度")
# plt.title("六城市8月份日均最高气温")
# plt.bar(range(len(data)),data)
# for x,y in zip(range(len(data)),data):
#     plt.text(x,y,y,ha="center",va="bottom")
# plt.show()

# 6.要求：练习series和dataframe的折线图，
# s=pd.Series(np.random.randn(10).cumsum(),index=np.arange(0,100,10))
# s.plot()
# plt.show()
#
# s=pd.DataFrame(np.random.randn(10,4).cumsum(0),columns=["A","B","C","D"],index=np.arange(0,100,10))
# s.plot()
# plt.show()

# 7.要求：利用plot函数绘制下列图形。
# x=np.arange(9)
# y=np.sin(x)
# z=np.cos(x)
# plt.plot(x,y,marker="*",linewidth=1,linestyle="--",color="orange")
# plt.plot(x,z)
# plt.title("matplotlib")
# plt.xlabel("height",fontsize=15)
# plt.legend(["Y","Z"],loc="upper right")
# plt.grid(True)
# plt.show()



# 8.要求：练习以下例子
# fig,ax=plt.subplots()
# x1=np.arange(1,30)
# y1=np.sin(x1)
# ax1=plt.subplot(1,1,1)
# plt.title("散点图")
# plt.xlabel("X")
# plt.ylabel("Y")
# lvalue=x1
# ax1.scatter(x1,y1,c="r",s=100,linewidths=lvalue,marker="o")
# plt.legend("x1")
# plt.show()


# 9.要求：练习并查看结果
# df=pd.DataFrame(np.random.rand(6,4),index=["one","two","three","four","five","six"],columns=pd.Index(["A","B","C","D"],name="Genus"))
# df.plot.bar()
# plt.show()


# 10.要求：练习并查看结果
# fig,axes=plt.subplots(2,1)
# data=pd.Series(np.random.randn(16),index=list("abcdefghijklmnop"))
# data.plot.bar(ax=axes[0],color="k",alpha=0.7)
# data.plot.barh(ax=axes[1],color="k",alpha=0.7)
# plt.show()

# fig,ax =plt.subplots()
# x=np.arange(1,6)
# Y1=np.random.uniform(1.5,1.0,5)
# Y2=np.random.uniform(1.5,1.0,5)
# plt.bar(x,Y1,width=0.35,facecolor="lightskyblue",edgecolor="white")
# plt.bar(x+0.35,Y2,width=0.35,facecolor="yellowgreen",edgecolor="white")
# plt.show()





# 11.要求：绘制下列饼图。
# date={
#     "python":25.2,
#     "java:":23.6,
#     "HTML":15.5,
#     "SQL":15.3,
#     "C谣言":20.3
# }
# ex=[0.05, 0.3, 0.05, 0.05,0.05]
# plt.pie(date.values(),explode=ex,labels=date.keys(),autopct='%1.1f%%')
# plt.show()

# 12.要求：练习例子，分析结果
# np.random.seed(2)
# df=pd.DataFrame(np.random.rand(5,4))
# columns=["A","B","C","D"]
# df.boxplot()
# plt.show()




# 13.星巴克数据分析
starbucks = pd.read_csv("directory.csv")
# （1）查看星巴克旗下有哪些品牌。如果我们只关心星巴克咖啡门店，则只需获取星巴克中Brand的数据集，并查看全世界一共有多少家星巴克门店。。
# print("星巴克旗下品牌有：\n",starbucks.Brand.value_counts())

# （2）查看全世界一共有多少个国家和地区开设了星巴克门店，显示门店数量排名前10和后10的国家和地区。
df = starbucks.groupby(["Country"]).size()
df1 = df.sort_values(ascending=False)
# print("全世界一共多少个国家开设了星巴克门店:",df.size)
# print("排名前10的国家：\n",df1.head(10))
# print("排名后10的国家：\n",df1.tail(10))

# （3）显示拥有星巴克门店数量排名前10的城市。
# df1.head(10).plot(kind='bar',rot=0)
# plt.title('星巴克门店数排名前10的国家')
# plt.ylabel('Store Counts')
# plt.xlabel('Countries')
# plt.show()

# （4）星巴克门店数排名前10的国家
# df1.head(10).plot(kind='bar',rot=0)
# plt.title('星巴克门店数排名前10的国家')
# plt.ylabel('Store Counts')
# plt.xlabel('Countries')
# plt.show()


# （5）绘制星巴克门店数前10的城市分布柱状图。
# star = starbucks.dropna(how='any',subset=['City'])
# star.isnull().sum()
# plt.figure(1,figsize=(8,6))
# count_starbucks_city =star.City.value_counts()
# city_top10 = count_starbucks_city.head(10)
# city_top10.plot(kind='bar',rot=30)
# plt.title('拥有星巴克门店最多的10个城市')
# plt.ylabel('Store Counts')
# plt.xlabel('Cities')
# plt.show()

# （6）按照星巴克门店在中国的分布情况，统计排名前10的城市。
# import pinyin
# star = starbucks.dropna(how='any',subset=['City'])
# star.isnull().sum()
# df = star[star["Country"]=="CN"]
#
# df1 = df.copy()
# df1["City"] = df1["City"].apply(lambda x:x.lower())
#
# df1["City"] = df1["City"].apply(lambda x:pinyin.get(x, format="strip", delimiter="")[0:-3])

# df1 = df1.groupby(["City"]).size().sort_values(ascending=False)
# df1.head(10)
# plt.figure(1,figsize=(8,6))
# df1.head(10).plot(kind='bar',rot=30)
# plt.title('中国拥有星巴克门店最多的10个城市')
# plt.ylabel('Store Counts')
# plt.xlabel('Cities')
# plt.show()


# （7）用饼状图显示星巴克门店的经营方式有哪几种？
# plt.figure(1,figsize=(8,6))
# ownership = star['Ownership Type'].value_counts()
# plt.title('星巴克门店所有权类型')
# ownership.plot(kind='pie')
# plt.show()


