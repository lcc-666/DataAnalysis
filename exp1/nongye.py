# 扩展：1.读取toutiao_cat_data.txt文本，提取文本中与农业相关的新闻并保存在agriculture.txt。
f = open("toutiao_cat_data.txt", "r")
txt = f.readlines()
f.close()
f = open("agriculture.txt", "w")
for i in txt:
    if "农" in i:
        f.write(i)
        print(i.strip())
