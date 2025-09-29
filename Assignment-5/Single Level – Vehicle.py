class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def show_details(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Seats: {self.seats}")


car1 = Car("Toyota", "Corolla", 5)
car1.show_details()


v = Vehicle("Honda", "Civic")
print(f"Vehicle: {v.brand} {v.model}")

