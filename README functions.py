
import small_town_teller1

zc_bank = small_town_teller1.Bank()
bob = small_town_teller1.Person(1, "Bob", "Smith")
zc_bank.add_customer(bob)
bob_savings = small_town_teller1.Account(1001, "SAVINGS", bob)
zc_bank.add_account(bob_savings)
print(zc_bank.balance_inquiry(1001))
# 0
zc_bank.deposit_money(1001, 256.02)
print(zc_bank.balance_inquiry(1001))
# 256.02
print(zc_bank.withdraw_money(1001, 128))
print(zc_bank.balance_inquiry(1001))
