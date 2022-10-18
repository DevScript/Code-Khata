# Data loader for Health monitarization


import pandas as pd    # here we have imported Pandas Library 

file_to_load = "E:/DATA - Copy.txt"   # here we are having a .txt and we want to Extract data from a txt file split that data and create a CSV for our ML model

file_to_save = "E:/DATA Processed.csv"  # Location where processed Data will be saved

DF = pd.read_csv( file_to_load, index_col=None )    # class to read 

bpm = DF['bpm']                             # Label Declaration 
temp_f = DF['temp_f']                       # Label Declaration 
temp_c = DF['temp_c']                       # Label Declaration 
temp_date = DF['date']                      # Label Declaration 


Date = []                                   # Array Decleration
Time = []                                   # Array Decleration
BPM = []                                    # Array Decleration
Temp_f = []                                 # Array Decleration
Temp_c = []

for aa in range( len(temp_date) ):
    
    temp = temp_date[aa]
    
    try:

        Date.append( temp.split("\t")[1].split("T")[0] )
        Time.append( temp.split("\t")[1].split("T")[1] )
        
        BPM.append( bpm[aa] )
        Temp_f.append( temp_f[aa] )
        Temp_c.append( temp_c[aa] )
                
    except:
            
        pass
    
    
DF = pd.DataFrame( {"Date":Date, "Time":Time, "BPM":BPM, "Temp_f":Temp_f, "Temp_c":Temp_c}, index=None )     # creating a CSV file 
DF.to_csv( file_to_save )                                                                                    # Saving data to CSV file 
