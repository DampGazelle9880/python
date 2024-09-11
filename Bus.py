class vehicle():
    def __init__(self,name,maxspeed,mileage):
        self.name = name
        self.maxspeed = maxspeed
        self.mileage = mileage
class bus(vehicle):
    pass
school_bus = bus("Dash",190,110)
print("Vehicle name:",school_bus.name, "speed", school_bus.maxspeed, "milage", school_bus.mileage)        
    
    
        