class Bank_Account():
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance
    def withdraw(self, amount):
        if(self.balance < amount):
            print(f"insufficient funds, Available balance is: {self.balance}")
        else:
            self.balance -= amount
            print(f"Available balance after withdrawal: {self.balance}")

    def deposite(self, amount):
        self.balance+=amount
        print(f"Available balance after deposit: {self.balance}")
    
    def __str__(self):
        return f"name: {self.name}, available balance: {self.balance}"

account = Bank_Account("Bhavana", 10000)
print(f"Account Created, name: {account.name}, available balance: {account.balance}")
def switch():
    while(True):
        print("Press d for Deposit\npress w for Withdraw \npress p for display account\npress e for Exit ")
        option = input("your option : ")
        if option == 'd':
            amount=(int(input("enter the amount to be deposited: ")))
            account.deposite(amount)
            continue
        elif option == 'w':
            amount=(int(input("enter the amount to be withdrawn: ")))
            account.withdraw(amount)
            continue
        elif option == 'p':
            print(account)
            continue
        elif option == 'e':
            print("Thank You")
            break
        else:
            print("Incorrect option")
switch()    
