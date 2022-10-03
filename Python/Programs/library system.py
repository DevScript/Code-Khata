""" This program is an application of Object Oriented Programming concepts in Python.
A basic library system is created which allows users to see, issue,return,donate books in the library and
the data of respective users is stored simultaneously.
"""
import time
issueDic = {}
DonorDic = {}

#Creating Library class
class Library:
    def __init__(self,book_catalogue,library_name):
       self.book_catalogue=book_catalogue
       self.library_name=library_name
    def intro(self):
       print(20*"|*"+ " WELCOME TO SARASWATI LIBRARY " +20*"*|")
       userin=input("\n Do you want to get into options menu (Y/N): ")
       if userin=="Y":
           self.options()
       elif userin=="N":
           print("See you again,Thanks for coming to our library")
       else:
           print("Invalid Key entered,Type your response again after 3 seconds")
           time.sleep(3)
           self.intro()
    def options(self):
       print("\t How can we help you ?")
       print("\n","1. Show complete book catalogue ","\n","2. Issue a book","\n","3. Donate a book","\n","4. Return the issued book"
             "\n","5. List of issued books ","\n","6. List of donated books ","\n","7. Return to the main menu ")
       n=input("Enter your input:")
       if n=="1":
           self.display()
       elif n=="2":
           self.issueTheBook()
       elif n=="3":
           self.donate()
       elif n=="4":
           self.returnTheBook()
       elif n=="5":
           self.issuedBookList()
       elif n=="6":
           self.DonorsList()
       elif n=="7":
           self.MainMenu()
       else:
           print("Invalid Key entered,Type your response again after 3 seconds")
           time.sleep(3)
           self.options()
    def MainMenu(self):
        self.intro()
    def returnTheBook(self):
        self.display()
        name = input("Enter your name: ")
        retbooknum = input("Enter the serial number of the book you want to return: ")
        if name in issueDic.keys() and issueDic[name]==(self.book_catalogue)[int(retbooknum)-1] :
                print("Thanks "+name+" for returning the book "+(self.book_catalogue)[int(retbooknum)-1] + " in time")
                issueDic.pop(name)
        else:
            print("Record Not Found,Check the input details again carefully")
    def donate(self):
        donorName=input("Enter your name: ")
        bookDonated=input("Enter the name of the book you want to donate: ")
        (self.book_catalogue).append(bookDonated)
        print("Thanks "+str(donorName)+" for your generosity. Your contribution will empower many students ")
        DonorDic[donorName]=bookDonated
    def display(self):
       print("--- Our library currently have following books")
       for i in range(len(self.book_catalogue)):
        print(i+1," ",self.book_catalogue[i])
    def issueTheBook(self):
       self.display()
       name = input("Enter your name: ")
       booknum=input("Enter the serial number of the book you want to issue: ")
       if int(booknum)-1 not in list(range(len(self.book_catalogue))):
            print("Choose the serial number only provided in the given range of book catalogue.\n Wait for a while and type your response again")
            time.sleep(3)
            self.issueTheBook()

       elif (self.book_catalogue)[int(booknum)-1] not in issueDic.values():
            issueDic[name]=(self.book_catalogue)[int(booknum)-1]
            print("You have issued the book titled " + (self.book_catalogue)[int(booknum)-1])


       else:
            print("Sorry " + name+ " ,this book is already issued by someone else. We hope that you get it soon.")
    def issuedBookList(self):
       print("Person's name","\t"," Issued Book")
       for i in issueDic.keys():
           print(i,"\t",issueDic[i])
    def DonorsList(self):
        print("Person's name","\t", "Donated Book")
        for i in DonorDic.keys():
            print(i, "\t", DonorDic[i])

# creating object from library class
book_list=["Vedic Maths","Astrology","Physics by HC Verma","Optics by Ajoy Ghatak","Bhagwad Gita","Ramayan"]
lib_obj=Library(book_list,"Saraswati Library")

#infinite while loop asking users for their input
while(True):
    lib_obj.intro()



