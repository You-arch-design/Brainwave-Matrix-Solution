class ATM:
    def __init__(self, balance=1000, pin=1234):  # Fixed constructor name
        self.balance = balance
        self.pin = pin

    def authenticate(self):
        for attempt in range(3):
            entered_pin = int(input("Enter your PIN: "))
            if entered_pin == self.pin:
                print("Authentication successful!\n")
                return True
            print(f"Incorrect PIN. {2 - attempt} attempts remaining.")
        print("Authentication failed. Exiting.")
        return False

    def check_balance(self):
        print(f"Your balance: ${self.balance}\n")

    def deposit(self):
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}\n")
        else:
            print("Invalid amount.\n")

    def withdraw(self):
        amount = float(input("Enter withdrawal amount: "))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ${amount}. New balance: ${self.balance}\n")
        else:
            print("Insufficient funds or invalid amount.\n")

    def start(self):
        if not self.authenticate():
            return
        
        while True:
            print("1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
            choice = input("Choose an option: ")
            
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank you! Goodbye!")
                break
            else:
                print("Invalid option. Try again.\n")

if __name__ == "__main__":  # Fixed name check
    atm = ATM()
    atm.start()
