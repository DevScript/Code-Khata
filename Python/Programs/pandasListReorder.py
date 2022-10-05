#Simple dataframe
import pandas as pd
df = pd.DataFrame(
    {
        'Name'    : ['Brian', 'Morgan', 'Anderson', 'Clark', 'Junaid'],
        'Subject' : ['DSA', 'DS', 'OSDC', 'MAPD', 'CAAP'],
        'Language': ['Python', 'MATLAB','C', 'JAVA','AssembAly'],
        'Marks'   :  [80, 70, 94, 78, 91]
    }
)

#Pandas reorder columns based on list
df = df[['Language', 'Marks', 'Subject', 'Name']]
print(df)
