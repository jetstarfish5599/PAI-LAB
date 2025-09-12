def employee(name, salary=10000):
    tax = 0.02 * salary
    salary_after_tax = salary - tax
    print(f"Employee Name: {name}")
    print(f"Salary after tax: {salary_after_tax}")

employee("masoom", 15000)
employee("Khan")
