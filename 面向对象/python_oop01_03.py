class Animal(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def call(self):
        print(self.name, '会叫')

class Cat(Animal):
    def __init__(self, name, age, sex):
        super(Cat, self).__init__(name, age)
        self.sex = sex
    def call(self):
        print(self.name, '会“喵喵”叫')

class Dog(Animal):
    def __init__(self, name, age, sex):
        super(Dog, self).__init__(name, age)
        self.sex = sex
    def call(self):
        print(self.name, '会“汪汪”叫')
# 我们定义一个 do 函数，接收一个变量 ‘all’,如下：
def do(all):
    all.call()
if __name__ == '__main__':
    A = Animal('小黑',4)
    C = Cat('喵喵', 2, '男')
    D = Dog('旺财', 5, '女')

    for x in (A,C,D):
       do(x)