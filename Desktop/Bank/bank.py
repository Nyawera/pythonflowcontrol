
            
 
class Account:

    def __init__(self,account_name,account_number):
        self.account_name= account_name
        self.acount_number = account_number 
        self.balance = 0
        self.deposits =  []
        self.withdrawals= []
        


    def deposit(self,amount):
    
        if amount <=0:
            return f"Deposit amount must be greater than zero"

        else:
            self.balance+= amount
            self.deposits.append (amount)
        return  f"hello {self.account_name}you have deposited {amount} and your new balance is{self.balance} and the amount is {self.deposits}"

            
    def withdraw(self,amount):
        self.transaction=100
        if amount<=0:
            return f"withdrawals must be positive"
        elif  amount>self.balance:
            return f"your balance is {self.balance},you cant withdraw {amount}"
        else:
            self.balance-=amount+self.transaction
            self.withdrawals.append(amount)

        return f"hello {self.account_name} you have withdrawn {amount} and your new balance is {self.balance} and your withdrawals is {self.withdrawals}"

        
    def deposits_statement(self):
        for y in self.deposits:
            print (y,end="\n")
            
    def withdrawals_statement(self): 
        for y in self.deposits:
            print (y,end="\n") 
            
    def current_balance(self):
        return f"{self.balance}"

