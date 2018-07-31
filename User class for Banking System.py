class User:

    def __init__ (self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
        
    def withdraw(self, money_withdraw):
        if self.balance >= money_withdraw:
            self.balance -= money_withdraw
            return self.name + ' has ' + str(self.balance) + '.'
        else:
            raise ValueError()
                        
    def check(self, user, money_check):
        if user.checking_account == False or user.balance < money_check:
            raise ValueError()
        else:
            self.balance += money_check
            user.balance -= money_check
            return self.name + ' has ' + str(self.balance) + ' and ' + user.name + ' has ' + str(user.balance) + '.'
            
    def add_cash(self, money_add):
        self.balance += money_add
        return self.name + ' has ' + str(self.balance) + '.'
