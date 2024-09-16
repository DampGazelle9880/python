class BWM():
    def start_engine(self):
        print("BWM engine started!")
    def stop_engine(self):
            print("BWM engine stopped!")
    def drive(self):
        print("BWM driving!")
        

class Ferrari():
    def start_engine(self):
        print("Ferrari engine started!")
    def stop_engine(self):
            print("Ferrrari engine stopped!")
    def drive(self):
        print("Ferrari driving!")
def start_and_drive(car):
    car.start_engine()
    car.stop_engine()
    car.drive()
bwm_car = BWM()
ferrari_car = Ferrari()
start_and_drive(bwm_car)
start_and_drive(ferrari_car)
    
        
        
                        