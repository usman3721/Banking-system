class CreateAccount:
    def __init__(self):
        self.client_details_list = []
        self.loggedin = False
        self.cash = 100
        self.TranferCash = False

    def register(self, name , ph , password):
        cash = self.cash
        contitions = True
        if len(str(ph)) > 11 or len(str(ph)) < 10:
            print("Invalid Phone number ! please enter 10 digit number")
            contitions = False

        if len(password) < 5 or len(password) > 18:
            print("Enter password greater than 5 and less than 18 character")
            contitions = False  
        
        if contitions == True:
            print("Account created successfully")
            self.client_details_list = [name , ph , password , cash]
            with open(f"{name}.txt","w") as f:
                for details in self.client_details_list:
                    f.write(str(details)+"\n")

            print("Your registered Account name is",name)
            print("Your registered phone number is",ph)


# C:\Users\hp\Desktop\100DaysOfCode by Angela Yu\updated banking sytem
