class Dog(object):

    def __init__(self, name):
        self.name = name

    @property
    def eat(self):
        print(" %s is eating" % self.name)


d = Dog("ChenRonghua")
d.eat  #变成一个（固有）属性，不能通过调用函数实现，而是直接使用
       #但是，区别在于，不调用函数意味着无法传参数了