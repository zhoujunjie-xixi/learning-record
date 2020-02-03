import re

# match 匹配从左到右依次进行 第一个不符合直接pass

# . 匹配任意1个字符（除\n）
res = re.match(".","happy")
print(res.group())

res = re.match("...","ha")  # 匹配至少三个(除\n)
# return None

# \d 匹配数字，即0~9
# \D 匹配非数字
res = re.match("\d\D","1abc") #注意区分 "\" 和 "/"
print(res.group())

# \s 匹配空白
# \S 匹配非空白
res = re.match("\s\s\s123","   123abc") # tab键 = 3个空白
print(res.group())

# \w 匹配单词字符 包括 0-9，a-z, A-Z
# \W 匹配非单词字符
res = re.match("\w\w\w","123abc")
print(res.group())
