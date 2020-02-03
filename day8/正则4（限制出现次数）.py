import re

# 取满足*前面规则的字符（0~任意多）
# 只要满足就取，不满足终止，没有满足的也无所谓（相当于上面为0时）
res = re.match("\d*","123a34")
print(res.group())

res = re.match("\s*1","  123")
print(res.group())

# 取满足+前面规则的字符（1~任意多）
# 至少出现一次
res = re.match("\d+","123a34")
print(res.group())

# 取满足？前面规则的字符（0或1个）
res = re.match("\d?\w","1a23a34")
print(res.group())

# {m} 规定出现m次
# {m,} 规定至少出现m次
# {m,n} 规定出现次数在m~n内
res = re.match("\d{3}a","123a34")
print(res.group())

res = re.match("\d{1,}a","123a34")
print(res.group())

res = re.match("\d{1,4}a","123a34")
print(res.group())