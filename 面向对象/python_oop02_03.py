class Father(object):
    def action(self):
        print("调用父类的方法")
class Son(Father):
    def action(self):
        super(Son, self).action()
if __name__ == '__main__':
    son = Son()
    son.action()