import json

try:
    #Take input
    data = {}
    n = int(input("Enter number of people: "))
    for i in range(n):
        name = input(f"Enter name of person {i+1}: ")
        age = int(input(f"Enter age of {name}: "))
        data[name] = age

    #json file
    with open("task5.json", "w") as f:
        json.dump(data, f)

    #Load json file
    with open("task5.json", "r") as f:
        loaded_data = json.load(f)

    #Find max age and check for dups
    max_age = -1
    for name in loaded_data:
        if loaded_data[name] > max_age:
            max_age = loaded_data[name]

    max_age_people = []
    for name in loaded_data:
        if loaded_data[name] == max_age:
            max_age_people.append(name)

    #Display
    print("\nPerson(s) having maximum age:")
    for person in max_age_people:
        print(person, "with age", max_age)

    if len(max_age_people) > 1:
        print("More than one person has the same maximum age.")
    else:
        print("No one else has the same age.")

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except ValueError:
    print("Error: Invalid input type.")
except Exception as e:
    print("An unexpected error occurred:", e)
