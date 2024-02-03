#create bank account
#deposit money
#withdraw money
#calculate interest for saving account

class BankAccount:
    def __init__(self, acc_number, acc_holder, balance):
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance+amount
        print(self.balance)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print("insufficient")
        print(self.balance)

    #def interest(self, total):
    #    SI = (total * rate * time)/100
    #    print(SI)
        
class SavingAcc(BankAccount):
    def __init__(self, acc_number, acc_holder, balance, interest_rate):
        super().__init__(acc_number, acc_holder, balance)
        self.interest_rate = interest_rate

    def calInt(self):
        return self.balance * (self.interest_rate / 100)

#ob = BankAccount(acc_number='1', acc_holder='A', balance='100')
#os = SavingAcc(interest_rate='3')

#ob.deposit
#ob.withdraw
#os.calInt
    
acc1 = SavingAcc(1, "abc", 100, 3)
acc1.deposit(500)
acc1.withdraw(100)
SI = acc1.calInt()
print(acc1.balance)
print(SI)