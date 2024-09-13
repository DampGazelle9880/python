class Computor():
    def __init__(self):
        self.__maxprice = 999
    def sell(self):
        print("Selling price: {}".format(self.__maxprice))
    def set_maxprice(self,price):
        self.__maxprice = price
zn = Computor()
zn.sell()
zn.__maxprice = 99
zn.sell()
zn.set_maxprice(1230)     
zn.sell()        