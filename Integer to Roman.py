class roman():
    def __init__(self):
        self.values = [
            (1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),
            (90,'XC'),(50,'L'),(40,'XL')(10,'X'),(9,'IX'),(5,'V'),(3,'III'),(1,'I')
            
        ]
    def convert(self,num):
         roman_numeral = '' 
    for value,numeral in self.Value:
        while num >= value:
            roman_numeral += numeral
            num -= Value
        return roman_numeral
    convertor = roman()
    number = 1000
    print(f"The roman numeral for{number}is{convertor.convert}(number)")
           
            
    
                                
        