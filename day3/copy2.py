name1 = ["alex","xiaoming","xiaohua",["xiaohua","xiaojin"]]

name2 = name1
name3 = name1[:]
name4 = name1.copy()
name1[2] = "小明"
name1[3][1] = "小华"

print(name1)
print(name2)
print(name3)
print(name4)

