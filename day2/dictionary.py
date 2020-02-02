info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya"
}

print(info)
print(info["stu1101"])

info["stu1101"] = "武藤兰"
info["stu1104"] = "cangjinkong"
print(info)

del info["stu1101"]
print(info)

print("stu1104" in info)
print("stu1105" in info)