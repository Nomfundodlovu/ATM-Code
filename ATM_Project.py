class ATM:
    def __init__(self, balance = 1000, pin = 2023):
        self.balance = balance
        self.pin = pin
        
    def run(self):
        input_pin = int(input("Enter your PIN: "))

        #Verify pin, if incorrect it exits
        if input_pin != self.pin:
            print("Incorrect PIN. Exiting...")
            return

        while True:
            print("1. Check balance")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Exit")

            choice = int(input("Enter choice: "))

            if choice == 1:
                print("Your current balance is: R", self.balance)
            elif choice == 2:
                amount = int(input("Enter amount to withdraw: "))
                if self.balance < amount:
                    print("Insufficient funds. Your balance is: R", self.balance)
                else:
                    self.balance -= amount
                    print("Withdrawal successful. Your remaining balance is: R", self.balance)
            elif choice == 3:
                amount = int(input("Enter amount to deposit: "))
                self.balance += amount
                print("Deposit successful. Your new balance is: R", self.balance)
            elif choice == 4:
                print("Thank you for using our ATM.")
                return
            else:
                print("Invalid choice.")
    
absa_atm = ATM(1000, 2023)
absa_atm.run()