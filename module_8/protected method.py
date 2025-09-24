class MyClass:
    def __init__(self):
        self._protected_variable = "This is a protected variable"


    def _protected_method(self):
        print("This is a protected variable")

myclass = MyClass()
print(myclass._protected_variable)
myclass._protected_method()