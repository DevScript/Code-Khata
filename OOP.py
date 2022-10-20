import abc
class Bank(abc.ABC):
    @abc.abstractmethod
    def Accountname(self):
        pass
    @abc.abstractmethod
    def Deposit(self):
        pass
    @abc.abstractmethod
    def Withdraw(self):
        pass
class HBLBank(Bank):
    def Accountname(self):
        a="Muhammad Hassaan Iqbal"
        b=input("Enter your name: ")
        if b == a:
            print("Your logged in")
        else:
            print("Accountname not correct")
    def Deposit(self):
        c=input("Enter the amount you want deposit: ")
        return c
    def Withdraw(self):
        d=input("Enter the amount you want to withdraw: ")
        return d    
class MeezanBank(Bank):
    def Accountname(self):
        a="Muhammad Hassaan Iqbal"
        b=input("Enter your name: ")
        if b == a:
            print("Your logged in")
        else:
            print("Accountname not correct") 
    def Deposit(self):
        c=input("Enter the amount you want deposit: ")
        return c 
    def Withdraw(self):
        d=input("Enter the amount you want to withdraw: ")
        return d
obj2=MeezanBank()
obj2.Accountname()
print("The amount you deposited is",obj2.Deposit())
print("The amount you withdrawn after deposition is",obj2.Withdraw())
