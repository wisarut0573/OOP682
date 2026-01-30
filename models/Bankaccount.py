class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def __sub__(self, other):
        if isinstance(other, BankAccount):
            new_balance = self.balance + other.balance
            new_balance = BankAccount(new_balance)
            return new_balance
        return None
        
    def __add__(self, other):
        if isinstance(other, BankAccount):
            new_balance = self.balance + other.balance
            new_balance = BankAccount(new_balance)
            return new_balance
        return None
    
    def __str__(self):
        return f"BankAccount(Balance: {self.balance})"
    
        