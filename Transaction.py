
from CreateAccount  import CreateAccount

class Transaction(CreateAccount):
    def __init__(self):
        super().__init__()
      
    
    def login(self, name , ph , password):
        with open(rf"\Users\hp\Desktop/100DaysOfCode by Angela Yu\updated banking sytem/{name}.txt","r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in str(self.client_details_list):
                if str(password) in str(self.client_details_list):
                        self.loggedin = True
        
            if self.loggedin == True:
                print(f"{name} logged in")
                self.cash = int(self.client_details_list[3])
                self.name = name
            else:
                print("Wrong details")
                print("Please reload to login again")


    def Deposit(self, amount):
        if amount > 0:
            self.cash += amount
            name=self.name
            with open(rf"\Users\hp\Desktop/100DaysOfCode by Angela Yu\updated banking sytem/{name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")
            
            with open(rf"\Users\hp\Desktop/100DaysOfCode by Angela Yu\updated banking sytem/{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(self.cash)))

            print("Amount added successfully")

        else:
            print("Enter correct value of amount")

    def Transfer(self, amount , name ,ph):
        with open(rf"\Users\hp\Desktop/100DaysOfCode by Angela Yu\updated banking sytem/{name}.txt","r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in self.client_details_list:
                self.TranferCash = True

        
        if self.TranferCash == True:
            total_cash = int(self.client_details_list[3]) + amount
            left_cash = self.cash - amount
            with open(rf"\Users\hp\Desktop/100DaysOfCode by Angela Yu\updated banking sytem/{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(total_cash)))

            with open(rf"\Users\hp\Desktop/100DaysOfCode by Angela Yu\updated banking sytem/{self.name}.txt","r") as f:
                details_2 = f.read()
                self.client_details_list = details_2.split("\n")
            
            with open(rf"\Users\hp\Desktop/100DaysOfCode by Angela Yu\updated banking sytem/{self.name}.txt","w") as f:
                f.write(details_2.replace(str(self.client_details_list[3]),str(left_cash)))

            print("Transfer Successfully to",name,"-",ph)
            print("Balacne: =",left_cash)
            self.cash = left_cash

    def withdraw(self,amount,name):
        self.TranferCash=True     
        if self.TranferCash == True:
            left_cash = self.cash - amount

            with open(rf"\Users\hp\Desktop/100DaysOfCode by Angela Yu\updated banking sytem/{name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")
            
            with open(rf"\Users\hp\Desktop/100DaysOfCode by Angela Yu\updated banking sytem/{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(left_cash)))
                
            print("ًWithdraw Successful")
            print("Balacne: =",left_cash)
            self.cash = left_cash
   



        