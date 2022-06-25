python装饰器入门
--------
**装饰器在python中的功能非常强大。** 但它的概念在刚开始接触的时候不太好理解。不好理解的地方主要是因为要想理解装饰器首先你必须理解python的**闭包概念**。要理解闭包，就得要知道在python中**一切都是对象**这个基础，有了这些铺垫，理解装饰器就水到渠成了，所以这篇我们先从基本的讲起。

首先说在python中**一切都是对象**，这个相信大家都早已听说，**所以一个函数也是一个对象**。我们定义的名称只是绑定到这些对象的标识符，**不同的名称可以绑定到同一个函数对象**，这么说可能也不好理解，我们来看一个例子：
```python
def fun1(msg):
   print(msg)
   
fun1("I'm body")
# output
I'm body

fun2 = fun1
fun2("I'm body")
# output
I'm body
```
这个例子就很明白看出，函数就是个对象，fun1,fun2是绑定到对象的标识符，所以fun2 = fun1后，fun2也指向了这个对象，所以运行fun2也得到相同的结果

我们接着说闭包，闭包简单说就是一个函数里面嵌套了一个函数，因为函数是对象，所以最外层函数可以返回内部函数对象，我们执行的时候是执行的这个返回对象的函数，来看个例子：
```python
def fun1():
   def fun2():
       print("Hello")
   return fun2

new = fun1()
new()
# Output
Hello
```
从上面例子可以看出，定义的fun1函数返回的是内部函数fun2，所以new这个指向对象fun2，所以运行完结果是Hello。

以上都是一些概念，主要是为装饰器做准备的，那么下面我们说一下装饰器的概念，有了上面的铺垫，装饰器都非常好理解了，为什么说它是python的语法糖，因为它就是个简单的形式变化，我们先写第一个装饰器：
```python
def make_decorate(func):
   def inner():
       print("我负责装饰")
       func()
   return inner

def fun1():
   print("我是普通函数")

>>> fun1()
我是普通函数

>>> pretty = make_decorate(fun1)
>>> pretty()
我负责装饰
我是普通函数
```
现在看这个例子是不是很好理解了，make_decorate运行完返回了内部函数inner，inner内部函数执行了print和运行了fun1函数，所以执行pretty的时候结果就先打印了print紧接着运行了fun1函数内容，然后完毕。

那用上面的代码，我们变个形式：
```python
def make_decorate(func):
   def inner():
       print("我负责装饰")
       func()
   return inner

@make_decorate
def fun1():
   print("我是普通函数")

>>> fun1()
我负责装饰
我是普通函数
```
看出这个跟上面的写法区别了吗，这也就回答了为什么说是语法糖，其实就是为了方便换了个写法，加了个@符在要装饰的函数上方，在这里例子中**fun1会被当做参数传递给make_decorate函数**，运行输出的结果是一样的。


