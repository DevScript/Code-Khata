import pandas as pd
data = [['DSA', 'Python', 80],
          ['DS', 'MATLAB', 70],
          ['OSDC', 'C', 94],
          ['MAPD', 'JAVA', 78]]
df = pd.DataFrame(data, columns=['Subject', 'Language', 'Marks'])
print(df)
