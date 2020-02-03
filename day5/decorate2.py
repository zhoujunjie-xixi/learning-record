import time

def bar():
    time.sleep(3)
    print("in the bar")

def test(func):
    start_time = time.time()
    #func()
    end_time = time.time()
    return func

test2 = test(bar)
test2()
