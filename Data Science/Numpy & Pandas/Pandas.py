#write all basic pandas functions here

import pandas as pd

#series
a = pd.Series([1,2,3,4,5])
print(a)

#dataframe
b = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
print(b)

#read csv
c = pd.read_csv('Data Science\Numpy & Pandas\Numpy.py')

#read excel
d = pd.read_excel('Data Science\Numpy & Pandas\Numpy.py')

#read html
e = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')

#read sql
from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
f = pd.read_sql('table', engine)

#write to csv
c.to_csv('Data Science\Numpy & Pandas\Numpy.py')

#write to excel
d.to_excel('Data Science\Numpy & Pandas\Numpy.py')

#write to sql
f.to_sql('my_table', engine)

#head
c.head()

#tail
c.tail()

#info
c.info()

#describe
c.describe()

#columns
c.columns

#values
c.values

#sort_values
c.sort_values('column1')

#sort_index
c.sort_index()

#isnull
c.isnull()

#dropna
c.dropna()

#fillna
c.fillna('fill')

#drop_duplicates
c.drop_duplicates()