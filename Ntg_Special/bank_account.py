class bank_account:
    def __new__(cls, name, balance ):
        if not isinstance(name,str) or not isinstance(balance,int) or balance < 0  :
            print("Enter valid details ! Account not created")
            return None
        return super().__new__(cls)

    def __init__(self, name, balance):
        self.name = name 
        self. balance = balance
        self.transaction = []



    def withdraw(self,amount):
        if amount > self.balance:
            print("Not enough balance !")
            return
        if amount < 1:
            print("Enter a valid amount to withdraw !")
            return
        self.balance -= amount
        self.transaction.append(f'Withdrew {amount}')
        print(f"{amount} successfully withdrew from {self.name}'s account ! Current balance is {self.balance}")



    def deposit(self, amount):
        if amount < 5 :
            print("Enter a valid amount to deposit !")
            return
        self.balance += amount
        self.transaction.append(f'Deposited {amount}')
        print(f"{amount} successfully deposited in {self.name}'s account ! Current balance is {self.balance}")


    def get_balance(self):
        return self.balance

    def show_transactions(self):
        if not self.transaction:
            print("No transactions made yet !")
        else:
            for trans in self.transaction:
                print(trans)


    def show_summary(self):
        print("==== ACCOUNT SUMMARY ====")
        print(f'Account holder : {self.name}')
        print(f'Balance : {self.balance}')
        print(f'Total Transactions : {len(self.transaction)}')
        print("==========================")


acc1 = bank_account("Dawood",100)

print(f'Balance : {acc1.get_balance()}')

acc1.withdraw(10)
acc1.deposit(5)
acc1.withdraw(54)
acc1.show_transactions()
acc1.show_summary()


