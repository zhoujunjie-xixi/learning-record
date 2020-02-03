import copy
name1 = ["alex","xiaoming","xiaohua",["xiaohua","xiaojin"]]

name2 = name1
name3 = name1[:]
name4 = name1.copy()
name5 = copy.deepcopy(name1)
name1[2] = "小明"
name1[3][1] = "小华"

#正常的浅copy只copy一层，如果还有嵌套，copy的是地址，所以没有真正地copy第二层，需要使用深copy
print(name1)
print(name2)
print(name3)
print(name4)
print(name5)

