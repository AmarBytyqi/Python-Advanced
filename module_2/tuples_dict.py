grades = {
    ("John", "Math"): 5,
    ("Alice", "Biology"): 4,
    ("Bob", "Physics"): 3,
    ("Enes", "Music"): 1,
    ("Jane", "English"): 4,
}
john_math = grades[("John", "Math")]
print("John's grade in math is ", john_math)

grades[("Bob", "Math")] = 3
print(grades)

keys = list(grades.keys())
student, subject = keys[0]
print(student, "'s grade in ", subject, " is ", john_math)




























