# hamarya done
import abc


class Account(abc.ABC):
    def __init__(self, account_type: str, balance: float, interest_rate: float):
        self.account_type = account_type
        self.balance = balance
        self.interest_rate = interest_rate

    @abc.abstractmethod
    def calculate_rate(self):
        pass


class SavingAccount(Account):
    def calculate_rate(self):
        return self.balance * 0.1


class CheckingAccount(Account):
    def calculate_rate(self):
        return self.balance * 0.2


class Transaction:
    def __init__(self, account: Account, trans_type: str, amount: float):
        self.account = account
        self.trans_type = trans_type
        self.amount = amount


class Customer:
    def __init__(self, name: str, address: str, contact_info: str):
        self.name = name
        self.address = address
        self.contact_info = contact_info

    def implement_transaction(self, account: Account, trans_type: str, amount: float):
        trans = Transaction(account, trans_type, amount)
        if account in bank.accounts:
            if trans.trans_type == 'withdraw':
                if amount <= account.balance:
                    account.balance -= amount
                    print(f'Transaction successfully done, current balance is {account.balance}')
                else:
                    print(f'Amount is higher, balance is {account.balance}')
            elif trans.trans_type == 'deposit':
                account.balance += amount
                print(f'Transaction successfully done, current balance is {account.balance}')
        else:
            print('Account currently unavailable,please try another one.')


class BankingSystem:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.accounts = []

    def create_account(self, customer: Customer, account_type: str, balance: float, interest_rate: float):
        self.customers.append(customer)
        if account_type == 'saving':
            save_ac = SavingAccount(account_type, balance, interest_rate)
            self.accounts.append(save_ac)
            return save_ac
        elif account_type == 'checking':
            check_ac = CheckingAccount(account_type, balance, interest_rate)
            self.accounts.append(check_ac)
            return check_ac
        else:
            return 'Invalid type'

    def delete_account(self, account: Account):
        if account in self.accounts:
            self.accounts.remove(account)
        else:
            print('No such account in this bank')

    def create_customer(self, name, address, contact_info):
        cust = Customer(name, address, contact_info)
        self.customers.append(cust)
        return cust


bank = BankingSystem('Ameria')
customer1 = bank.create_customer('Anna', 'Baker st. 14', '+7700251656')
customer2 = bank.create_customer('Lily', 'Abovyan st. 23', '+37455812036')
account1_1 = bank.create_account(customer1, 'saving', 250, 20)
account1_2 = bank.create_account(customer2, 'saving', 300, 25)
account2_1 = bank.create_account(customer2, 'checking', 300, 35)
bank.delete_account(account2_1)
print('Here are available accounts in our bank:')
for i in bank.accounts:
    print(f'Account type: {i.account_type},  Balance: {i.balance},  Rate: {i.interest_rate}')
customer1.implement_transaction(account1_1, 'withdraw', 150)
customer2.implement_transaction(account2_1, 'deposit', 500)
saving = SavingAccount('saving', 500, 45)
print('Savings account interest rate is ', saving.calculate_rate())
