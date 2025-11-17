from exercises.customer_data import read_customers
from exercises.bank_account import BankAccount, SavingsAccount

# ===== CSV & Collections Exercise =====
file_path = "data/customers.csv"
read_customers(file_path)

# ===== OOP Bank Account Exercise =====
print("\n=== Bank Account Example ===")
acc1 = BankAccount("001", "Alice", 1000)
acc1.deposit(500)
acc1.withdraw(200)

print("\n=== Savings Account Example ===")
sacc = SavingsAccount("002", "Bob", 2000, interest_rate=0.05)
sacc.deposit(500)
sacc.add_interest()
sacc.withdraw(1000)
