class Father(object):
    def __init__(self, a):
        self.a = a
    def action(self):
        print('调用父类方法')
class Son(Father):
    def __init__(self,a):
        super().__init__(a)

if __name__ == '__main__':
    son = Son(1)
    son.action()
    print(son.a)