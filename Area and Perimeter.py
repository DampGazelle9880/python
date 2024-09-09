import math

class Circle():
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius**2)
    def perimeter (self):
        return 2 * math.pi * self.radius
obj = Circle(11)
    
area_cir = obj.area()
print(f"The area of the circle is: {area_cir.f}") 
perimeter_cir = obj.perimeter()
print(f"The perimeter of circle is:{perimeter_cir.f}")
   