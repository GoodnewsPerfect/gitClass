from datetime import datetime

#datetime object containing current date and time
e = datetime.now()
        
print('%s' %e) #prints current date and time
import random

database = {}

def init():

    print("Welcome to bankGoody!!!")

    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):
        
        login()
    elif(haveAccount == 2):
        
        register()
    else:
        print("You have selected invalid option, please kindly select a valid option")
        init()

def register():

    print("****** Register *******")

    email = input("Enter your email address? \n")
    first_name = input("Enter your first name? \n")
    last_name = input("Enter your last name? \n")
    password = input("create a password for yourself \n")

    accountNumber = generationAccountNumber()

    database[accountNumber] = [ first_name, last_name, email, password ]

    print("Your Account Has been created Succssfully")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")
    print("                           ")
    print("                           ")
    login()

def generationAccountNumber():

    return random.randrange(1111111111,9999999999)

def login():
    
    print("********* Login ***********")

    accountNumberFromUser = int(input("Enter your account number? \n"))
    password = input("Enter your password \n")

    for accountNumber,userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                e = datetime.now()
                dt_string = e.strftime("%d/%m/%Y at %H:%M:%S")
                # prints current date and time and a welcome message for the user
                print("You logged in on", dt_string)
                bankOperation(userDetails)
               
                
   # print('Invalid account or password')
    print("                           ")
    print("                           ")
    login()

def bankOperation(user):

    print("Welcome %s %s " % ( user[0], user[1] ) )

    selectedOption = int(input("These are the available options:\n (1) Deposit\n (2) Withdrawal\n (3) Complaint\n (4) Logout\n (5) Exit \n"))

    if(selectedOption == 1):
        depositOperation()
        
    elif(selectedOption == 2):
         withdrawalOperation()
         
    elif(selectedOption == 3):
        complaintOperation()
        
    elif(selectedOption == 4):
        logout()
        
    elif(selectedOption == 5):
        exit()
        
    else:
      
        print("Invalid option selected")
        bankOperation(user)

def withdrawalOperation():
    witdrawal=float(input('How much would you like to withdraw($)?\n'))
    balance = 20000
    if (witdrawal > balance):
        print('insufficiant funds\n')
        print('Please, try again')
    else:
        print('Take your cash')

def depositOperation():
    balance = 0
    deposit=float(input('How much would you like to deposit($)?\n'))
    currentBalance = deposit + balance
    print('Your Current Balance: $%s' % currentBalance)

def logout():
    print("                           ")
    print("                           ")
    login()

def complaintOperation():
    complaint=input('What issue would you like to report?\n')
    print('\nThank you for contacting us.')

init()



