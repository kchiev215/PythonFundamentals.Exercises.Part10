class Person:
    def __init__(self, person_id, first_name, last_name):
        self.id = person_id
        self.firstname = first_name
        self.lastname = last_name


class Account:
    def __init__(self, account_num, account_type, owner):
        self.account_id = account_num
        self.account_type = account_type
        self.owner: Person = owner
        self.balance = 0


class Bank:
    def __init__(self):
        self.accounts = {}
        self.customers = {}

    def add_customer(self, person: Person):
        if person.id in self.customers:
            print("you're not welcomed")
            # raise ValueError(f"{person_id} is already registered in our system")
        else:
            name = person.firstname + ' ' + person.lastname
            self.customers[person.id] = name

    def add_account(self, account: Account):
        if account.owner.id not in self.customers:
            raise ValueError(f'{account.owner.id} is not a customer of our bank')
        elif account.account_id in self.accounts:
            raise ValueError(f'{account.account_id} already exists in our system')
        else:
            self.accounts[account.account_id] = account

    def remove_account(self, person_id, account_id):
        if person_id not in self.customers:
            raise ValueError(f"{person_id} is not a customer in our bank")
        elif account_id in self.accounts:
            del self.accounts[account_id]
        else:
            raise ValueError(f"{account_id} isn't a valid account")

    def deposit_money(self, account_id, amount):
        if account_id in self.accounts:
            account = self.accounts.get(account_id)
            account.balance += round(amount, 2)

    def withdraw_money(self, account_id, amount):
        if account_id in self.accounts:
            account = self.accounts.get(account_id)
            account.balance -= round(amount, 2)

    def balance_inquiry(self, account_id):
        if account_id in self.accounts:
            balance = self.accounts.get(account_id).balance
            return round(balance, 2)
        else:
            raise ValueError(f"Account with id {account_id} does not exist.")


