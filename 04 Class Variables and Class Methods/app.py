class Bank:
    bank_name = "Meezan Bank Limited"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder} | Bank Name: {self.bank_name}")

# Creating instances
customer1 = Bank("Basit")
customer2 = Bank("Ahmed")

print("Before changing bank name:")
customer1.display()
customer2.display()

# Changing bank name using class method
Bank.change_bank_name("Chartered Bank")

print("\nAfter changing bank name:")
customer1.display()
customer2.display()