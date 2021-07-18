

import os
os.system('cls')
from datetime import datetime

class Product_Manager:
    
    m_stock=90                 #Existing Stock
    l_stock=70
    c_stock=30
    m_unit_price=20000
    l_unit_price=60000
    c_unit_price=40000
    m_stock_price=m_stock*m_unit_price
    l_stock_price=l_stock*l_unit_price
    c_stock_price=c_stock*c_unit_price
    

    def file_data(self):
        f=open('chrom.txt','w+')
        current_Dt_Time = datetime.now()
        dt_time_format = current_Dt_Time.strftime("%d-%m-%Y   %H:%M:%S")
        f.write("%s\n"%dt_time_format)
        n1="Sr. No.  product    stock    Per Unit Cost  Each stock total Price"
        n2="\n1        Mobile     "+str(self.m_stock)+'       '+str(self.m_unit_price)+'          '+str(self.m_stock_price)
        n3="\n2        Laptop     "+str(self.l_stock)+'       '+str(self.l_unit_price)+'          '+str(self.l_stock_price)
        n4="\n3        Computer   "+str(self.c_stock)+'       '+str(self.c_unit_price)+'          '+str(self.c_stock_price)
        self.product_list=[n1,n2,n3,n4]
        for i in self.product_list:
            f.write(i)
       
    def add_Product(self):
        while True:
            print("Which item do you want to add to stock? \nPress '1' for Mobile \n      '2' for laptop \n      '3' for Computer")
            choice=int(input("Enter your choice: "))
            if choice==1:
                m_add=int(input("Enter number of Mobile unit you want to add into existing stock:"))
                self.m_stock+=m_add
                self.m_stock_price=self.m_stock*self.m_unit_price
                print("Total Mobile Unit Available in stock after updation: ",self.m_stock)
                print(f"Total Mobile stock Price after updation: {self.m_stock_price} INR ({self.m_unit_price} INR/Unit)")

            elif choice==2:
                l_add=int(input("Enter number of Laptop unit you want to add into existing stock:"))
                self.l_stock+=l_add
                self.l_stock_price=self.l_stock*self.l_unit_price
                print("Total Laptop Unit Available in stock after updation: ",self.l_stock)
                print(f"Total Laptop stock Price after updation: {self.l_stock_price} INR ({self.l_unit_price} INR/Unit)")
                
            elif choice==3:
                c_add=int(input("Enter number of Computer unit you want to add into existing stock:"))
                self.c_stock+=c_add
                self.c_stock_price=self.c_stock*self.c_unit_price
                print("Total Computer Unit Available in stock after updation: ",self.c_stock)
                print(f"Total Computer stock Price after updation: {self.c_stock_price} INR ({self.c_unit_price} INR/Unit)")
            
            else:
                print("Sorry!Invalid Input Entered!")
            
            print('----------------------------------------------------------------------')
            choice=input("Do you want to continue to add item?:Press 'y' for Yes and 'n' for No: ").lower()
            if choice=='n':
                break
        obj2.file_data()          #Updated stock(After Adding item .txt file should be updated. so,if we view stock detail it will fetch updated data from .txt file)


    def view_stock(self):
        for i in self.product_list:          #try---->f.read
            print(i)
        print('----------------------------------------------------------------------')
        print("-".center(30,"-"))
    def select_choice(self):
        while True:
            print("Select Your Choice: \nPress '1' to Add Products \n      '2' to View Stock Details")
            choice=int(input("Enter Your Choice: "));print('----------------------------------------------------------------------')
            if choice==1:
                obj2.add_Product()
            elif choice==2:
                obj2.view_stock()
            choice=input("Have you forgotten to View stock list or Add Item? Press 'y' to continue and 'n' to exit")
            if choice=='n':
                break
        
#obj=Product_Manager()
#obj.file_data()         #Existing stock data
#obj.select_choice()

class Customer(Product_Manager):
    
    def __init__(self):
        pass
        #self.m_quantity=0
        #self.m_quantity=0
        #self.c_quantity=0

    def view_product(self):
        Product_Manager.view_stock(self)       #Method Over-riding
    
    def view_and_buy(self):
        while True:
            print("List of Products Available")
            Customer.view_stock(self)
            choice=int(input("Which product do you want to buy?:\nPress '1' to Buy Mobile \n      '2' to Buy Laptop\n      '3' to buy Computer"))
            if choice==1:
                print("Mobile Price per Unit is: ",self.m_unit_price,"INR")
                self.m_quantity=int(input("Howmany Mobiles do you want to purchase?: "))
                if self.m_stock>=self.m_quantity:
                    self.m_stock-=self.m_quantity                                 #It updates mobile stock after purchase 
                    self.m_stock_price=self.m_stock*self.m_unit_price             #It updates mobile stock price after purchase
                    self.m_order_price=self.m_unit_price*self.m_quantity
                    print(f"Your Mobile Purchse bill for {self.m_quantity} is {self.m_order_price} INR")
                else:
                    print("Sorry! Out Of Stock!!")

            elif choice==2:
                print("Laptop Price per Unit is: ",self.l_unit_price,"INR")
                self.l_quantity=int(input("Howmany laptops do you want to purchase?: "))
                if self.l_stock>=self.l_quantity:
                    self.l_stock-=self.l_quantity 
                    self.l_stock_price=self.l_stock*self.l_unit_price
                    self.l_order_price=self.l_unit_price*self.l_quantity
                    print(f"Your Laptop Purchse bill for {self.l_quantity} is {self.l_order_price} INR")
                else:
                    print("Sorry! Out Of Stock!!")

            elif choice==3:
                print("Computer Price per Unit is: ",self.c_unit_price,"INR")
                self.c_quantity=int(input("Howmany Computers do you want to purchase?: "))
                if self.c_stock>=self.c_quantity:
                    self.c_stock-=self.c_quantity 
                    self.c_stock_price=self.c_stock*self.c_unit_price
                    self.c_order_price=self.c_unit_price*self.c_quantity
                    print(f"Your Computer Purchse bill for {self.c_quantity} is {self.c_order_price} INR")
                else:
                    print("Sorry! Out Of Stock!!")
            choice=input("Do you want to continue to buy Product?:Press 'y' for Yes and 'n' for No: ").lower()
            obj2.file_data()
            if choice=='n':
                break
        
    def select_choice(self):
        while True:
            print("Select Your Choice: \nPress '1' to View Products \n      '2' to View and Buy Products")
            choice=int(input("Enter Your Choice: "));print('----------------------------------------------------------------------')
            if choice==1:
                obj2.view_product()
            elif choice==2:
                obj2.view_and_buy()
            choice=input("Have you forgotten to Buy product or view product list? Press 'y' to continue and 'n' to exit")
            if choice=='n':
                break

class Menu(Customer,Product_Manager):
    def __init__(self):
        print("'Welcome to Chroma'".center(160)) ;print()

    def main_menu(self):
        while True:
            choice=int(input("Select your role: \nPress '1' For Product Manager \n      '2' for Customer\n:"))
            print('----------------------------------------------------------------------')
            if choice==1:
                obj2.file_data()
                Product_Manager.select_choice(self)

            elif choice==2:
                obj2.file_data()         #Existing data store
                Customer.select_choice(self)
            choice=input("Do you want to continue as Customer/Product-Manager? Press 'y' to continue and 'n' to exit")
            if choice=='n':
                break
obj2=Menu()
obj2.main_menu()
