import time
from decorator02_2 import timer

@timer
class MyClass:
    def complex_calc(self):
        time.sleep(1)
        return 42

my_obj = MyClass()
print(my_obj.complex_calc())


def add_calc(target):
    def calc(self):
        return 42
    target.calc = calc
    return target

@add_calc
class My_Class:
    def __init__(self):
        print("MyClass __init__")

my_obj = My_Class()
print(my_obj.calc())