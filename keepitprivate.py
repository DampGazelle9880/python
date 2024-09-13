class mylib ():
    __privateVariable = -1;
    def __privateMethod(self):
        print("I am inside a library.")
    def nor(self):
        print("Private informathion is:",mylib.__privateVariable)
zoh = mylib()
zoh.__privateMethod
zoh.nor()        