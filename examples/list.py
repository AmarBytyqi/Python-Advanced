def get_user_data():
    people = {}
    count = 0
    while count < 5:
        try:
            name = input(f"Enter name #{count + 1}: ").strip()
            age_input = input(f"Enter age for {name}: ").strip()
            age = int(age_input)
            if age < 0:
                raise ValueError("Age cannot be negative.")
            people[name] = age
            count += 1
        except ValueError:
            print("Invalid input. Please enter a valid integer age.")
    return people

def print_adults(people_dict):
    print("\nPeople older than 18:")
    for name, age in people_dict.items():
        if age > 18:
            print(name)

def get_age_set(people_dict):
    return set(people_dict.values())

def average_age(people_dict):
    if not people_dict:
        return 0
    return sum(people_dict.values()) / len(people_dict)

# Main program
people = get_user_data()
print_adults(people)
ages_set = get_age_set(people)
print("\nUnique ages:", ages_set)
print("\nAverage age:", average_age(people))
