class bank_account():
    def __init__(self , owner , balance ):
        self.owner = owner
        self.balance = balance
    def deposit(self):
        self.owner_deposit = int(input("Enter the amount you want to deposit "))
        while(self.owner_deposit == 0):
            self.owner_deposit = int(input("Enter the amount you want to deposit "))
        self.balance += self.owner_deposit
        print(f'Account replenished! Balance : {self.balance}')
    def withdraw(self):
        self.owner_withdraw = int(input("Enter the amount you want to withdraw "))
        while(self.owner_withdraw > self.balance):
            self.owner_withdraw = int(input("Not enough funds, please try again "))
        self.balance -= self.owner_withdraw
        print(f'Withdrawal of funds was successful! Balance : {self.balance}')

little_arab = bank_account("Habibi" , 10000000)
start = input(f'Hello {little_arab.owner} START/EXIT ')
while(start == "START"):
    operation = input("deposit/withdraw ")
    if(operation == "deposit"):
        little_arab.deposit()
    else:
        little_arab.withdraw()
    start = input("START/EXIT ")
print(f'Goodbye , {little_arab.owner} !')