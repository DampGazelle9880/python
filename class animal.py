from abc import ABC,abstractmethod
class animal(ABC):
    def move(self):
        pass
class Human(animal):
    def move(self):
        print("I can run and walk!")
class Snake(animal):
    def move(self):
        print("I can crawl!")
class Dog(animal):
    def move(self):
        print("I can bark!")
class Lion(animal):
    def move(self):
        print("I can roar!")
h = Human()
h.move()
s = Snake()
s.move()
d = Dog()
d.move()
l = Lion()
l.move()
    
    