from abc import ABC,abstractmethod
class absABC(ABC):
    def at(self,x):
        print("Pass value = ", x)
    @abstractmethod
    def task(self):
        print("You are inside ABS class.")
class abcs(absABC):
    def task(self):
         print("You are inside abcs class.")
sb = abcs()
sb.task()
sb.at(999)
    
        
   