class MyClass:
    def __init__(self):
        self.__private_variable = "This is a private variable"


    def __private_method(self):
        print("This is a private variable")

myclass = MyClass()
print(myclass._MyClass__private_variable)
myclass._MyClass__private_method()