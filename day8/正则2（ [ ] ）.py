import re

# []匹配[]中列举的字符，中间不加任何分隔符
res = re.match("12[123456]","123")
print(res.group())

res = re.match("12[1,23456]a","12,a")
print(res.group())

# 加一个 ^ 则代表除了列举的以外的
res = re.match("12[^123456]","12a")
print(res.group())

# 加一个 - 则代表范围
res = re.match("12[a-z]","12h")
print(res.group())