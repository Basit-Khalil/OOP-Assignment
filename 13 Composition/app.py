class Engine:
    def __init__(self, power):
        self.power = power  

    def ignite(self):
        print(f"Engine with {self.power} horsepower is igniting...") 

class Vehicle:
    def __init__(self, model, engine):
        self.model = model 
        self.engine = engine

    def activate(self):
        print(f"Starting the {self.model} vehicle.")
        self.engine.ignite() 

engine2 = Engine(300)

vehicle1 = Vehicle("Chevrolet", engine2)

vehicle1.activate() 