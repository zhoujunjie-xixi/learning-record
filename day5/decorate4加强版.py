import time

def timer(func):
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("the func run time is %s" %(end_time - start_time))
    return deco

@timer
def test1():
    time.sleep(1)
    print("in the test1")


@timer
def test2(name):
    time.sleep(1)
    print(name)

test1()
test2("alex")
