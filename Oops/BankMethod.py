import datetime


# Add date time module
# Exercise
class Account:
    @staticmethod
    def curr_time(self):
        time = datetime.datetime.now()
        return time

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        print(f'Account created for {name}')
        self.trans_list = [(Account.curr_time(self), balance)]  # Tuple
        self.show_tran_list()

    # Amount
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show()
            self.trans_list.append((Account.curr_time(self), amount))

    def withdraw(self, amount):
        # if 0 < amount and amount <= self.balance
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.show()
            self.trans_list.append((Account.curr_time(self), amount))
        else:
            print(f'Hey {self.name}, You are Bankrupted')

    def show(self):
        print(f'{self.name} balance is {self.balance}')

    def show_tran_list(self):
        for date, amount in self.trans_list:
            if amount > 0:
                trans_typ = 'Deposit'
            else:
                trans_typ = 'Withdraw'
                amount *= -1
            print(f'Amount {amount} dollar, {trans_typ} on {date}')


Shubham = Account('Kartik', 20)
Shubham.deposit(100)
Shubham.show()
Shubham.withdraw(80)
Shubham.show_tran_list()

print('X' * 20)

kartik = Account('Shubham', 200)
kartik.deposit(450)
kartik.withdraw(230)
kartik.withdraw(1000)
kartik.deposit(2000)
kartik.show_tran_list()
