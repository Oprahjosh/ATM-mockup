from datetime import datetime
name = input("Input your Username \n")

allowedUsers = ["Seyi","Mike","Love"]
allowedPassword = ["passwordSeyi","passwordMike","passwordLove"]

if name in allowedUsers:
    password = input("Input your password \n")
    userId = allowedUsers.index(name)
    if password == allowedPassword[userId]:
        print("Welcome %s " % name)
        print ("You have sucessfully logged into Brabus Bank,Allen Avenue on \n" + datetime.today().strftime('%Y-%m-%d-%H:%M:%S') + "\n")

        print ("1. Withdrawal")
        print ("2. Cash Deposit")
        print ("3. Lodge a complain \n")

        selectOption = int(input("Please choose your activity \n"))
        balance = 30000000000
        if selectOption == 1 :
            print ( "Your account balance is \n"+ "₦" + str(balance) +"\n")
            print("How much would you like to withdraw?\n")
            amount = int(input("Enter amount\n"))
            if amount <= balance :
                accountBalance = balance - amount
                #print("machine counts with the sound prrrrrrrrr")
                print ( "Take your cash \n")
                print ('Your account balance is ' + '₦' + str(accountBalance) + " \n")
                print ("Thank you for banking with us")
            else:
                print ("insufficient fund")
        elif selectOption == 2 :
            deposit = int(input("How much would you like to deposit \n"))
            currentBalance = int(deposit + balance)
            print("Your current balance is \n " + "₦"+ str(currentBalance) + " \n Thank you for banking with us" )
        elif selectOption == 3 :
            complain = input("What issue would you like to report? \n")
            print("Thank you for contacting us")
        else:
            print ('Please input a valid key')
            