#Simple dataframe
import pandas as pd
df = pd.DataFrame(
    {
        'Name'    : ['Brian', 'Morgan', 'Anderson', 'Clark', 'Junaid'],
        'Subject' : ['DSA', 'DS', 'OSDC', 'MAPD', 'CAAP'],
        'Language': ['Python', 'MATLAB','C', 'JAVA','Assembly'],
        'Marks'   :  [80, 70, 94, 78, 91]
    }
)
#Pandas reorder columns by index
df = df.reindex(columns=['Subject', 'Language', 'Name', 'Marks'])
print(df)
