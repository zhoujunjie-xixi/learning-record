def fibo(max):
    n,a,b = 0,0,1
    while n<max:
        #print(b)
        yield b  #相当于return b 并且记录此中断位置，下一步继续从此开始
        a,b = b,a+b #等价于c=[b,a+b] a=c[0],b=c[1]
        n = n+1
    return "done"

fi = fibo(10)
print(next(fi))
print(next(fi))
print(next(fi))