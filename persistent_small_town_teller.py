from small_town_teller1 import Person, Account, Bank

class PersistenceUtils:
    def write_pickle(self):
        pass

    def load_pickle(self):
        pass

zc_bank = Bank()
zc_bank.customers
# {}
zc_bank.accounts
# {}
# zc_bank.load_data()
zc_bank.customers
# {1: <persistent_small_town_teller.Person object at 0x1098e6a90>}
zc_bank.accounts
# {1001: <persistent_small_town_teller.Account object at 0x1099e04d0>}

