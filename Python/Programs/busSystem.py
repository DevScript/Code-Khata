import mmap
import os
from turtle import write # for shared memory
from prettytable import PrettyTable
import threading #for using threads

def readFile():
    data = []
    with open('busses.txt', 'r') as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as s:
            for line in iter(s.readline, b''):
                data.append(line)
    return data

def cleanData(data):
    for i in range(len(data)):
        data[i] = data[i].decode("utf-8").strip()
    return data

def organizeData(data):
    for i in range(len(data)):
        data[i] = data[i].split(',')
    return data

def tabularData(data):
    table = PrettyTable(["Bus #", "SQU Location", "Destination", "Student's Gender", "Driver's Name", "Available Seats", "Pickup Time"])
    for i in range(6):
        table.add_row(data[i])
    print(table)

def seatBook(data):
    print("Book a seat")
    busNumber = input("Enter the bus number: ")
    for i in range(len(data)):
        for j in range(len(data[i])):
            if busNumber == data[j][0]:
                if(int(data[i][5]) > 0):
                    print("Seat available")
                    data[i][5] = int(data[i][5]) - 1
                    with open('busses.txt', 'w') as f:
                        for k in range(len(data)):
                            for g in range(len(data[k])):
                                writeData = ''
                                writeData += str(data[k][g]) + ','
                                if(g == len(data[k]) - 1):
                                    writeData = writeData[:-1]
                                    writeData += '\n'
                                if(k == len(data) - 1 and g == len(data[k]) - 1):
                                    writeData = writeData[:-1]
                                f.write(writeData)
                    print("Seat booked")
                    return
                else:
                    print("Seat not available in Bus #: ", busNumber)
                    return
        else:
            print("Bus number not found")
            break
    
    
def main():
    os.system('clear')
    data = readFile()
    data = cleanData(data)
    data = organizeData(data)
    print("Welcome to the online bus reservation sytem\nPlease select anyone option from the following:\n1)View Busses\n2)Book a Seat")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        tabularData(data)
    elif choice == 2:
        x = threading.Thread(target=seatBook, args=(data,))
        print("I am a thread")
        x.start()
    else:
        print("Invalid choice")
        os.system("clear")
        main()
main()