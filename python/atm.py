class atm:
    def __init__(self):
        self.balance = 0
        self.pin = None
        self.menu()
        

    def menu(self):
        print("1. Check balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Change pin")
        print("5. Exit")
        
        user_input = input("Enter your choice: ")
        if user_input == "1":
                self.get_balance()
        elif user_input == "2":
             self.withdraw()
        elif user_input == "3":
             self.deposit()
        elif user_input == "4":
             self.set_pin()
        elif user_input == "5":
             print("Exiting...")
             exit()
        else:
             print("Invalid choice. Please try again.")
             

    def set_pin(self):
        if self.pin == None:
            pin = int(input("Please enter your pin: "))
            self.pin = pin
            print("Pin set successfully")
        elif self.pin != None:
            print("You already have a pin set.")
            current = int(input("If you want to change your pin, please enter your current pin." ))
            if current == self.pin:
                pin = int(input("Please enter your new pin: "))
                if pin == self.pin:
                    print("Cannot use already used pin set up a new one ")
                    
                else:
                    self.pin = pin
                    print("Pin changed successfully")
                    
        self.menu()    

    def verify_pin(self):
        pin = int(input("Please enter your pin: "))
        if self.pin == pin:
            return True
        else:
            return False

    def get_balance(self):
        if self.verify_pin():
            print("Your balance is: ", self.balance)
        else:
            print("Invalid pin. Please try again.")
        self.menu()
        
        

    def withdraw(self):
        if self.balance <=0:
            print("Insufficient balance")
            
        elif self.verify_pin():
            print("Your balance is: ", self.balance)
            amount = int(input("Enter the amount you want to withdraw: "))
            if amount > self.balance:
                print("Insufficient balance")
                
            else:
                self.balance -= amount
                print("Withdrawal successful. Your new balance is: ", self.balance)
        self.menu()

    def deposit(self):
        if self.verify_pin():
            print("Your balance is: ", self.balance)
            amount = int(input("Enter the amount you want to deposit: "))
            self.balance += amount
            print("Deposit successful. Your new balance is: ", self.balance)
        else:
            print("Invalid pin. Please try again.")
        self.menu()

sbi = atm()

