class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight  # in kilograms
        self.height = height  # in meters
        self.bmi = self.calculate_bmi()

    def calculate_bmi(self):
        try:
            return round(self.weight / (self.height ** 2), 2)
        except ZeroDivisionError:
            return 0

    def get_bmi_category(self):
        raise NotImplementedError("This method should be implemented by subclasses")

    def print_info(self):
        print(f"\n--- BMI Report for {self.name} ---")
        print(f"Age: {self.age}")
        print(f"Weight: {self.weight} kg")
        print(f"Height: {self.height} m")
        print(f"BMI: {self.bmi}")
        print(f"Category: {self.get_bmi_category()}")


class Adult(Person):
    def get_bmi_category(self):
        if self.bmi < 18.5:
            return "Underweight"
        elif 18.5 <= self.bmi < 25:
            return "Normal weight"
        elif 25 <= self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"


class Child(Person):
    def get_bmi_category(self):
        if self.bmi < 14:
            return "Underweight"
        elif 14 <= self.bmi < 18:
            return "Normal weight"
        elif 18 <= self.bmi < 20:
            return "Overweight"
        else:
            return "Obese"


def main():
    print("Welcome to the BMI Calculator App")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    if age >= 18:
        person = Adult(name, age, weight, height)
    else:
        person = Child(name, age, weight, height)

    person.print_info()


if __name__ == "__main__":
    main()
