age = 18

if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")

temp = 28

if temp > 30:
    print("It's a hot day, stay hydrated")
elif 20 <= temp <=30:
    print("The weather is pleasant")
else:
    print("It's a cold day")


gpa = 4.5
score = 75
if gpa >= 3.5:
    if 50 <= score <= 65:
        print(f"Student with GPA {gpa} and test score of {score} may be eligible for a partial scholarship")0
    elif score > 65:
        print(f"Student with GPA {gpa} and test score of {score} is eligible for a partial scholarship")
    else:
        print(f"Student with GPA {gpa} and test score of {score} is not eligible for a partial scholarship")
else:
    print(f"Student with GPA {gpa} and test score of {score} is not eligible for a partial scholarship")