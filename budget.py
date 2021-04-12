# Object class
class Budget:
    # Initial function created
    def __init__(self, food, clothing, entertainment):
        self.food = food
        self.clothing = clothing
        self.entertainment = entertainment
        self.food_balance = 0
        self.clothing_balance = 0
        self.entertainment_balance = 0
        self.food_withdrawal = 0
        self.clothing_withdrawal = 0
        self.entertainment_withdrawal = 0
        self.food_deposit = 0
        self.clothing_deposit = 0
        self.entertainment_deposit = 0

    # Function to prompt user about which operation he/she wants to perform
    def operations(self):
        print(" ")
        print("******************************************")
        selected_options = int(input("What would you like to do?\nAVAILABLE OPERATIONS:\n(1) Deposit"
                                     "\n(2) Check Balance\n(3) Withdrawal\n(4) Food to Cloth transfer\n"
                                     "(5) Food to Entertainment transfer\n(6) Cloth to Food transfer\n"
                                     "(7) Cloth to Entertainment transfer\n(8) Entertainment to Food transfer\n"
                                     "(9) Entertainment to Cloth transfer\n(10) Exit\n"))
        if selected_options == 1:
            self.deposit()
        elif selected_options == 2:
            self.category_balance()
        elif selected_options == 3:
            self.withdrawal()
            print("Please take your cash")
            self.options()
        elif selected_options == 4:
            self.food_to_cloth()
        elif selected_options == 5:
            self.food_to_entertainment()
        elif selected_options == 6:
            self.cloth_to_food()
        elif selected_options == 7:
            self.cloth_to_entertainment()
        elif selected_options == 8:
            self.entertainment_to_food()
        elif selected_options == 9:
            self.entertainment_to_cloth()
        elif selected_options == 10:
            print("Thank you for your patronage")
            exit()
        else:
            print("Please enter a valid option")
            self.operations()

    # Fund Deposit function
    def deposit(self):
        print(" ")
        print("******************************************")
        print("What category would you like to deposit into?")
        option=int(input("1. Food\n2. Cloth\n3. Entertainment\n"))
        if option==1:
            self.food_deposit = int(input("Enter how much you want to deposit for food\n"))
            self.food_balance += self.food_deposit
            print(f"You have deposited ${self.food_deposit} in food successfully.")
        elif option==2:
            self.clothing_deposit = int(input("Enter how much you want to deposit for clothing\n"))
            self.clothing_balance += self.clothing_deposit
            print(f"You have deposited ${self.clothing_deposit} in clothing successfully.")
        elif option==3:
            self.entertainment_deposit = int(input("Enter how much you want to deposit for entertainment\n"))
            self.entertainment_balance += self.entertainment_deposit
            print(f"You have deposited ${self.entertainment_deposit} in entertainment successfully.")
        else:
            print("Invalid option Dear!! kindly enter a valid option ")
        print(" ")
        
        self.options()

    # Fund withdrawal function
    def withdrawal(self):
        print(" ")
        print("**************************************")
        print("WITHDRAWAL OPERATIONS")
        print("What category would you like to witdraw from?")
        option=int(input("1. Food\n2. Cloth\n3. Entertainment\n"))
        if option==1:
            self.food_withdrawal = int(input("How much would you like to withdraw from food\n"))
            self.food_balance -= self.food_withdrawal
        elif option==2:
            self.clothing_withdrawal = int(input("How much would you like to withdraw from clothing\n"))
            self.clothing_balance -= self.clothing_withdrawal
        elif option==3:
             self.entertainment_withdrawal = int(input("How much would you like to withdraw from entertainment\n"))
             self.entertainment_balance -= self.entertainment_withdrawal
        else:
            print("Invalid option Dear!! kindly enter a valid option ")
       
    # Function to display balance for each category
    def category_balance(self):
        print(" ")
        print("*************************************")
        print("YOUR CATEGORY BALANCE:")
        print(f"Food: ${self.food_balance}")
        print(f"Clothing: ${self.clothing_balance}")
        print(f"Entertainment: ${self.entertainment_balance}")
        self.options()

    # Function to display balance after transfer of funds from food to clothing category
    def food_to_cloth(self):
        print(" ")
        print("*****************************************")
        print("FOOD TO CLOTH TRANSFER")
        self.withdrawal()
        self.clothing_balance = self.clothing_balance + self.food_withdrawal
        print(f"Clothing balance = {self.clothing_balance}")
        self.options()

    # Function to display balance after transfer of funds from food to entertainment category
    def food_to_entertainment(self):
        print(" ")
        print("****************************************")
        print("FOOD TO ENTERTAINMENT TRANSFER")
        self.withdrawal()
        self.entertainment_balance = self.entertainment_balance + self.food_withdrawal
        print(f"Entertainment balance = {self.entertainment_balance}")
        self.options()

    # Function to display balance after transfer of funds from cloth to food category
    def cloth_to_food(self):
        print(" ")
        print("******************************************")
        print("CLOTH TO FOOD TRANSFER")
        self.withdrawal()
        self.food_balance = self.food_balance + self.clothing_withdrawal
        print(f"Food balance = {self.food_balance}")
        self.options()

    # Function to display balance after transfer of funds from cloth to entertainment category
    def cloth_to_entertainment(self):
        print(" ")
        print("*********************************************")
        print("CLOTH TO ENTERTAINMENT TRANSFER")
        self.withdrawal()
        self.entertainment_balance = self.entertainment_balance + self.clothing_withdrawal
        print(f"Entertainment balance = {self.entertainment_balance}")
        self.options()

    # Function to display balance after transfer of funds from entertainment to food category
    def entertainment_to_food(self):
        print(" ")
        print("************************************************")
        print("ENTERTAINMENT TO FOOD TRANSFER")
        self.withdrawal()
        self.food_balance = self.food_balance + self.entertainment_withdrawal
        print(f"Food balance = {self.food_balance}")
        self.options()

    # Function to display balance after transfer of funds from entertainment to cloth category
    def entertainment_to_cloth(self):
        print(" ")
        print("*****************************************************")
        print("ENTERTAINMENT TO CLOTH TRANSFER")
        self.withdrawal()
        self.clothing_balance = self.clothing_balance + self.entertainment_withdrawal
        print(f"Clothing balance = {self.clothing_balance}")
        self.options()

    # Function to prompt user if he/she wants to perform another operation
    def options(self):
        selected_option = int(input("Do you want to perform another operation?\n(1) Yes\n(2) No\n"))
        if selected_option == 1:
            self.operations()
        elif selected_option == 2:
            print("Thank you for your patronage")
            exit()


print("Category entry")
# Person object
person = Budget(
    input("Please enter your food category\n"),
    input("Please enter your clothing category\n"),
    input("Please enter your entertainment category\n")
)

print(" ")
print("*******************************************")
print("Categories are:\nFOOD\nCLOTHING\nENTERTAINMENT")
print(" ")
print("*********************************************")
print("The category names are:\n", person.food, "\n", person.clothing, "\n", person.entertainment)

person.operations()
