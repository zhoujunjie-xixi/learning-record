import json

f = open("test.txt","r")

dir = json.load(f)
print(dir)

f.close()
