import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei']  # 指定默认字体为“文泉驿正黑”
plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题

color = sns.color_palette()
pd.set_option("precision", 3)

df = pd.read_csv("winequality-red.csv")
# print(df.head())
# print("数据的维度",df.shape)

# print(df.describe())

# print("quality的取值:",df["quality"].unique())
# print("quality的取值个数:",df["quality"].nunique())
# print(df.groupby("quality").mean())

color = sns.color_palette()
column = df.columns.tolist()
# fig = plt.figure(figsize=(10, 8))
# for i in range(12):
#     plt.subplot(4, 3,i+1)
#     df[column[i]].hist(bins=100,color=color[3])
#     plt.xlabel(column[i],fontsize=12)
#     plt.ylabel("Frequency",fontsize=12)
# plt.tight_layout()
# plt.show()

# fig=plt.figure(figsize=(10,8))
# for i in range(12):
#     plt.subplot(4,3,i+1)
#     sns.boxplot(df[column[i]],orient="v",width=0.5,color=color[4])
#     plt.ylabel(column[i],fontsize=12)
# plt.tight_layout()
# plt.show()

# acidtyfeat = [
#     "fixed acidity", "volatile acidity", "citric acid", "chlorides", "free sulfur dioxide", "total sulfur dioxide"
# ]
#
# fig=plt.figure(figsize=(10,6))
# for i in range(6):
#     plt.subplot(2,3,i+1)
#     v=np.log10(np.clip(df[acidtyfeat[i]].values,a_min=0.001,a_max=None))
#     plt.hist(v,bins=50,color=color[0])
#     plt.xlabel("log("+acidtyfeat[i]+")",fontsize=12)
#     plt.ylabel("Frequency")
# plt.tight_layout()
# plt.show()

# df["sweetness"]=pd.cut(df["residual sugar"],bins=[0,4,12,45],labels=["dry","semi-dry","semi-sweet"])
# print(df.head())

# ERROR
# plt.figure(figsize=(6,4))
# df["sweetness"].value_counts().plot(kind="bar",color=color[0])
# plt.xticks(rotation=0)
# plt.xlabel("sweetness")
# plt.ylabel("frequency")
# plt.tight_layout()
# plt.show()
#
# df["total acid"]=df["fixed acidity"]+df["volatile acidity"]+df["citric acid"]
# columns=df.columns.tolist()
# sns.set_style("ticks")
# sns.set_context("notebook",font_scale=1.1)
# column=columns[0:11]+["total acid"]
# plt.figure(figsize=(10,8))
# for i in range(12):
#     plt.subplot(4,3,i+1)
#     sns.boxplot(x="quality",y=column[i],data=df,color=color[1],width=0.6)
#     plt.ylabel(column[i],fontsize=12)
# plt.tight_layout()
# plt.show()

# sns.set_style("ticks")
# sns.set_context("notebook",font_scale=1.4)
# plt.figure(figsize=(6,4))
# sns.regplot(x="density",y="alcohol",data=df,scatter_kws={"s":10},color=color[1])
# plt.xlabel("density",fontsize=12)
# plt.ylabel("alcohol",fontsize=12)
# plt.xlim(0.989,1.005)
# plt.ylim(7,16)
# plt.show()

print(df.isnull().sum())


