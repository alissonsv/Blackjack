class Wallet():
    def __init__(self, value):
        self.balance = value


    def get_balance(self):
        print(f'BALANCE: {self.balance}')