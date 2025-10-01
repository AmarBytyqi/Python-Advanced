class Student:
    def __init__(self,name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

student1 = Student("BlerdonIriqi", 67)

print("Name: ", student1.get_name())
student1.set_name("Zotri Ibriqi")
print("Updated Name: ", student1.get_name())

print("Age: ", student1.get_age())
student1.set_age(69)
print("Updated Age: ", student1.get_age())