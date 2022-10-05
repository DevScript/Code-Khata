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

#pandas reorder columns alphabetically
sorted_column_df = df.sort_index(axis=1)
print(sorted_column_df)
