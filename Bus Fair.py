class Vehicle():
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage
        
        
class Bus(Vehicle):
    def __init__(self, name, maxspeed, mileage):
        super().__init__(name, maxspeed, mileage)
        self.capacity = capacity
        
        def fare(self):
            bus_fare = 10
            total_fare = self.capacity * bus_fare
            return total_fare
school_bus = Bus("Dash",200,100,10,79)
print("Vehicle name:",school_bus.name)   
print("Speed:",school_bus.maxspeed)    
print("Mileage:",school_bus.mileage) 
print("Total fare:",school_bus.fare())
            
    