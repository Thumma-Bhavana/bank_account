class bank_account():
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
    def deposite(self, amt):
        self.amount += amt
        print(f'your account balance after deposite: {self.amount}')
    def withdraw(self, amt):
        if(self.amount < amt):
            print('Insufficient funds')
            return
        self.amount -= amt
        print(f'your account balance after withdrawal: {self.amount}')
    def display(self):
        print("Net Available Balance: ", self.amount)
    def __str__(self):
        return f'account holder: {self.name}, amount: {self.amount}'

b = bank_account('Bhavana', 1000)
switcher = {
    'd': 
        b.deposite,
    'w': 
        b.withdraw,
    'a':
        b.display,
    'p':
        b
}
while(True):
    s =  input('deposite: d, withdrawal: w , display amount: a, print: p, 0: exit  ')
    if(s == '0'):
        print('Thank You')
        break
    else:
        func = switcher.get(s)
        if(func == b.display):
            func()
        if(func == b):
            print(b)
        else:
            amt = float(input("Enter amount "))
            func(amt)
