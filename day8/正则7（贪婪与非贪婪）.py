import re

s = "This is a number: 111-222-333"

res = re.match(r"(.+)(\d+-\d+-\d+)",s)
print(res.groups())
# 结果：('This is a number: 11', '1-222-333')
# 即是：在满足后面判定可行情况下前面尽可能多拿
# 此处即是后面\d最少需要1个，所以只留了一个


#取消贪婪，加？,则变为尽可能少拿
res = re.match(r"(.+?)(\d+-\d+-\d+)",s)
print(res.groups())

s1 = "aa233bb"
res = re.match(r"aa(\d+)",s1)  #贪婪，尽可能多取
print(res.groups())

res = re.match(r"aa(\d+?)",s1) #非贪婪，尽可能少取
print(res.groups())

res = re.match(r"aa(\d+)bb",s1)
print(res.groups())

res = re.match(r"aa(\d+?)bb",s1)  #尽管此情况下已经取消贪婪，但是要满足后面的匹配
print(res.groups())
