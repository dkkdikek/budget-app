

class Category:
    #class that tracks the budget of a specific category such as food, clothing or entertainment
    
    def __init__(self,name):
        # name -string- name of the budget
        # balance -float- budget amount(current total)
        # ledger -list of dictionaries- records the deposits and withdraws, the key "amount" holds the amount 
        # and the key "description" holds the description
        self.name=name
        self.balance=0
        self.ledger=[]

    def check_funds(self,amount):
        # methode that compares an amount with the current balance
        # input : amount -float- amount that needs to be compared with the balance
        # output: True if the amount is <= than the balance
        #         False if the amount is > then the balance
        if amount > self.balance:
            return False
        elif amount <= self.balance:
            return True

    def __str__(self):
        display=self.name.center(30,"*") + "\n"
        for item in self.ledger:
            row = item["description"][:23] + (30 - len(item["description"][:23]) - len(str("{:.2f}".format(item["amount"]))) )*" " + str("{:.2f}".format(item["amount"]))+"\n"
            display+= row
        display += "Total: " + str(self.balance)
        return display

    def deposit(self,amount,description=""):
        # method that accepts an amount and a description in order to deposit into the budget
        # input : amount - float, cannot be < 0 
        #         description - optional argument, if empty will default to an empty string
        self.balance+=amount
        self.ledger.append({"amount":amount,"description":description})


    def withdraw(self,amount,description=""):
        # method that accepts an amount and a description in order to withdraw from the budget
        # input : amount - float, cannot be < 0 
        #         description - optional argument, if empty will default to an empty string
        # the amount will be stored as a negative number in the ledger
        # this method uses the __checkfunds__ method in order to check if the withdraw is possible
        if self.check_funds(amount) is True:
            self.balance-=amount
            self.ledger.append({"amount":amount * -1,"description":description})
            return True
        else:
            return False


    
    def get_balance(self):
        return self.balance

    def transfer(self,amount,reciever):
        if self.check_funds(amount) is True:
            self.balance-=amount
            self.ledger.append({"amount":amount * -1,"description":"Transfer to "+ reciever.name})
            reciever.deposit(amount,"Transfer from "+self.name)
            return True
        else:
            return False


def create_spend_chart(lista):
    # function that creeates a bar chart of the spendings of all the budgets and shows the % of
    #  each specific budget contribution to the total spendings
    # input : a list of budgets
    # output: the bar chart 

    #list of each budget
    budgets={}
    #the total amout of spendings
    total=0
    #the building block of the final chart
    display=""
    
    
    for item in lista:
        budgets[item.name.capitalize()]=0
        for transaction in item.ledger:
            if transaction["amount"]<0:
                budgets[item.name]+= transaction["amount"] * -1
                total+=transaction["amount"]*-1

    for key in budgets:
        budgets[key]=(budgets[key] / total * 100)/10
        budgets[key]=int(budgets[key])*10
    display+="Percentage spent by category\n"
    for x in range(100, -1, -10):
        bar=""
        for key in budgets:
            if budgets[key] >= x:
                bar+=" o "
            else:
                bar+="   "
        line=(3-len(str(x))) * " "+ str(x) +"|" + bar + " \n"
        display+=line
    cut="    "+ len(budgets) * "---" + "-"
    display+=cut
    breakPP=True
    counter=0
    while breakPP:
        row="    "
        breakPP=False
        for key in budgets:
            if len(key)-1>=counter:
                row+=" " + key[counter] + " "
                breakPP=True
            else:
                row+="   "
        
        if breakPP:
            display+=" \n"+row if counter > 0 else "\n"+row
        counter+=1
    display+=" "
    return display

        
            



        

    


