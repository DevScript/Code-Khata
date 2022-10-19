class cart:
    def __init__(self,area,menu,df,excel,delivery_address,customer_name,phone_no,payment_type,rider_name,rider_phone,no_plate):
        self.area=area
        self.menu=menu
        self.df=df
        self.excel=excel
        self.delivery_address=delivery_address
        self.customer_name=customer_name
        self.phone_no=phone_no
        self.payment_type=payment_type
        self.rider_name=rider_name
        self.rider_phone=rider_phone
        self.no_plate=no_plate
    def your_cart(self):
        rst=str(input("Enter Restaurant Name:"))
        rst=rst.upper()
        for x,y in self.area.items():
            if  self.delivery_address in x:
                itm=int(input("Enter Total Dishes You want: "))
                for i in range(itm):
                    order=str(input("Enter Order With Qty: "))
                    num=order[0:1]
                    qty=int(num)
                    lst=[0,1,2,3,4,5,6,7,8,9]
                    if qty not in lst:
                        print("You have entered qty in a wrong way!")
                    food=order[2:]
                    string=str(food)
                    string=string.title()
                    a=excel["Qty"]
                    a.append(num)
                    b=excel["Food"]
                    b.append(string)
                    c=menu[rst][string]
                    d=excel["Price"]
                    d.append(c)
                    price=c*qty
                    f=excel["Price with Quantity"]
                    f.append(price)
                ask3=str(input("Order Confirm Write Yes or No: "))
                ask3=ask3.title()
                if ask3=="No":
                    z=int(input("How many items you want to remove from it: "))
                    for i in range(z):
                        order=str(input("Enter Removing Order With Qty: "))
                        num=order[0:1]
                        qty=int(num)
                        lst=[0,1,2,3,4,5,6,7,8,9]
                        if qty not in lst:
                            print("You have entered qty in a wrong way!")
                        food=order[2:]
                        string=str(food)
                        string=string.title()
                        a=excel["Qty"]
                        a.remove(num)
                        b=excel["Food"]
                        b.remove(string)
                        c=menu[rst][string]
                        d=excel["Price"]
                        d.remove(c)
                        price=c*qty
                        f=excel["Price with Quantity"]
                        f.remove(price)
                        f=excel["Price with Quantity"]
                        self.df=pd.DataFrame.from_dict(excel)
                offer=str(input("enter is it your first order: "))
                if offer=="yes":
                    price=c*qty
                    tax=price*0.13 
                    final_price=price+tax
                    discount=final_price-0.2
                    import time
                    from datetime import datetime 
                    now=datetime.now()
                    time=now.strftime("%H:%M%p")
                    date=now.strftime("%m/%d/%Y")
                    day=now.strftime("%a")
                    print("-"*20+"RIDER DETAILS"+"-"*20)
                    print("your rider name is\t\t\t"+str(self.rider_name))
                    print("-"*30+"-"*30)
                    print("rider phone no is:\t\t\t\t"+str(self.rider_phone))
                    print("-"*30+"-"*30)
                    print("rider bike no plate:\t\t\t\t"+str(self.no_plate))
                    print("-"*30+"-"*30)
                    print("-"*30+"Receipt"+"-"*30)
                    print("Delivery Address\t\t\t\t:"+str(self.delivery_address))
                    print("-"*30+"-"*30)
                    print("Customer Name\t\t\t\t\t"+str(self.customer_name))
                    print("-"*30+"-"*30)
                    print("Phone\t\t\t\t\t\t"+str(self.phone_no))
                    print("-"*30+"-"*30)
                    print("Order date\t\t\t",date,time,day)
                    print("-"*30+"-"*30)
                    print("Payment type\t\t\t\t\t"+str(self.payment_type))
                    print("-"*30+"-"*30)
                    print("Amount without GST\t\t\t\t:"+str(excel["Price"]))
                    print("-"*30+"-"*30)
                    print("Total Amount Without discount: PKR\t\t"+str(final_price))
                    print("-"*30+"-"*30)
                    print("13% GST: PKR\t\t\t\t\t"+str(discount))
                    print("-"*30+"-"*30)
                    print("Total Amount With Distcont PKR\t"+str(discount))
                    print("-"*30+"-"*30)
                    print("Your area is\t\t\t\t\t"+str(self.delivery_address))
                    print("-"*30+"-"*30)
                    print("Your No of total items you order\t\t"+str(excel["Qty"]))
                    print("-"*30+"-"*30)
                    print("Your total items\t\t\t\t"+str(excel["Food"]))
                    print("-"*30+"-"*30)
                    print("Order will be delivered within 45 mins")
                    print("-"*20+"THANK YOU FOR SHOPPING"+"-"*20)
                else:
                    price=c*qty
                    tax=price*0.13 
                    final_price=price+tax
                    import time
                    from datetime import datetime
                    now=datetime.now()
                    time=now.strftime("%H:%M%p")
                    date=now.strftime("%m/%d/%Y")
                    day=now.strftime("%a")
                    print("-"*20+"RIDER DETAILS"+"-"*20)
                    print("your rider name is\t\\t"+str(self.rider_name))
                    print("-"*30+"-"*30)
                    print("rider phone no is:\t\t\t\t"+str(self.rider_phone))
                    print("-"*30+"-"*30)
                    print("rider bike no plate:\t\t\t\t"+str(self.no_plate))
                    print("-"*30+"-"*30)
                    print("-"*30+"Receipt"+"-"*30)
                    print("Delivery Address\t\t\t\t"+ self.delivery_address)
                    print("-"*30+"-"*20)
                    print("Customer Name\t\t\t\t\t"+self.customer_name)
                    print("-"*30+"-"*30)
                    print("Phone\t\t\t\t\t\t"+str(self.phone_no))
                    print("-"*30+"-"*30)
                    print("Order date\t\t\t",date,time,day)
                    print("-"*30+"-"*30)
                    print("Payment type\t\t\t\t\t"+str(self.payment_type))
                    print("-"*30+"-"*30)
                    print("Amount without GST\t\t\t\t"+str(excel["Price"]))
                    print("-"*30+"-"*30)
                    print("Total Amount Without discount PKR\t\t"+str(final_price))
                    print("-"*30+"-"*30)
                    print("13% GST: PKR\t\t\t\t\t"+str(price))
                    print("-"*30+"-"*30)
                    print("Your area is\t\t\t\t\t"+str(self. delivery_address))
                    print("-"*30+"-"*30)
                    print("Your No of total items you order\t\t"+str(excel["Qty"]))
                    print("-"*30+"-"*30)
                    print("Your total items\t\t\t\t"+str(excel["Food"]))
                    print("-"*30+"-"*30)
                    print("Order will be delivered within 45 mins")
                    print("-"*20+"THANK YOU FOR SHOPPING"+"-"*20)
class customer(cart):
    def __init__(self,delivery_address,customer_name,phone_no,df,excel,cus_file):
        self.delivery_address=delivery_address
        self.customer_name=customer_name
        self.phone_no=phone_no
        self.df=df
        self.excel=excel
        self.cus_file=cus_file
    def customer_data(self):
        customer_sheet=({"customer address":[],"customer name":[],"phone no":[]})
        add=customer_sheet["customer address"]
        add.append(self.delivery_address)
        cus_name=customer_sheet["customer name"]
        cus_name.append(self.customer_name)
        phone=customer_sheet["phone no"]
        phone.append(self.phone_no)
        self.df=pd.DataFrame.from_dict(excel)
        print("you can print your order details from here")
        print("customer recepit")
        print(self.df)
        df=pd.DataFrame.from_dict(customer_sheet)
        print("customer data")
        print(df)
        cus_file=open("file1.txt","r")
        print(cus_file.read())

#drivers code
print("LOGIN HERE FIRST")
import re
from getpass import getpass  
email=str(input("enter your email:\t"))
password=getpass("enter your password:\t")
match1=re.search("@+",email)
cus_file=open("file1.txt","w")
cus_file.write(email+"\n")
cus_file.write(password+"\n")
cus_file=open("file1.txt","r")
email1=cus_file.readline()
password1=cus_file.readline()
if match1:
    if email in email1 and password in password1:
        print('"LOGIN SUCCESSFULL"')
        print()
        print('"WELCOME TO MY FOOD DELIVERY"')
        print()
    delivery_address=str(input("enter your location: ")).upper()
    customer_name=str(input("enter your name: ")).title()
    phone_no=int(input("enter your phone number: "))
    payment_type=input("enter payment type cash or debit: ").title() 
    print()
    print('"RESTAURENTS WE OFFER YOU"')
    df1=pd.read_excel("D:\Book1.xlsx")
    print(df1)
    print()
    print('"YOUR NEAR BY RESTAURANTS ARE:"')
    print()
    if  delivery_address=="GULSHAN":
        df1=pd.read_excel("D:\Book2.xlsx")
        print(df1)
    if  delivery_address=="HIGHWAY":
        df2=pd.read_excel("D:\Book3.xlsx")
        print(df2)    
    if  delivery_address=="DHA":
        df3=pd.read_excel("D:\Book4.xlsx")
        print(df3)   
    if  delivery_address=="SHAHFAISAL":
        df4=pd.read_excel("D:\Book5.xlsx")
        print(df4)            
    area={"GULSHAN":["kfc","burger o clock","subway","pizza  point","kaybees"],
                    "HIGHWAY":["khyber shenwari","haveli","khan sahab","al sajjad"],
                    "DHA":["amichi pizzeria","nando's"],
                    "SHAHFAISAL":["Ginsoy","Golden Fish"]}
    menu={"KFC":{"Twister":350,"Zinger":400,"Kentucky":500,"Mighty Zinger":600,"Zinger Stacker":450},
            "BUGER O CLOCK":{"Fire Bird":500,"Chick'n krisp":550,"Beef Vegi":600,"Beef Cheese":400,"Smoky Tang":230},
            "SUBWAY":{"Bbq Chicken":400,"Chicken Fajita":3000,"Oven Rosted Chicken":550,"Chicken Sub":379,"Chicken Tikka Salad":450,"Periperi Chicken Salad":500},
            "PIZZA POINT":{"Chicken Max":700,"Shawarma Lover":900,"Malai Tikka":450,"Chesse Lover":300,"spicy italian":300,"italian light":300},
            "KAYBEES":{"Scoopy Soft":599,"Chicken Mughlai Boti":723,"Crispy Chicken Burger":442,"Club Sandwich":417,"Crispy Broast":417,"Cripy Fish Burger":599},
            "KHYBER SHENWARI":{"Chicken Karhai":1200,"Boneless Karhai":1400,"White Karhai":1500,"Tikka":300},
            "KHAN SAHAB":{"Kabuli Pulao":1300,"Mandi":1600,"Malai Boti":340,"Chargha":650},
             "HAVELI":{"Chicken Cheese Naan":495,"Qeema Wala Naan":475,"Mutton Kabab":1295,"Girlled Chops":1295},
             "AL SAJJAD":{"Thai consome":195,"Vegetable Soup":195,"Reshmi Kabab":945,"Gola Kabab":995},
            "AMICHI PIZZERIA":{"Arab Sensation":1200,"The Majesty":230," Calzone":400,"Molten Lava":300,"Choclate Calzone":300},
            "Nando's":{"Cheesy Festa Fries":500,"Chicken Wings":300,"Appeteaser Platter":1200,"Peri-Peri Bites":890,"Bbq Chicken Wings":700},
            "Ginsoy":{"Vegi Soup":395,"Egg Tomato":335,"Chicken Corn Soup":300,"Chowmin":1200,"Fried Rice":600},
            "Golden Fish":{"Biryani Fish":1200,"Shirmp Biryani":1400,"Fish Kabab":1500,"Prawn Kabab":1600,"Fried Fish":1000}}
    excel=({"Qty":[],"Food":[],"Price":[],"Price with Quantity":[]})
    df=pd.DataFrame.from_dict(excel)
    obj2=cart(area,menu,df,excel,delivery_address,customer_name,phone_no,payment_type,"saad","0315123633","av9032")
    obj2.your_cart()
    obj3=customer(delivery_address,customer_name,phone_no,df,excel,cus_file)
    obj3.customer_data()
else:
    print("OOP !EMAIL NOT VAILD")
