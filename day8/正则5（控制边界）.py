import re

# ^ 匹配字符串开头
# 此方法在match时没啥用，因为match本身就是从头开始
res = re.match(r"^123","12345a")
print(res.group())

# $ 匹配字符串结尾
# res = re.match("\w+123$","abc123a") 错误
res = re.match(r"\w+123$","abc123")
print(res.group())

res = re.match(r"\d{9}$","123456789") #此方法控制一共9个数字
# res = re.match("\d{9}$","1234567890") # 共10个数字，不符，错误
print(res.group())

# \b 匹配一个单词的边界
res = re.match(r".+\d+\b","hahaha123")  #单词以数字结尾
#res = re.match(r"\d+\b","123a") 非以数字结尾，错误
print(res.group())
res = re.match(r"\s\d+\b"," 123")
print(res.group())

# \B 匹配非单词边界
res = re.match(r".+\Bab\B","c123abc")
print(res.group())
