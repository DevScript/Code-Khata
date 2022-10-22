import time
name=input("enter name of customer")
#price for each book
price=250
dict={'love':{'7398798':10},'revenge':{'798798':12},'hate':{'79870':6},'care':{'80980':9}}
for keys,value in dict.items():
    dict[keys]=value
    c=keys
    print(c)
    #for keys,value in c.items():
       #c[keys]=value
      #print(value)
a=input("enter the name of book")
h=int(input("enter number of quantity"))
d=dict.pop(a)
print(d)
for x,y in d.items():
    d[x]=y
    f=y-h
    print(f)
r=input("enter name of book return")
days=0
fine=0
if c!=r:
    for i in range(20):
        days=days+1
        fine=fine+1
    if days<=20:
        fine=fine+10
    if days==20:
        print(days)
        print("since you exceeded the time period for return you fine is","=",fine)
total_price_of_books_borrowed=price*f      
print("*----------------ORIGNAL SLIP---------------------*")
j=time.strftime('%d %m %y')
print("date","=",j)
print("name of customer","=", name)
print("-----library-----")
print("name of book","=",a)
print("quantity","=",f)
print("price of book","=","RS",":", total_price_of_books_borrowed)
print("total price of book borrowed","=", price*f)
print("casheir on counter",":","dua-e-zainab")
print("*------","EMANUELLA LIBRARY AT YOUR SERVICE!!","------*")

be=str(dict)
se=str(total_price_of_books_borrowed)
infile=open('library.txt','w')
infile.write(be)
infile.write(se)
infile.close()
