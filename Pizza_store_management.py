#write a python program that handles pizzeria customers and at the end of day show the 
# full day report(like total earning of day,pizza earning, pasta earning etc..)

import os
os.system('cls')
from decimal import Decimal
from datetime import datetime

class Pizzeria:
    shift=0
    def __init__(self):
        print("'Welcome to Amazing Pizza and Pasta Store-Pizzeria'".center(160)) ;print()
        self.pizza_earning=0
        self.pasta_earning=0
        self.full_day_earning=0
        self.full_day_quantity=0
        self.soft_drink=0
        self.bruschetta=0
        self.brownies=0
    
    def showPizza(self,price):
        self.price=price
        print("Get 1 large pizza @",self.price,"AUD")
        print("Get 2 large pizza @",self.price+10,"AUD")
        print("Get 3 large pizza @",self.price+19,"AUD")
        print('***Buy 4 or more pizza and get 1.5lt of soft drink free***');print()

    def showPasta(self,price):
        self.price=price
        print("Get 1 large pasta @",self.price,"AUD")
        print("Get 2 large pasta @",self.price+Decimal('7.5'),"AUD")
        print("Get 3 large pasta @",self.price+18,"AUD")
        print('***Buy 4 or more pastas and get 2 bruschetta free.***')
        print('***Buy 4 or more pizzas and pastas and get 2 chocco brownies ice cream free.');print()
        print('--------------------------------------------------------------------------------------')
    
    def pizzaChoice(self,price):
        self.price=price
        self.pizza_quantity=int(input("Enter number of pizza, you want to order:"))
        if self.pizza_quantity==1:
            return self.price
        elif self.pizza_quantity==2:
            return self.price+10
        elif self.pizza_quantity==3:
            return self.price+19
        else:
            return self.price*self.pizza_quantity #,"\n*** Congratulations !! 1.5lt softdrink free *** "

    def pastaChoice(self,price):
        self.price=price
        print()
        self.pasta_quantity=int(input("Enter number of pasta, you want to order:"))
        if self.pasta_quantity==1:
            return self.price
        elif self.pasta_quantity==2:
            return self.price+Decimal('7.5')
        elif self.pasta_quantity==3:
            return self.price+18
        else:
            return self.price*self.pasta_quantity 
    
    def main(self):
        print("Press 1 to order food and 2 for quit")
        choice=int(input("Enter your choice:"));print()
        if choice==1:
            status=True
            while status:
                self.name=input("Enter Your Good name: ")
                print("Welcome",self.name);input()

                obj.showPizza(Decimal('10.99'))       # showPizza method called
                obj.showPasta(Decimal('9.50'))         # showPasta method called

            
                pizzaNetTotal=obj.pizzaChoice(Decimal('10.99'))         #pizzaChoice method is called
                print("Your Pizza Order Amount is:",pizzaNetTotal,"AUD");print()
                if self.pizza_quantity>3:
                    print('*** Congratulations !! 1.5lt softdrink free ***')
                    self.soft_drink+=1

                pastaNetTotal=obj.pastaChoice(Decimal('9.5'))           #pizzaChoice method is called    
                print("Your Pasta Order Amount is:",pastaNetTotal,"AUD");print()
                if self.pasta_quantity>3:
                    print('*** Congratulations !! get 2 bruschetta free ***')
                    self.bruschetta+=2
                    
                if self.pizza_quantity>3 and self.pasta_quantity>3:
                    print('*** Congratulations !! get 2 chocco brownies ice cream free *** ')
                    self.brownies+=2

                print("Your Total Order Amount is:",pizzaNetTotal+pastaNetTotal,"AUD");print()
                print('--------------------------------------------------------------------------------------')

                self.pizza_earning+=pizzaNetTotal                               #Total pizza earning of the day
                self.pasta_earning+=pastaNetTotal                               #Total pizza earning of the day
                self.full_day_earning+=(pizzaNetTotal+pastaNetTotal)             #total earning of the day
                self.full_day_quantity+=(self.pizza_quantity+self.pasta_quantity) #total quantity pizza+pasta sold in a day

                allow_next=input("Do you want to allow next customer to enter into pizzaria? Press 'y' for Yes and 'n' for No:").lower()
                if allow_next=='n':
                    status=False
        elif choice==2:
            print("You choosed, not to order from pizzeria!")

    def show_bill(self):
        
        print()
        n1="<<<<<<<<<<<<<<<<<<<<< Pizza & Pasta Bill >>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        n00=" "
        n2="Total Earning of the day: "+ str(self.full_day_earning) +"AUD"
        n3="Payment Received from Pizza: "+str(self.pizza_earning)+"AUD"
        n4="Payment Received from Pasta: "+str(self.pasta_earning)+"AUD"
        n5="Total number of Pizza & Pasta sold in a day: "+str(self.full_day_quantity)
        n6="Total Number of 1.5lt soft drink bottles given: "+str(self.soft_drink)
        n7="Total Number of bruschetta given to customer: "+str(self.bruschetta)
        n8="Total Number of chocco brownies with ice cream given to customer: "+str(self.brownies)
        n01=" "
        n9="------------------------------------END----------------------------------------"
        self.l1=[n1,n00,n2,n3,n4,n5,n6,n7,n8,n01,n9]
        for i in self.l1:
            print(i)

    def print_bill(self):
        
        #obj.shift+=1
        current_Dt_Time = datetime.now()
        dt_time_format = current_Dt_Time.strftime("%d-%m-%Y   %H:%M:%S")
        today=dt_time_format[:10]                      #Displays today's date

        if not os.path.exists("Pizzeria_Database"):
            os.mkdir("Pizzeria_Database")
    
        with open('Pizzeria_Database/'+str(today)+'.txt','a+') as f:
            f.write("%s\n"%dt_time_format)
            #f.write("%s\n"%('Shift: '+str(obj.shift)))
            l1=map(lambda x:x+'\n', self.l1)
            f.writelines(l1)
            


obj=Pizzeria()
obj.main()
obj.show_bill()
obj.print_bill()

print("Thank You!! ")
