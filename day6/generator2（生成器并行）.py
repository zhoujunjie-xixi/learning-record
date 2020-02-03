# 对于普通的生成器，第一个next调用，相当于启动生成器
# 会从生成器函数的第一行代码开始执行
# 直到第一次执行完yield语句后，跳出生成器函数。
#
# 其实next()和send()在一定意义上作用是相似的
# 区别是send()可以传递yield表达式的值进去
# 而next()不能传递特定的值，只能传递None进去
# 因此，我们可以看做c.next() 和 c.send(None) 作用是一样的
# 需要提醒的是，第一次调用时，请使用next()语句或是send(None)

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)            # 转到yield处 并且为其赋值 i
        c2.send(i)

producer("alex")