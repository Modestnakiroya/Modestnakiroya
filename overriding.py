class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start_engine(self):
        return f"{self.brand} {self.model} engine started with a key"
    
    def get_info(self):
        return f"Vehicle: {self.brand} {self.model}"

class ElectricCar(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
    
    def start_engine(self):
        return f"{self.brand} {self.model} started silently (electric motor)"
    
    def get_info(self):
        return f"Electric Car: {self.brand} {self.model}, Battery: {self.battery_capacity}kWh"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, engine_size):
        super().__init__(brand, model)
        self.engine_size = engine_size
    
    def start_engine(self):
        return f"{self.brand} {self.model} roars to life! ({self.engine_size}cc engine)"

print("=== METHOD OVERRIDING EXAMPLE ===")
vehicles = [
    Vehicle("Toyota", "Camry"),
    ElectricCar("Tesla", "Model 3", 75),
    Motorcycle("Harley-Davidson", "Street 750", 750)
]

for vehicle in vehicles:
    print(f"{vehicle.get_info()}")
    print(f"Starting: {vehicle.start_engine()}")
    print("-" * 50)