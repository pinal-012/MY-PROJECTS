class Atm_manager:

    dictAtmBalance={2000:2, 500:4, 200:5, 100:10, 50:20, 20:100, 10:100, 5:20, 2:50, 1:100} #initial atm balance
    atm_Balance=0
    amount=0
    for i in dictAtmBalance:
        atm_Balance+=dictAtmBalance[i]*i
    
    def viewBalance(self):
        self.atm_Balance=0
        for i in self.dictAtmBalance:
            print(f"{i} X {self.dictAtmBalance[i]} = {i*self.dictAtmBalance[i]}")
            self.atm_Balance+=(i*self.dictAtmBalance[i])
        print(f"Total Balance: {self.atm_Balance} Rs.");print("-".center(50,"-"))
    
    def autoDeposit(self):
        self.amount=int(input("Howmuch amount do you want to deposit?"))
        currency={2000:0, 500:0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}
        rem_of_notes=0
        for i in currency:
            currency_part=self.amount//10  
            rem_of_currency_part=self.amount%10
            notes = currency_part//i
            rem_of_notes+=currency_part%i
            currency.update({i : notes}) 
            notUpdatedCurrency=rem_of_currency_part+rem_of_notes 
        for i in currency:      
            pendingNotes=notUpdatedCurrency//i
            notUpdatedCurrency=notUpdatedCurrency-(pendingNotes*i)      #remainder of pendingNotes
            currency[i]+=pendingNotes

        print("Your Deposited Amount:",self.amount)
        for i in currency:
            print(f"{i} X {currency[i]} = {i*currency[i]}")
            self.dictAtmBalance[i]+=currency[i]         #Existing notes are updated with deposited notes
               
    def deposit(self):
        self.amount=int(input("Howmuch amount do you want to deposit?"))
        deposit_amount=0
        currency={2000:0, 500:0, 200:0, 100:0, 50:0, 20:0, 10:0, 5:0, 2:0, 1:0}

        for i in currency:
            list_quantity=[]
            print("Quantity of",i, "Notes:  ");quantity=int(input())
            list_quantity.append(quantity)
            deposit_amount+=(quantity*i)
            currency[i]=quantity                           #Dict currency is updated with customer entered quantity
            #self.dictAtmBalance[i]+=quantity             #Existing notes are updated with deposited notes
            
            if deposit_amount==self.amount:
                print("Your Deposited Amount:",deposit_amount)
                for i in currency:
                    print(f"{i} X {currency[i]} = {i*currency[i]}")
                    self.dictAtmBalance[i]+=currency[i]         #Existing notes are updated with deposited notes
                break
            elif deposit_amount>self.amount:
                print(f"Sorry! Please Try Again!! You have entered {deposit_amount-self.amount} Rs. more.")
                break
        if deposit_amount<self.amount:
            print(f"Sorry! Please Try Again!! You have entered {self.amount-deposit_amount} Rs. less.")
            
        
    def select_choice(self):
        while True:
            print("Select Your Choice: \nPress '1' to View ATM Balance \n      '2' to Deposit Amount\n      '3' to Deposit Particular Notes \n      '4' to Exit: ")
            choice=int(input("Enter Your Choice: "));print("-".center(50,"-"))
            if choice==1:
                Atm_manager.viewBalance(self);print("-".center(50,"-"))
            elif choice==2:
                Atm_manager.autoDeposit(self)
            elif choice==3:
                Atm_manager.deposit(self)
            elif choice==4:
                break
            else:
                print("Invalid Choice")

class Customer(Atm_manager):
    customer_balance=100000

    def deposit(self):
        Atm_manager.deposit(self)
        self.customer_balance+=self.amount

    def money_withdraw(self):
        self.withdraw=int(input("Enter an amount that you want to withdraw: "))
        if self.withdraw<=self.customer_balance:
            if self.withdraw<=self.atm_Balance:
                self.customer_balance-=self.withdraw
                for i in self.dictAtmBalance:     #dict is used only to get key i.e. 2000,500,200 etc..
                    note=self.withdraw//i
                    if note<=self.dictAtmBalance[i]:       #to check whether atm has quantity of particular currency
                        self.withdraw=self.withdraw-(note*i)
                        print(f"{i} X {note} = {i*note}")
                        self.dictAtmBalance[i]-=note      #atm balance is updated after withdraw
                    else:                                 #if atm has not sufficient particular currency,existing quantity is used for withdraw and loop forward.
                        self.withdraw=self.withdraw-(self.dictAtmBalance[i]*i)      
                        print(f"{i} X {self.dictAtmBalance[i]} = {i*self.dictAtmBalance[i]}")
                        self.dictAtmBalance[i]=0

                print("Please Collect Your Card and Amount!")
                print("Your remaining balance is: ",self.customer_balance);print("-".center(50,"-"))
            else:
                print("Sorry! Try Again to withdraw some lesser amount")
        else:
            print("Sorry! Not enough balance!! You need",self.withdraw-self.customer_balance,"Rs more!")
    
    def select_choice(self):
        while True:
            print("Select Your Choice: Press \n\t'1 to View your Bank Balance \n\t'2' to Withdraw Amount \n\t'3' to Deposit Amount \n\t'4' to Exit")
            choice=int(input("Enter Your Choice: "));print("-".center(50,"-"))
            if choice==1:
                print("Your Bank Balance is:",self.customer_balance,"Rs.");print("-".center(50,"-"))
            elif choice==2:
                obj1.money_withdraw()
            elif choice==3:
                obj1.deposit()
            elif choice==4:
                break
            else:
                print("Invalid Choice")

class Menu(Customer,Atm_manager):
    def __init__(self):
        print("'Welcome to HDFC Bank ATM'".center(110,"-")) ;print()

    def main_menu(self):
        while True:
            print("Select Your Role: \nPress '1' For ATM Manager \n      '2' For Customer \n      '3' to Exit")
            choice=int(input("Enter Your Choice: "));print("-".center(50,"-"))
            if choice==1:
                Atm_manager.select_choice(self)
            elif choice==2:
                obj1.select_choice()
            elif choice==3:
                break
            else:
                print("Invalid Choice")
            choice=input("Do you want to continue as Customer/ATM-Manager? Press 'y' to continue and 'n' to exit: ")
            if choice=='n':
                break

obj1=Menu()
obj1.main_menu()
print("Thank you for Visiting HDFC Bank ATM!!")