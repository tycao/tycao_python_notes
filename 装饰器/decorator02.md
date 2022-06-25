理解 Python 中的装饰器高级篇
--------
## 类装饰器
到上篇最后为止，我们只是查看了函数的装饰器，但是，装饰器也可以装饰类.

让我们从上面的示例中获取计时器装饰器。像这样用这个装饰器包装一个类是非常好的：
```python
import time
from decorator02_2 import timer

@timer
class MyClass:
    def complex_calculation(self):
        time.sleep(1)
        return 42

my_obj = MyClass()
my_obj.complex_calculation()
# result
# Finished 'MyClass' in 0.0000 secs
```
上面例子中我们的 `complex_calculation` 方法显然没有打印时间。请记住，`@` 符号与编写 `MyClass = timer(MyClass)` 的等价物，即装饰器只有在“调用”class时才会被调用。调用一个类意味着实例化它，所以定时器只在 **my_obj = MyClass()** 行执行。

装饰类时不会自动装饰类方法。简单来说，使用普通装饰器来装饰普通类只装饰其构造函数（__init__ 方法）。

但是，可以通过使用另一种形式的构造函数来更改整个类的行为。然而，让我们首先看看装饰器是否可以反过来工作，即我们是否可以用一个类来装饰一个函数。事实证明我们可以:
```python
class MyDecorator:
    def __init__(self, function):
        self.function = function
        self.counter = 0
    
    def __call__(self, *args, **kwargs):
        self.function(*args, **kwargs)
        self.counter+=1
        print(f"Called {self.counter} times")


@MyDecorator
def some_function():
    return 42


some_function()
some_function()
some_function()
# output
Called 1 times
Called 2 times
Called 3 times
```
这段代码工作方式如下：
- __init__ 在装饰 some_function 时被调用，装饰器方式跟这样调用一样：some_function = MyDecorator(some_function)。
- __call__ 在使用类的实例时调用，例如调用函数。由于 some_function 现在是 MyDecorator 的一个实例，但我们仍想将其用作函数，DoubleUnderscore 魔术方法 __call__ 负责此操作。

另一方面，在 Python 中装饰一个类是通过从外部（即，从装饰器）更改类来实现的。
考虑一下：
```python

def add_calc(target):

    def calc(self):
        return 42

    target.calc = calc
    return target

@add_calc
class MyClass:
    def __init__():
        print("MyClass __init__")

my_obj = MyClass()
print(my_obj.calc())
# output
MyClass __init__
42
```
同样，如果我们回顾一下装饰器的定义，这里发生的一切都遵循相同的逻辑：
- my_obj = MyClass() 首先调用装饰器
- add_calc 装饰器将 calc 方法修补到类
- 最终，通过使用构造函数实例化该类。

你可以使用装饰器以继承的方式更改类。这是否是一个不错的选择，这很大程度上取决于整个 Python 项目的体系结构。标准库的数据类装饰器是选择装饰器而不是继承的明智用法的一个很好的例子。

### 使用装饰器
#### Python 标准库中的装饰器
在接下来的部分中，我们将了解一些已经包含在标准库中的最流行和最有用的装饰器。

#### property



