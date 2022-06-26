class Animal(object): #python3中所有类都可以继承于object基类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call(self):
        print(f'{self.name}今年{self.age}了')

# 现在我们需要定义一个Cat 猫类继承于Animal，猫类比动物类多一个sex属性。
class Cat(Animal):
    def __init__(self, name, age, sex):
        super(Cat, self).__init__(name, age)
        self.sex = sex

if __name__ == '__main__':
    c = Cat('喵喵', 2, '男')
    c.call()