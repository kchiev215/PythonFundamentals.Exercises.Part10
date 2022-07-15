from plistlib import Dict


class Person:
    def __init__(self, person_id, firstname, lastname):
        self.id = person_id
        self.firstname = firstname
        self.lastname = lastname


class Account:
    def __init__(self, account_number, type_of_account, owner, balance):
        self.account_number = account_number
        self.type = type_of_account
        self.owner = owner
        self.balance = balance


class Bank:
    def __init__(self, customer, account):
        self.customers = Dict[int, customer] = dict()
        self.accounts = Dict[int, account] = dict()

    def add_customer(self, customer: Person):
        if customer.id in self.customers:
            raise ValueError(f"Customer with {customer.id} customer id exists in our system")
        else:
            self.customers[customer.id] = customer

    def add_account(self, account: Account):
        if account.owner.id not in self.customers:
            raise ValueError(f"You're not a customer of our bank")
        elif account.account_number in self.accounts:
            raise ValueError(f"{account.account_number} already exist in our systems")
        else:
            self.accounts[account.account_number] = account

    def remove_account(self, account_id):
        if account_id in self.accounts:
            del (self.accounts[account_id])
        else:
            raise ValueError(f"{account_id} does not exist in our systems")

    def deposit(self, deposit_amount, account_id):
        if account_id in self.accounts:
            account = self.accounts.get(account_id)
            account.balance += round(deposit_amount, 2)
        else:
            raise ValueError(f"{account_id} does not exist in our systems")

    def withdraw(self, withdraw_amount, account_id):
        if account_id in self.accounts:
            account = self.accounts.get(account_id)
            account.balance -= round(withdraw_amount, 2)
        else:
            raise ValueError(f"{account_id} does not exist in our systems")

    def balance_inquiry(self, account_id):
        if account_id in self.accounts:
            balance = self.accounts.get(account_id)
            return round(balance, 2)
        else:
            raise ValueError(f"{account_id} does not exist in our systems")
