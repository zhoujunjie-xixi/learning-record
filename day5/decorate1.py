import time

def bar():
    time.sleep(3)
    print("in the bar")

def test1(func):
    start_time = time.time()
    print(func)
    func()
    end_time = time.time()
    print("run time is %s" %(end_time - start_time))

test1(bar)
