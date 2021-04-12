from datetime import datetime
import random
allowedUsers = ["Seyi", "Mike", "Love"]
allowedPassword = ["passwordSeyi", "passwordMike", "passwordLove"]
def init():
    print("Welcome to Brabus Bank")
    isanaccountholder = input("Do you have an account with us? \n"
                              " YES/NO \n")
    if isanaccountholder.lower() == "yes"  :
        login()

    elif isanaccountholder.lower() == "no" :
        print("You'll have to register now\n kindly provide your details")
        register()
        login()
        transaction()
    else :
        print("Enter a valid input")
        init()



    #login
def login():
    name = input("Input your Username \n")

    if name in allowedUsers:
        password = input("Input your password \n")
        userId = allowedUsers.index(name)
        if password == allowedPassword[userId]:
            print("Welcome %s " % name)
            print ("You have sucessfully logged into Brabus Bank,Allen Avenue on \n" + datetime.today().strftime('%Y-%m-%d-%H:%M:%S') + "\n")
            print("Your account number is " + str(generateAccountNumber()) + "\n")

            transaction()

    else:
        print("Access Denied. \n"
              "Please enter a valid user")
        init()

    #transaction
def transaction():
    print("1. Withdrawal")
    print("2. Cash Deposit")
    print("3. Lodge a complain ")
    print("4. Transfer \n ")

    selectOption = int(input("Please choose your activity \n"))
    balance = 30000000000
    if selectOption == 1:
        print("Your account balance is \n" + "₦" + str(balance) + "\n")
        print("How much would you like to withdraw?\n")
        amount = int(input("Enter amount\n"))
        if amount <= balance:
            accountBalance = balance - amount
            # print("machine counts with the sound prrrrrrrrr")
            print("Take your cash \n")
            print('Your account balance is ' + '₦' + str(accountBalance) + " \n")
            print("Thank you for banking with us")
        else:
            print("insufficient fund")
    elif selectOption == 2:
        deposit = int(input("How much would you like to deposit \n"))
        currentBalance = int(deposit + balance)
        print("Your current balance is \n " + "₦" + str(currentBalance) + " \n Thank you for banking with us")
    elif selectOption == 3:
        complain = input("What issue would you like to report? \n")
        print("Thank you for contacting us")
    elif selectOption == 4:
        receiverBank = input("Select the receiving bank ")
        receiverAccountNo = input("Input transfer destination account ")
        transferAmount = input("Input amount to transfer")
        confirmation = input("Are you sure you want to send " + str(transferAmount) + " to " + str(receiverAccountNo) + " ?\n"
              "YES or NO \n")
        if confirmation.lower() == "yes" :
            print( "You have sucessfully transferred "+ str(transferAmount) + str(receiverAccountNo))
            print(" Your new account balance is " + str((balance - int(transferAmount))) )

        elif confirmation.lower() == "no":
            print("Transfer has been cancelled")
            transaction()

    else:
        print('Please input a valid key')

    #register
def register():
    username = input("Input your username \n")
    allowedUsers.append(username)
    email = input("Enter your email \n")
    password = input("Enter your password \n")
    allowedPassword.append(password)
    print("Account created successfully \n"
          "Please login to continue \n")


    #Create Account Number
def generateAccountNumber():

    return random.randrange(1111111111,9999999999)



init()