from datetime import date

#Vehicle Base Class
class Vehicle:
    def __init__(self, make, model, rental_price):
        self.make = make
        self.model = model
 # encapsulated
        self.__rental_price = rental_price  
        self.available = True

    def check_availability(self):
        return self.available

    def rent(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_vehicle(self):
        self.available = True

    def calculate_rental_cost(self, days):
        return self.__rental_price * days

    def display_details(self):
        print(f"{self.__class__.__name__}: {self.make} {self.model}")
        print(f"Rental Price (per day): {self.__rental_price}")
        print(f"Availability: {'Available' if self.available else 'Rented'}")


#Vehicle Subclasses
class Car(Vehicle):
    pass


class SUV(Vehicle):
    pass


class Truck(Vehicle):
    pass


#Customer Class
class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.__contact = contact   
# encapsulated
        self.rental_history = []

    def add_rental(self, reservation):
        self.rental_history.append(reservation)

    def display_history(self):
        print(f"Rental History for {self.name}:")
        for res in self.rental_history:
            res.display_details()

    def display_contact(self):
        print(f"Customer: {self.name}, Contact: {self.__contact}")

#Rental Reservation Class
class RentalReservation:
    def __init__(self, customer, vehicle, start_date, end_date):
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date
        if self.vehicle.rent():
            customer.add_rental(self)
        else:
            print("Vehicle is not available!")

    def calculate_total_cost(self):
        days = (self.end_date - self.start_date).days
        return self.vehicle.calculate_rental_cost(days)

    def end_reservation(self):
        self.vehicle.return_vehicle()

    def display_details(self):
        print(f"Reservation: {self.customer.name} -> {self.vehicle.make} {self.vehicle.model}")
        print(f"From {self.start_date} to {self.end_date}")
        print(f"Total Cost: {self.calculate_total_cost()}")
        print(f"Vehicle Status: {'Available' if self.vehicle.check_availability() else 'Rented'}")


#Polymorphic Function
def display_info(obj):
    obj.display_details()


#Use case
if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 50)
    suv1 = SUV("Honda", "CR-V", 80)
    truck1 = Truck("Ford", "F-150", 100)

    customer1 = Customer("Masoom", "0300-1234567")

    #reservations
    res1 = RentalReservation(customer1, car1, date(2025, 9, 13), date(2025, 9, 16))

    print("\n--- Vehicle Details ---")
    display_info(car1)
    display_info(suv1)
    display_info(truck1)

    print("\n--- Reservation Details ---")
    display_info(res1)

    print("\n--- Customer Rental History ---")
    customer1.display_history()

    #End reservation
    res1.end_reservation()
    print("\nAfter returning vehicle:")
    car1.display_details()
