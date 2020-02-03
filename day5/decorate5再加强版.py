import time

def out_wagger(tag):
    def wagger(func):
        def deco(*args, **kwargs):
            if tag == "tag1":
                stat_time = time.time()
                func(*args, **kwargs)
                end_time = time.time()
                print("the func run time is %s" %(end_time-stat_time))
            elif tag == "tag2":
                print("skip the step")
        return deco
    return wagger

@out_wagger("tag1")   #test1() = out_wagger(tag)(test1) = wagger(test1) = deco
def test1(argu1):
    print("in the "+argu1)

@out_wagger("tag2")
def test2(argu2):
    print("in the "+argu2)

test1("test1")
test2("test2")
