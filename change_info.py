from CreateAccount import CreateAccount
from Transaction import Transaction


class Change_info(CreateAccount):
    def __init__(self):
        super().__init__()

    def password_change(self,password,name):
        if len(password) < 5 or len(password) > 18:
            print("Enter password greater than 5 and less than 18 character")
        else:
            with open(rf"\Users\hp\Desktop/100DaysOfCode by Angela Yu\updated banking sytem/{name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(rf"\Users\hp\Desktop/100DaysOfCode by Angela Yu\updated banking sytem/{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[2]),str(password)))
            print("new Password set up successfully")

    

    def ph_change(self,ph,name):
        if len(str(ph)) > 12 and len(str(ph)) < 10:
            print("Invalid Phone number ! please enter 10 digit number")
        else:
            with open(rf"\Users\hp\Desktop/100DaysOfCode by Angela Yu\updated banking sytem/{name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")
                

            with open(rf"\Users\hp\Desktop/100DaysOfCode by Angela Yu\updated banking sytem/{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[1]),str(ph)))
            print("new Phone number set up successfully")
