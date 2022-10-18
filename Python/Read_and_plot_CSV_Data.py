import matplotlib.pyplot as plt   # here we are importing matplot library to plot data 
import csv                        # here we imported CSV library to read CSV file 

x = []                            # here we declared an empty array variable 
y = []                            # here we declared an empty array variable

with open('Example.csv','r') as csvfile:       # here we open CSV file 
	plots = csv.reader(csvfile, delimiter = ',') # ploting csv file data 
	
	for row in plots:
		x.append(row[0])                          # collecting data from rows and storing in array 
		y.append(int(row[2]))

plt.bar(x, y, color = 'g', width = 0.72, label = "Age")    #ploting data with Labels 
plt.xlabel('Names')                                        # declaring Labels 
plt.ylabel('Ages')                                         # declaring Labels
plt.title('Ages of different persons')                     # declaring Title
plt.legend()
plt.show()
