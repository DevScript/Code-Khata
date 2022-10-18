burgers=[]
quan=[]
def PrintHead():
    print("             ABC Burgers")
    print("        Pakistan Road,Karachi")
    print("=====================================")


# Data Entry:
rates = {"cheese": 110, "zinger": 160, "abc special": 250, "chicken": 120}
# Front-End:
def TakeInputs():
    b = input("Burger Type:").lower()
    if b not in rates.keys():
        print("Burger Type Not Recognized")
        print("Kindly try again, or add the new burger in Rates list")
        TakeInputs()
        return
    q = int(input("Quantity:"))
    burgers.append(b)
    quan.append(q)
    yn = input("Y to add another burger:")
    if yn == "y" or yn=="Y" :
        TakeInputs()
    else:
        print("Data Collection Complete!")


def receipt():
    total = 0
    print("{0:13} {1} {2:9} {3:9}".format("Burger","Rate","    Quantity","  Price"))
    for index,each_burger in enumerate(burgers):
        print("{0:13}".format(burgers[index].title()), rates[burgers[index]], "{0:9}".format(quan[index]),
              "{0:9}".format(rates[burgers[index]] * quan[index]))
        total += (rates[burgers[index]] * quan[index])

    print("-------------------------------------")
    print("                        Total:", total)

PrintHead()
TakeInputs()
PrintHead()
receipt()
