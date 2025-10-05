try:
    #data from user
    name = input("Enter employee name: ")
    cnic = input("Enter employee CNIC number: ")
    age = input("Enter employee age: ")
    salary = input("Enter employee salary: ")

    #Write to file
    with open("task4.txt", "w") as f:
        f.write("Name: " + name + "\n")
        f.write("CNIC: " + cnic + "\n")
        f.write("Age: " + age + "\n")
        f.write("Salary: " + salary + "\n")

    # Append  number
    contact = input("Enter employee contact number: ")
    with open("task4.txt", "a") as f:
        f.write("Contact: " + contact + "\n")

    #display
    print("\nEmployee data:")
    with open("task4.txt", "r") as f:
        print(f.read())

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied to access file.")
except Exception as e:
    print("An unexpected error occurred:", e)
