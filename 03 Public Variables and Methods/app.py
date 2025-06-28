class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"The {self.brand} car has started successfully!")

my_car = Car("Honda")

print(f"Car Brand Selected: {my_car.brand}")
my_car.start()