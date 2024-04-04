class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def __add__(self, other):
        if self.currency == other.currency:
            return self.amount+ other.amount
        else:
            raise RuntimeError("Mismatched currencies!")
        
        
        
    def __mul__(self, number):
        return self.amount * number
    
    def __str__(self):
        return f" Amount is {self.amount}"

m = Money(20, "EUR") + Money(30,"USD")
print(m)