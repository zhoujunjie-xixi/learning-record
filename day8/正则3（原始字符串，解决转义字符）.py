import re

s1 = "\nabc"
s2 = "\\nabc"
s3 = r"\nabc"  # r为raw的意思 原始字符串，不做转义处理

print(s1)
print(s2)
print(s3)

print("测试正则中：")
res = re.match("\na",s1)  # 此时正则判定规则里的\n被转义
print(res.group())

# res = re.match("\\na",s2)  不可行,规则里面的\被转义了
res = re.match("\\\\na",s2)  # 可行方法
print(res.group())

res = re.match(r"\\nabc",s2)  #此方法比上面的更加方便，所以以后用正则前面都加r，避免转义引起的麻烦
print(res.group())

res = re.match(r"\na",s1)  # 加上r就没有什么争议了
print(res.group())