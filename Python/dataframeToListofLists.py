import pandas as pd
df = pd.DataFrame(
          [['DSA', 'Python', 80],
          ['DS', 'MATLAB', 70],
          ['OSDC', 'C', 94],
          ['MAPD', 'JAVA', 78]], columns= ['Subject', 'Language', 'Marks'])
print ("DataFrame Output")
print(df)

def dfToTable(df:pd.DataFrame) -> list:
 return [list(df.columns)] + df.values.tolist()

print("\n Convert DataFrame to  list of lists :" +str(dfToTable(df)))
