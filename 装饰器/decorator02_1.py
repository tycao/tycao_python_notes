class MyDecorator:
    def __init__(self, func):
        self.func = func
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)
        self.counter += 1
        print(f"Called {self.counter} times.")

@MyDecorator
def some_function():
    return 10

some_function()
some_function()
some_function()