from CreateAccount  import CreateAccount
from Transaction  import Transaction
from change_info import Change_info



print("Welcome to my Bank")
print("1.Login")
print("2.Creata a new Account")
user = int(input("Take an action: "))

transaction=Transaction()
change_details=Change_info()
bank=CreateAccount()


if user==1:
    print("Logging in")
    name = input("Enter  Registered Name: ")
    ph = int(input("Enter registered Phone Number: "))
    password = input("Enter password: ")
   
    try:
        with open(rf"\Users\hp\Desktop/100DaysOfCode by Angela Yu\updated banking sytem/{name}.txt","r") as file:
            file.read ()
    except FileNotFoundError:
        print("This is not the registered name!!!")
        print("please reload to login")
    else:
        transaction.login(name,ph,password)


    while True:
        if transaction.loggedin:
            print("1.Check Balcane")
            print("2.Deposit")
            print("3.Tranfer amount")
            print("4.Withdraw")
            print("5.Edit profile")
            print("6.Logout")
            login_user = int(input())
            if login_user == 1:
                print("Balacne =",transaction.cash)
                print("\n1.back menu")
                print("2.Logout")
                choose = int(input())
                if choose == 1:
                    continue
                elif choose == 2:
                    break
            elif login_user == 2:
                print("Balance =",transaction.cash)
                amount = int(input("Enter amount: "))
                transaction.Deposit(amount)
                print("\n1.back menu")
                print("2.Logout")
                choose = int(input())
                if choose == 1:
                    continue
                elif choose == 2:
                    break
            elif login_user == 3:
                print("Balance =",transaction.cash)
                amount = int(input("Enter amount: "))
                if amount >= 0 and amount <= transaction.cash:
                    name = input("Enter person name: ")
                    ph = input("Enter person phone number: ")
                    transaction.Transfer(amount,name,ph)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
                elif amount < 0 :
                    print("Enter please correct value of amount")

                elif amount > bank.cash:
                    print("Not enough balance")

            elif login_user == 4:
                print("Balance =",transaction.cash)
                amount = int(input("Enter amount: "))
                if amount >= 0 and amount <= transaction.cash:
                  
                    transaction.withdraw(amount,name)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
                elif amount < 0 :
                    print("Enter please correct value of amount")

                elif amount > bank.cash:
                    print("Not enough balance")

            elif login_user == 5:
                print("1.Password change")
                print("2.Phone Number change")
                edit_profile = int(input())
                if edit_profile == 1:
                    new_password =input("Enter new Password: ")
                    change_details.password_change(new_password,name)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
                elif edit_profile == 2:
                    new_ph = int(input("Enter new Phone Number: "))
                    change_details.ph_change(new_ph,name)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
            elif login_user==6:
                    break

elif user==2:
    print("Creating a new  Account")
    name = input("Enter Name: ")
    ph = int(input("Enter Phone Number: "))
    password = input("Enter password: ")
    bank.register(name, ph, password)



