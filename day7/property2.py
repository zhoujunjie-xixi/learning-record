class Dog(object):

    def __init__(self, name):
        self.name = name
        self.__food = None

    @property
    def eat(self):
        print(" %s is eating %s" % (self.name,self.__food))

    @eat.setter
    def eat(self,food):
        print(" %s is eating %s" % (self.name,food))

    @eat.deleter
    def eat(self):
        del self.__food
        print("hahaha")

d = Dog("Dom")
d.eat
# d.eat("baozi") 此方法仍然不能使用
d.eat = "baozi"   #解决函数赋值的需求，给属性赋值  @eat.setter
d.eat

del d.eat   #运行@eat.deleter的函数