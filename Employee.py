class Employee():
    
    def __init__(self):
        print("Employeee created.")
    def __del__(self):
        print("Destructor called.")
def Create_obj():
    print("Making object.")
    obj = Employee()
    return obj
obj = Create_obj()     
 