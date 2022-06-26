Python类的继承
------
如下定义一个动物类**Animal**为基类，它基本两个实例属性**name和age**、一个方法**call**:
```python
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
```
**注意**：
- 一定要用 **super(Cat, self).__init__(name,age)** 去初始化父类，否则，继承自 Animal的 Cat子类将没有 name和age两个属性。
- 函数super(Cat, self)将返回当前类继承的父类，即 Animal，然后调用__init__()方法，注意self参数已在super()中传入，在__init__()中将隐式传递，不能再写出self。

### 一、Python对子类方法的重构
上面例子中 Animal 的子类 Cat 继承了父类的属性和方法，但是我们猫类 Cat 有自己的叫声 '喵喵' ，这时我们可以对父类的 Call() 方法进行重构。如下：
```python
class Cat(Animal):
    def __init__(self, name, age, sex):
        super(Cat, self).__init__(name, age)
        self.sex = sex
    def call(self):
        print(self.name,'会“喵喵”叫')

if __name__ == '__main__':
   c = Cat('喵喵', 2, '男')
   c.call()  # 输出：喵喵 会“喵喵”叫
```
**注意**：类方法的调用顺序，当我们在子类中重构父类的方法后，Cat子类的实例先会在自己的类 Cat 中查找该方法，当找不到该方法时才会去父类Animal中查找对应的方法。

### 二、Python中子类与父类的关系
```python
class Animal(object):
    pass
class Cat(Animal):
    pass
if __name__ == '__main__':
A= Animal()
C = Cat()
```
子类与父类的关系是 “is” 的关系，如上 Cat 继承于 Animal 类，我们可以说：
- “A”是 Animal 类的实例，但，“A”不是 Cat 类的实例。
- “C”是 Animal 类的实例，“C”也是 Cat 类的实例。

判断对象之间的关系，我们可以通过 isinstance (变量,类型) 来进行判断：
```python
print('"A" IS Animal?', isinstance(A, Animal))
print('"A" IS Cat?', isinstance(A, Cat))
print('"C" IS Animal?', isinstance(C, Animal))
print('"C" IS Cat?', isinstance(C, Cat))
```
输出结果：
```python
"A" IS Animal? True
"A" IS Cat? False
"C" IS Animal? True
"C" IS Cat? True
```
**拓展**：_isinstance()_ 判断变量类型

函数 isinstance() 不止可以用在我们自定义的类，也可以判断一个变量的类型，如判断数据类型是否为 int、str、list、dict 等。
```python
print(isinstance(100, int))
print(isinstance('100', int))
print(isinstance(100, str))
print(isinstance('100', str))
```
输出：
```python
True
False
False
True
```
### 三、python 中多态
类具有继承关系，并且子类类型可以向上转型看做父类类型，如果我们从 Animal 派生出 Cat和 Dog，并都写了一个 call() 方法，如下示例：
```python
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
```
输出结果：
```python
小黑 会叫
喵喵 会“喵喵”叫
旺财 会“汪汪”叫
```
### 四、小知识：多态
这种行为称为多态。也就是说，方法调用将作用在 **all** 的实际类型上。**C 是 Cat 类型，它实际上拥有自己的 call() 方法以及从 Animal 继承的 call 方法**，但调用 C .call() 总是先查找它自身的定义，如果没有定义，则顺着继承链向上查找，直到在某个父类中找到为止。

**传递给函数 do(all) 的参数 all 不一定是 Animal 或 Animal 的子类型。** **任何数据类型的实例都可以，只要它有一个 call() 的方法即可**。其他类不继承于 Animal，具备 call 方法也可以使用 do 函数。这就是动态语言，动态语言调用实例方法，不检查类型，只要方法存在，参数正确，就可以调用。

### 五、Python类继承 注意事项：
- 在继承中基类的构造方法（__init__()方法）不会被自动调用，它需要在其派生类的构造方法中亲自专门调用。
- 在调用基类的方法时，需要加上基类的类名前缀，且需要带上**self**参数变量。而在类中调用普通函数时并不需要带上**self**参数
- Python 总是首先查找对应类的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）
