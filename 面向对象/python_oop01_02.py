class Animal(object):
    pass
class Cat(Animal):
    pass
if __name__ == '__main__':
    A= Animal()
    C = Cat()
    print('"A" IS Animal?', isinstance(A, Animal))
    print('"A" IS Cat?', isinstance(A, Cat))
    print('"C" IS Animal?', isinstance(C, Animal))
    print('"C" IS Cat?', isinstance(C, Cat))
