f=open("toutiao_cat_data.txt","r")
txt=f.readlines()
f.close()
f=open("agriculture.txt","w")
for i in txt:
    if "农" in i:
        f.write(i)
        print(i.strip())