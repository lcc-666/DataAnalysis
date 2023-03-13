# （1）在列表中追加元素
list=['a','b','c','d']
list.append('Baidu')
print('更新后的列表：',list)

# （2）在列表中插入元素
list=['a','b','c','d']
list.insert(1,"Baidu")
print("更新后的列表:",list)

# （3）返回第一个指定值的索引
list=['a','b','c','d']
print("b索引值为",list.index("b"))


# （4）删除列表中第一次找到的数值
list=['a','b','c','d']
list.remove("d")
print("列表现在为：",list)

# # （5）列表元素倒排
# list=['a','b','c','d']
# p=list.pop()
# print("删除%r后的列表为%r"%(p,list))
# print("删除元素为：",list.pop(1))

# （5）列表元素倒排
list=['a','b','c','d']
list.reverse()
print(list)

# (6)返回列表中指定数组的出现次数
list=['a','b','c','d']
print("c的出现次数是：",list.count("c"))
print("list中一共有%d个a:"%list.count("a"))

# （7）输入一个包含若干数据的列表，先将列表中的数由小到大进行排序，然后将值为负数的元素进行平方运算。
listRe=[1,5,6,-5,-1]
listRe.sort()
print("排序后的列表",list)
listEnd=[x if x>0 else x**2 for x in listRe]
# (8)列表推导式
import random
total=[]
for i in range(30):
    total.append(random.randint(1,150))
print("列表:",total)
sum=0
for item in total:
    sum=sum+item
total_m=sum//len(total)
print("新列表：",[x-total_m for x in total])

# （1）元组创建
tup=tuple('bar')
print('输出元组tup:',tup)
nested_tup=(4,5,6),(7,8)
print('输出元组tup:',nested_tup)
print('元组的连接',tup+tuple('wwy'))
a,b,c=tup
print(a,b,c)
print(tup.count(a))

dt={'w':97,'a':19}
print(dt.get('w',None))

# 6.读取txt,csv文件

import csv
def skip_header(f):
    line =f.readline()
    while line.startswith('#'):
        line = f.readline()
    return line
def process_file(f):
    line =skip_header(f).strip()
    print(line)

    for line in f:
        if line.startswith("-") or line.startswith("#"):
              line=f.readline()
        line = line.strip()
        print (line)


if __name__ == "__main__":
    input_file = open("a.txt",'r',encoding="gbk")
    process_file(input_file)
    input_file.close()

# 7.葡萄酒探索
import csv

f=open("white_wine.csv","r")

reader=csv.reader(f)
content=[]
for row in reader:
    content.append(row)

f.close()

for i in range(5):
    print(content[i])

quality_list=[]
for row in content[1:]:
    quality_list.append(int(row[-1]))
quality_count=set(quality_list)
print("白葡萄酒共有%d种等级，分别是：%r"%(len(quality_count),quality_count))

content_dict = {}
for row in content[1:]:
    qulity = int(row[-1])
    if qulity not in content_dict.keys():
        content_dict[qulity] = [row]
    else:
        content_dict[qulity].append(row)

for key in content_dict:
    print(key, ":", len(content_dict[key]))

number_tuple = []
for key, value in content_dict.items():
    number_tuple.append((key, len(value)))
print(number_tuple)

mean_list = []
for key, value in content_dict.items():
    sum = 0
    for row in value:
        sum += float(row[0])
    mean_list.append((key, sum / len(value)))

for item in mean_list:
    print(item[0], ":", item[1])




