class Bank:
    
    def __init__(self):
        self.accounts = []

    def __str__(self):
        account_descriptions = []
        for account in self.accounts:
            account_descriptions.append(str(account))
        return f"Bank Accounts: " + ", " .join(account_descriptions)
    





class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number} - Account Balance: {self.balance}"
    




class Customer:
    def __init__(self, name, age, account_number):
        self.name = name
        self.age = age
        self.account_number = account_number

    def __str__(self):
        return f"Customer Name: {self.name} - Customer Age: {self.age} - Customer Account Number: {self.account_number}"





nordea = Bank()

nordea.accounts.append(Account("nr. 121233", 0), Account("nr. 323421", 200000))

customer = Customer("Mikkel", 25, nordea.accounts[0].account_number)

print(nordea)

print(customer)
