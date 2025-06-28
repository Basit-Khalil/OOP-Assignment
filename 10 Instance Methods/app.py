class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"Woof! My name is {self.name} and I am a {self.breed}.")

dog1 = Dog("Oscar", "Labrador")
dog1.bark()
