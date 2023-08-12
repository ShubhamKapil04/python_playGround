import datetime


class Account:

    @staticmethod
    def _curr_time(self):
        time = datetime.datetime.now()
        return time

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        print(f'Account created for {name}')
        self.trans_list = [(Account._curr_time(self), balance)]  # Tuple
        self.show_tran_list()

    # Amount
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show()
            self.trans_list.append((Account._curr_time(self), amount))

    def withdraw(self, amount):
        # if 0 < amount and amount <= self.__balance
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.show()
            self.trans_list.append((Account._curr_time(self), amount))
        else:
            print(f'Hey {self._name}, You are Bankrupted')

    def show(self):
        print(f'{self._name} _balance is {self.__balance}')

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
print('x'*20)
print(Shubham.__dict__)
