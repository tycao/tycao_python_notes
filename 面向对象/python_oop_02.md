Python:类的继承，调用父类的属性和方法
---------
5个模块：
- （1）：直接调用父类属性方法
- （2）：重写父类属性方法
- （3）：强制调用父类私有属性方法
- （4）：调用父类的__init__方法
- （5）：继承父类初始化过程中的参数
### 一、直接调用父类属性方法
```python
class Father(object):
    def __init__(self, a):
        self.a = a
    def action(self):
        print('调用父类方法')
class Son(Father):
    pass

if '__name__' == '__main__':
    son = Son(1) # 子类Son继承父类Father的所有属性和方法
    son.action() # 调用父类方法
    son.a        # 调用父类属性
```
输出结果：
```python
调用父类方法
1
```
### 二、重写父类属性方法
**注意**：在上面的例子中，_**子类Son没有属性和action的方法**_，所以会从父类调用，那我们再来看看，子类Son有自身的属性和方法的结果是怎样的？

上述代码修改为：
```python
class Father(object):
    def __init__(self, a):
        self.a = a
    def action(self):
        print('调用父类方法')
class Son(Father):
    def __init__(self,a):
        super().__init__(a)
    def action(self):
        print("子类重新父类的方法")
if __name__ == '__main__':
    son = Son(1)
    son.action()
    print(son.a)
```
输出结果：
```python
子类重新父类的方法
1
```
这里，子类Son已经重写了父类Father的action的方法，并且子类Son也有初始化，因此，子类会调用自身的action方法和属性。总结：如果子类没有重写父类的方法，当调用该方法的时候，会调用父类的方法，当子类重写了父类的方法，默认是调用自身的方法。

另外，如果子类**Son**重写了父类**Father**的方法，如果想调用父类的action方法，可以利用**super()**
##### 如果重写父类方法后，调用父类的方法
```python
class Father(object):
    def action(self):
        print("调用父类的方法")
class Son(Father):
    def action(self):
        super(Son, self).action()
son = Son()
son.action()
```
输出结果：
```python
调用父类的方法
```
### 三、强制调用父类私有属性方法






- [x] [python 参考](https://blog.csdn.net/yilulvxing/article/details/85374142)