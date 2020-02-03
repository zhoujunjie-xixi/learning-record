a = [i*2 for i in range(10000000)] # 列表生成式
print(a[9999])

b = ( i*2 for i in range(10000000)) # 简单生成器
# print(b[9999]) 此方法不可行，因为生成器只有在调用时才会生成，不能直接取值
print(b.__next__())
#　只记录当前位置，只有一个next的方法
print(next(b))  #两种next的方法