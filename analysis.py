import pandas as pd
import datetime as dt
from sqlalchemy import create_engine # database connection

big_csv = pd.read_csv("311.csv") # fails
big_db = create_engine('sqlite:///big.db')

start = dt.datetime.now()
chunksize = 20000
j = 0
index_start = 1

for df in pd.read_csv('311.csv', chunksize=chunksize, iterator=True, encoding='utf-8'):
    
    df = df.rename(columns={c: c.replace(' ', '') for c in df.columns}) # Remove spaces from columns

    df['CreatedDate'] = pd.to_datetime(df['CreatedDate']) # Convert to datetimes
    df['ClosedDate'] = pd.to_datetime(df['ClosedDate'])

    df.index += index_start

    # Remove the un-interesting columns
    columns = ['Agency', 'CreatedDate', 'ClosedDate', 'ComplaintType', 'Descriptor',
               'CreatedDate', 'ClosedDate', 'TimeToCompletion',
               'City']

    for c in df.columns:
        if c not in columns:
            df = df.drop(c, axis=1)    

    
    j+=1
    print('{} seconds: completed {} rows'.format((dt.datetime.now() - start).seconds, j*chunksize))

    df.to_sql('data', big_db, if_exists='append')
    index_start = df.index[-1] + 1
    
df = pd.read_sql_query('SELECT * FROM data LIMIT 3', big_db)
df.head()