class Vehicle:
    def __init__(self, cap):
        self.cap = cap

    def fare(self):
        return self.cap * 100


class Bus(Vehicle):
    def fare(self):
        base_fare = super().fare()
        return base_fare + (0.1 * base_fare)


# Example
v = Vehicle(50)
print("Vehicle fare:", v.fare())

b = Bus(50)
print("Bus fare:", b.fare())
