# *args只接收位置参数，输出为元组形式
def test1(x, *args):
    print(x)
    print(args)


test1(1, 2, 3, 4, 5, 6)


# **kwargs只接收关键字参数，输出为字典形式
def test2(**kwargs):
    print(kwargs)


# test2() takes 0 positional arguments but 5 were given
# test2(1,2,3,4,5)
test2(name="bob", age=23)
