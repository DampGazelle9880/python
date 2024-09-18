class A():
    def __init__(self,a):
        self.a = a
    def __lt__(self,other):
        if(self.a < other.a):
            return "ob1 is less than ob2"
        else:
            return "Both are equal"
    def __eq__(self,other):
        if(self.a == other.a):
            return "Both are equal"
        else:
            return "Not equal"
ob1 = A(9)
ob2 = A(1)
print("Passed value =", ob1.a,ob2.a)
print(ob1 < ob2)
ob3 = A(10) 
ob4 = A(10)
print("Passed value =", ob3.a,ob4.a) 
print(ob3 == ob4)          
       