import re

# | 管道符表示匹配其左右任意一个即可
res = re.match(r"12|ab","ab")
print(res.group())

# 判断一个数是否是在0~100
res = re.match(r"[1-9]\d$|0$|100$","100")
print(res.group())
res = re.match(r"[1-9]?\d$|100$","0") #对0的情况进行了合并
print(res.group())

# () 将()中字符作为一个分组
res = re.match(r"<.+>(.*)<.+>","<h1>匹配分组<h2>")
print(res.group())  #显示全部结果
print(res.group(1))  # 取()里的内容

res = re.match(r"(<.+>).*(<.+>)","<h1>匹配分组<h2>")
print(res.group())
print(res.group(1))
print(res.group(2))
print(res.groups())  #显示所有分组的结果并且放到元组中

# 下面\1相当于调用前面分组生成的元组的元素1
# \2相当于调用元组中元素2
res = re.match(r"<(.*)><(.*)>.+</\2></\1>","<html><ht1>haha</ht1></html>") #此规则可表示左右对称
print(res.group())
print(res.groups())

# 对上例采用起名字的方法
# 作用：分组过多时避免混淆
# (?P<>)   对分组起别名
# (?P=name)  引用别名为name的分组
# 注意下面的?P<>的内容不再正则判定内，他是单独的起名字用的
s = "<html><ht1>haha</ht1></html>"
res = re.match(r"<(?P<a>.*)><(?P<b>.*)>.+</(?P=b)></(?P=a)>",s)
print("起名：")
print(res.group())
print(res.groups())