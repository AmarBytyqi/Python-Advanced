class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width
    def calculate_perimeter(self):
        return 2*(self.length + self.width)

rectangle1 = Rectangle(2, 5)

area = rectangle1.calculate_area()
perimeter = rectangle1.calculate_perimeter()

print(area)
print(perimeter)





class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, i am {self.name}, and i am {self.age} years old.")

person1 = Person('Amar', 14)
person2 = Person('Blerdon', 15)

person1.greet()
person2.greet()

class Student:
    school = "Digital School"
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student('Blerdon', 15, 'Python')
student2 = Student('Amar', 14, 'javascript')

print(student1.course)
print(student2.course)
