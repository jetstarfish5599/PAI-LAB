  #base class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
# no bonus
    def calBonus(self):
        return 0 


class Manager(Employee):
    def calBonus(self):
        return self.salary * 0.20

    def hire(self):
        print(self.name, "is hiring someone.")


class Developer(Employee):
    def calBonus(self):
        return self.salary * 0.10

    def wCode(self):
        print(self.name, "is writing code.")


class SeniorManager(Manager):
    def calBonus(self):
        return self.salary * 0.30


#Example
m = Manager("Ali", 50000)
d = Developer("Sara", 40000)
s = SeniorManager("Khan", 80000)

print("Manager Bonus:", m.calBonus())
m.hire()

print("Developer Bonus:", d.calBonus())
d.wCode()

print("Senior Manager Bonus:", s.calBonus())
s.hire()
