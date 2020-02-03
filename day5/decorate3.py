import time

def timer(func):
    def deco():
        star_time = time.time()
        func()
        end_time = time.time()
        print("the func run time is %s" %(end_time - star_time))
    return deco

@timer   # test1 = timer(test1)
def test1():
    time.sleep(3)
    print("in the test1")

test1()  #相当于 test1=timer(test1) --> test1()