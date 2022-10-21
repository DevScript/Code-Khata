from datetime import date 
import pandas as pd

class food:
    def loc(self):
        pass
    def basic_info(self):
        pass
    def rating_(self):
        pass
    def reviews(self):
        pass
class Mcdonald(food):
    def loc(self):
        print("info of Restaurant:Mcdonald")
        print("Address: Plot No, 3-A/FL-06, 24, KDA Scheme #1 Block 7 Gulshan-e-Iqbal, Karachi")
    def basic_info(self,ph=0,hr=0):
        hr="Open(24 hours)"
        ph=3008259945
        print(f'Phone :{ph}\tHours :{hr}')
    def rating_(self):
        print("4.2 rating")
    def reviews(self):
        print("Reviews:")
        print("taha xafar:\nWonderful place, I love this place just because of play area for kids.")
class Royal_Taj_Restaurant(food):
    def loc(self):
        print("info of Restaurant:Royal Taj Restaurant")
        print("Address: Allama Shabbir Ahmed Usmani Rd, Block 7 Gulshan-e-Iqbal, Karachi,")
    def basic_info(self,ph=0,hr=0):
        hr="Open(12 pm - 1 am)"
        ph=3008259978
        print(f'Phone :{ph}\tHours :{hr}')
    def rating_(self):
        print("4.1 rating")
    def reviews(self):
        print("Reviews:")
        print("Anas masood:\nPretty ambiance,service was also good. ordered RT special pizza(amazing taste).")
class Alvigha_Food(food):
    def loc(self):
        print("info of Restaurant:Alvigha Food")
        print("Address: A 295, Block 2 Gulshan-e-Iqbal, Karachi, Karachi City, Sindh")
    def basic_info(self,ph=0,hr=0):
        hr="Open(12 pm - 1 am)"
        ph=3008259911
        print(f'Phone :{ph}\tHours :{hr}')
    def rating_(self):
        print("4.3 rating")
    def reviews(self):
        print("Reviews:")
        print("Ahsan sajid:\nThe best food I ate in Karachi till date.")
class Studio_7teas(food):
    def loc(self):
        print("info of Restaurant:Studio 7teas")
        print("Address: B-698, Federal B Area Block 13 Gulberg Town, Karachi")
    def basic_info(self,ph=0,hr=0):
        hr="Open(12 pm - 12 am)"
        ph=3008259780
        print(f'Phone :{ph}\tHours :{hr}')
    def rating_(self):
        print( "4.3 rating")
    def reviews(self):
        print("Reviews:")
        print("J iklas:\nTaste was good, overall good experience.")
class khan_broast(food):
    
    def loc(self):
        print("info of Restaurant:khan broast")
        print("Address: Shahrah-e-Pakistan, Federal B Area Block 13 Gulberg Town, Karachi")
    def basic_info(self,ph=0,hr=0):
        hr="Open(12 pm - 12 am)"
        ph=3008259078
        print(f'Phone :{ph}\tHours :{hr}')
    def rating_(self):
        print("4.0 rating")
    def reviews(self):
        print("Reviews:")
        print("Nadeem hussain:\nI used to eat fast food since my childhood from here. By then it was one of the best fast food restaurant in town.")
        print("Shariq:\nLast 30 years I have been visiting it. They have maintained their standards. Good quality zinger burgers and broast. The size matters")
class Baithak_Restaurant(food):
    def loc(self):
        print("info of Restaurant:Baithak Restaurant")
        print("Address: Plot # C-33 near Munawwer, Johar St, Block 12 Gulistan-e-Johar, Karachi")
    def basic_info(self,ph=0,hr=0):
        hr="Open(12 pm - 12 am)"
        ph=3008259977
        print(f'Phone :{ph}\tHours :{hr}')
    def rating_(self):
        print("4.0 rating")
    def reviews(self):
        print("Reviews:")
        print("Sammar khan:\nIt is an average restaurant in terms of sitting area and food quality.")
        print("Omair khalod:\nAverage taste, just liked garlic Nan.")
class Naan_Stop(food):
    def loc(self):
        print("info of Restaurant:Naan Stop")
        print("Address: near POB Eye Hospital, Block 11 Gulistan-e-Johar, Karachi")
    def basic_info(self,ph=0,hr=0):
        hr="Open(12 pm - 1 am)"
        ph=3004259978
        print(f'Phone :{ph}\tHours :{hr}')
    def rating_(self):
        print("4.0 rating")
    def reviews(self):
        print("Reviews:")
        print("Bilal khan:\nGreat taste👌.")
        print("Osama:\nSuch an exciting experience.")        
class Hevali(food):
    def loc(self):
        print("info of Restaurant:Hevali")
        print("Address: Karachi - Hyderabad Motorway, Sector 4 B Gulzar E Hijri Scheme 33, Karachi, Karachi City, Sindh")
    def basic_info(self,ph=0,hr=0):
        hr="Open(12 pm - 2 am)"
        ph=30072599789
        print(f'Phone :{ph}\tHours :{hr}')
    def rating_(self):
        print( "4.0 rating")
    def reviews(self):
        print("Reviews:")
        print("Sadia kasshif:\nVisited first time there.... Had an awesome experience in terms of ambiance, service and on the top of all these taste of food was delicious and so tempting. ")
        print("Umer khalid:\nFood quality is superb👌.")
class Al_habib(food):
    def loc(self):
        print("info of Restaurant:Al habib")
        print("Address: Karachi - Hyderabad Motorway, Gadap Town, Karachi, Karachi City, Sindh")
    def basic_info(self,ph=0,hr=0):
        hr="Open(12 pm - 1 am)"
        ph=3006259978
        print(f'Phone :{ph}\tHours :{hr}')
    def rating_(self):
        return "4.3 rating"
    def reviews(self):
        print("Reviews:")
        print("Noor hussian:\nWent AlHabib for their Special Handi.")
        print("The food was good and the service they provided were good as well! Highly recommended if you are near the Super Highway area!")
class Dua(food):
    def loc(self):
        print("info of Restaurant:Dua")
        print("Address: St-3, Scheme 33 Tapo Gujro deh Songal، Karachi - Hyderabad Motorway")
    def basic_info(self,ph=0,hr=0):
        hr="Open(12 pm - 1 am)"
        ph=3008959929
        print(f'Phone :{ph}\tHours :{hr}')
    def rating_(self):
        print("4.0 rating")
    def reviews(self):
        print("Reviews:")
        print("Daniyal khan:\nA lot to improve in terms of ambiance. Washrooms are in worst possible condition. Rates are also very high.")
class booking:
    def book_tables(self,b_1=0,pr_=0,b_c=0):
        self.b_1=int(input("enter what type of table you want?\n2 Person table\n4 Person table\n8 Person table\n16 Person table\n~~"))
        if (self.b_1 == 2) or (self.b_1 ==4) or (self.b_1==8)or(self.b_1==16):#booking person tables 
            if self.b_1 == self.b_1:
                print('!GREAT')
                self.pr_=10*self.b_1
                print(f'The price of {self.b_1} person  table is {self.pr_}.')
            else:
                pass
        elif self.b_1 >= 16 :
            self.b_c = int(input("Custom booking?\nEnter number of seats for custom table:"))
            self.pr_=10*self.b_c
            print(f'Custom table:\nThe price of {b_c} person  table is {pr_}.')
        else:
            print("None table was booked!")
    def parking(self,b_2=0,b_3=0):
        self.b_2=input("You want to book parking spot?\nYes \tNO \n~")

        if self.b_2 == "yes":
            self.b_3=int(input("How much parking space you want ?\n~"))
            print("Parking spot booked!")
        else:
            print("Parking is not Booked!")
    def info_(self,pn,day,Time):
        #infoo
        self.person=pn
        self.day=day
        self.Time = Time
        
    def show_info_reservation(self):
        data_1={"Table":[self.b_1],"Person":[self.person],"Parking":[self.b_3],"Time":[self.Time]}
        d=pd.DataFrame(data_1)
        d.to_csv("data_2.csv")
        d.index+=1
        
class login_sys:
    def new_acc(self,name,lname,email,phone,pas1=0):
        self.n=name
        self.__l=lname
        self.__e=email
        self.__p=phone
        print("!Your account has been created")
        dict1={
            "name":[self.n],
            "last name":[self.__l],
            "email":[self.__e],
            "phone":[self.__p]
        }
        info=pd.DataFrame(dict1)
        info.to_csv("data.csv")
        info.index+=1
        
    
class Seat_reservation(login_sys,booking):
    def recipt(self): 
        print("----Entry--Recipt--")
        print(f"Customer:{self.n} ")
        print("Customer details:")
        info=pd.read_csv('data.csv')
        info.index+=1
        display(info)
        print("Customer reservation details:")
        d=pd.read_csv('data_2.csv')
        d.index+=1
        display(d)
        print("Thank you --------")
    
#
print("welcome to Seat reservation app")
def APP(user,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10):
    app_ask=input("hello user are you searching for restaurants\n~Yes\n~No\n~")
    if app_ask == "yes":
        
        while(True):
            
            app = int(input("?\n1.Create account\n2.login into account\n3.Exit\n~~"))
            if app == 1:
                print("Creating Account:")
                name=input("enter your first name?")
                lname=input("enter your last name?")
                email=input("enter your email?")
                phone=int(input("enter phone number?"))
                user.new_acc(name,lname,email,phone) 
            elif app == 2:
                print("Login here!")
                c_n=input("enter your first name?")
                c_ph=int(input("enter phone number?"))
                show2=pd.read_csv('data.csv')
                if (show2['name'][0] == c_n ) and (show2['phone'][0] == c_ph):
                    print("User confirmed!")
                    ask=input(f"what type of food you like?\n1.Fast food\n2.Desi restaurant\n")
                    print("!Great ")
                    ask2=int(input("Search the nearest place you want to eat?\n1.Guberg,karachi\n2.Gulistan-e-johar,Karachi\n3.Gulshan,Karachi\n4.Motor highway,Karachi\n~ "))
                    if ask2 == 1:
                        print("Area :Guberg,karachi")
                        ask3=int(input("These restuarant are present in your given area:\n1.Studio 7teas\n2.khan broast\n~."))
                        if ask3 == 1:
                            f4.loc()
                            f4.basic_info()
                            f4.rating_()
                            f4.reviews()
                            ask_1=input("You want to book further facility?\nYes \nNo\n~")
                            if ask_1 == "yes":
                                
                                while(True):
                                    ask_2=int(input("Section : \n1.Book tables\t2.Book parking spot\n3.Details\t4.Show Reservation \n5.Generate Entry recipt\t6.Exit\n.~="))
                                    if ask_2 == 1:
                                        user.book_tables()
                                    elif ask_2 == 2:
                                        user.parking()
                                    elif ask_2 == 3:
                                        pn=int(input("how much person your are?\tThe information is just for your history\n~"))
                                        day=str(input('Enter check in date(yyyy-mm-dd): '))
                                        Time = str(input('Enter check in time(%H:%M:%S): '))
                                        user.info_(pn,day,Time)
                                    elif ask_2 == 4:
                                        user.show_info_reservation()
                                    elif ask_2 == 5:
                                        user.recipt()
                                    elif ask_2== 6:
                                        print("Exit")
                                        break

                            else:
                                print("Exit")
                        elif ask3 == 2:
                            f5.loc()
                            f5.basic_info()
                            f5.rating_()
                            f5.reviews()
                            ask_1=input("You want to book further facility?\nYes \nNo\n~")
                            if ask_1 == "yes":                          
                                while(True):
                                    ask_2=int(input("Section : \n1.Book tables\t2.Book parking spot\n3.Details\t4.Show Reservation \n5.Generate Entry recipt\t6.Exit\n.~="))
                                    if ask_2 == 1:
                                        user.book_tables()
                                    elif ask_2 == 2:
                                        user.parking()
                                    elif ask_2 == 3:
                                        pn=int(input("how much person your are?\tThe information is just for your history\n~"))
                                        day=str(input('Enter check in date(yyyy-mm-dd): '))
                                        Time = str(input('Enter check in time(%H:%M:%S): '))
                                        user.info_(pn,day,Time)
                                    elif ask_2 == 4:
                                        user.show_info_reservation()
                                    elif ask_2 == 5:
                                        user.recipt()
                                    elif ask_2== 6:
                                        print("Exit")
                                        break

                            else:
                                print("Exit")
                        else:
                            print("above restaurants are available!")
                    elif ask2 == 2:
                        print("Area :Gulistan-e-johar,Karachi")
                        ask3=int(input("These restuarant are present in your given area:\n1.Baithak Restaurant\n2.Naan stop\n~."))
                        if ask3 == 1:
                            f6.loc()
                            f6.basic_info()
                            f6.rating_()
                            f6.reviews()
                            ask_1=input("You want to book further facility?\nYes \nNo\n~")
                            if ask_1 == "yes":
                                
                                while(True):
                                    
                                    ask_2=int(input("Section : \n1.Book tables\t2.Book parking spot\n3.Details\t4.Show Reservation \n5.Generate Entry recipt\t6.Exit\n.~="))
                                    if ask_2 == 1:
                                        user.book_tables()
                                    elif ask_2 == 2:
                                        user.parking()
                                    elif ask_2 == 3:
                                        pn=int(input("how much person your are?\tThe information is just for your history\n~"))
                                        day=str(input('Enter check in date(yyyy-mm-dd): '))
                                        Time = str(input('Enter check in time(%H:%M:%S): '))
                                        user.info_(pn,day,Time)
                                    elif ask_2 == 4:
                                        user.show_info_reservation()
                                    elif ask_2 == 5:
                                        user.recipt()
                                    elif ask_2== 6:
                                        print("Exit")
                                        break
                            else:
                                print("Exit")
                        elif ask3 == 2:
                            f7.loc()
                            f7.basic_info()
                            f7.rating_()
                            f7.reviews()
                            ask_1=input("You want to book further facility?\nYes \nNo\n~")
                            if ask_1 == "yes":
                                
                                while(True):
                                    ask_2=int(input("Section : \n1.Book tables\t2.Book parking spot\n3.Details\t4.Show Reservation \n5.Generate Entry recipt\t6.Exit\n.~="))
                                    if ask_2 == 1:
                                        user.book_tables()
                                    elif ask_2 == 2:
                                        user.parking()
                                    elif ask_2 == 3:
                                        pn=int(input("how much person your are?\tThe information is just for your history\n~"))
                                        day=str(input('Enter check in date(yyyy-mm-dd): '))
                                        Time = str(input('Enter check in time(%H:%M:%S): '))
                                        user.info_(pn,day,Time)
                                    elif ask_2 == 4:
                                        user.show_info_reservation()
                                    elif ask_2 == 5:
                                        user.recipt()
                                    elif ask_2== 6:
                                        print("Exit")
                                        break
                            else:
                                print("Exit")
                        else:
                            print("above restaurants are available!")

                    elif ask2 == 3:
                        print("Area :Gulshan,Karachi")
                        ask3=int(input("These restuarant are present in your given area:\n1.Mcdonalds\n2.Royal Taj Restaurant\n3.Alvigha Food\n~"))
                        if ask3 == 1:
                            f1.loc()
                            f1.basic_info()
                            f1.rating_()
                            f1.reviews()
                            ask_1=input("You want to book further facility?\nYes \nNo\n~")
                            if ask_1 == "yes":
                                
                                while(True):
                                    ask_2=int(input("Section : \n1.Book tables\t2.Book parking spot\n3.Details\t4.Show Reservation \n5.Generate Entry recipt\t6.Exit\n.~="))
                                    if ask_2 == 1:
                                        user.book_tables()
                                    elif ask_2 == 2:
                                        user.parking()
                                    elif ask_2 == 3:
                                        pn=int(input("how much person your are?\tThe information is just for your history\n~"))
                                        day=str(input('Enter check in date(yyyy-mm-dd): '))
                                        Time = str(input('Enter check in time(%H:%M:%S): '))
                                        user.info_(pn,day,Time)
                                    elif ask_2 == 4:
                                        user.show_info_reservation()
                                    elif ask_2 == 5:
                                        user.recipt()
                                    elif ask_2== 6:
                                        print("Exit")
                                        break

                            else:
                                print("Exit")
                        elif ask3 == 2:
                            f2.loc()
                            f2.basic_info()
                            f2.rating_()
                            f2.reviews()
                            ask_1=input("You want to book further facility?\nYes \nNo\n~")
                            if ask_1 == "yes":
                                
                                while(True):
                                    ask_2=int(input("Section : \n1.Book tables\t2.Book parking spot\n3.Details\t4.Show Reservation \n5.Generate Entry recipt\t6.Exit\n.~="))
                                    if ask_2 == 1:
                                        user.book_tables()
                                    elif ask_2 == 2:
                                        user.parking()
                                    elif ask_2 == 3:
                                        pn=int(input("how much person your are?\tThe information is just for your history\n~"))
                                        day=str(input('Enter check in date(yyyy-mm-dd): '))
                                        Time = str(input('Enter check in time(%H:%M:%S): '))
                                        user.info_(pn,day,Time)
                                    elif ask_2 == 4:
                                        user.show_info_reservation()
                                    elif ask_2 == 5:
                                        user.recipt()
                                    elif ask_2== 6:
                                        print("Exit")
                                        break
                            else:
                                print("Exit")
                        elif ask3 == 3:
                            f3.loc()
                            f3.basic_info()
                            f3.rating_()
                            f3.reviews()
                            ask_1=input("You want to book further facility?\nYes \nNo\n~")
                            if ask_1 == "yes":
                                
                                
                                while(True):
                                    ask_2=int(input("Section : \n1.Book tables\t2.Book parking spot\n3.Details\t4.Show Reservation \n5.Generate Entry recipt\t6.Exit\n.~="))
                                    if ask_2 == 1:
                                        user.book_tables()
                                    elif ask_2 == 2:
                                        user.parking()
                                    elif ask_2 == 3:
                                        pn=int(input("how much person your are?\tThe information is just for your history\n~"))
                                        day=str(input('Enter check in date(yyyy-mm-dd): '))
                                        Time = str(input('Enter check in time(%H:%M:%S): '))
                                        user.info_(pn,day,Time)
                                    elif ask_2 == 4:
                                        user.show_info_reservation()
                                    elif ask_2 == 5:
                                        user.recipt()
                                    elif ask_2== 6:
                                        print("Exit")
                                        break

                            else:
                                print("Exit")
                        else:
                            print("above restaurants are available!")

                    elif ask2 == 4:
                        print("Area :Motor highway,Karachi")
                        ask3=int(input("These restuarant are present in your given area:\n1.Hevali restaurant\n2.Al habib restaurant\n3.Dua restaurant"))
                        if ask3 == 1:
                            f8.loc()
                            f8.basic_info()
                            f8.rating_()
                            f8.reviews()
                            ask_1=input("You want to book further facility?\nYes \nNo\n~")
                            if ask_1 == "yes":
                                
                                while(True):
                                    ask_2=int(input("Section : \n1.Book tables\t2.Book parking spot\n3.Details\t4.Show Reservation \n5.Generate Entry recipt\t6.Exit\n.~="))
                                    if ask_2 == 1:
                                        user.book_tables()
                                    elif ask_2 == 2:
                                        user.parking()
                                    elif ask_2 == 3:
                                        pn=int(input("how much person your are?\tThe information is just for your history\n~"))
                                        day=str(input('Enter check in date(yyyy-mm-dd): '))
                                        Time = str(input('Enter check in time(%H:%M:%S): '))
                                        user.info_(pn,day,Time)
                                    elif ask_2 == 4:
                                        user.show_info_reservation()
                                    elif ask_2 == 5:
                                        user.recipt()
                                    elif ask_2== 6:
                                        print("Exit")
                                        break

                            else:
                                print("Exit")
                        elif ask3 == 2:
                            f9.loc()
                            f9.basic_info()
                            f9.rating_()
                            f9.reviews()
                            ask_1=input("You want to book further facility?\nYes \nNo\n~")
                            if ask_1 == "yes":
                                while(True):
                                    ask_2=int(input("Section : \n1.Book tables\t2.Book parking spot\n3.Details\t4.Show Reservation \n5.Generate Entry recipt\t6.Exit\n.~="))
                                    if ask_2 == 1:
                                        user.book_tables()
                                    elif ask_2 == 2:
                                        user.parking()
                                    elif ask_2 == 3:
                                        pn=int(input("how much person your are?\tThe information is just for your history\n~"))
                                        day=str(input('Enter check in date(yyyy-mm-dd): '))
                                        Time = str(input('Enter check in time(%H:%M:%S): '))
                                        user.info_(pn,day,Time)
                                    elif ask_2 == 4:
                                        user.show_info_reservation()
                                    elif ask_2 == 5:
                                        user.recipt()
                                    elif ask_2== 6:
                                        print("Exit")
                                        break

                            else:
                                print("Exit")
                        elif ask3 == 3:
                            f10.loc()
                            f10.basic_info()
                            f10.rating_()
                            f10.reviews()
                            ask_1=input("You want to book further facility?\nYes \nNo\n~")
                            if ask_1 == "yes":
                                while(True):
                                    ask_2=int(input("Section : \n1.Book tables\t2.Book parking spot\n3.Details\t4.Show Reservation \n5.Generate Entry recipt\t6.Exit\n.~="))
                                    if ask_2 == 1:
                                        user.book_tables()
                                    elif ask_2 == 2:
                                        user.parking()
                                    elif ask_2 == 3:
                                        pn=int(input("how much person your are?\tThe information is just for your history\n~"))
                                        day=str(input('Enter check in date(yyyy-mm-dd): '))
                                        Time = str(input('Enter check in time(%H:%M:%S): '))
                                        user.info_(pn,day,Time)
                                    elif ask_2 == 4:
                                        user.show_info_reservation()
                                    elif ask_2 == 5:
                                        user.recipt()
                                    elif ask_2== 6:
                                        print("Exit")
                                        break

                            else:
                                print("Exit")

                        else:
                            print("above restaurants are available!")
                    else:
                        print("Other areaes are out of range!")

                else:
                    print("Your not register!")
            else:
                print("Thank you for visiting!")
                break
    else:
        print('Just checking!')
f1=Mcdonald()
f2=Royal_Taj_Restaurant()
f3=Alvigha_Food()
f4=Studio_7teas()
f5=khan_broast()
f6=Baithak_Restaurant()
f7=Naan_Stop()
f8=Hevali()
f9=Al_habib()
f10=Dua()
user=Seat_reservation()
APP(user,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10)
