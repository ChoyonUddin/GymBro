#Pretty much a bunch of random code i was messing around with, keeping it stored to just in case i need it later
import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sb
import glob,os
import Date
df = pd.DataFrame(pd.read_csv('CSVs\Bench Press.csv'))
#print(glob.glob('*.csv'))
#print(df.head(5)['Name'])

df = pd.DataFrame((pd.read_csv('data.csv')))
for i in df['Name','Primary Focus']:
    if i == 'Bench Press':
        print(i)

print(df.loc[df['Name'] == 'Bench Press'])
df.head(5).to_csv('New Data.csv')
#print(df.head(5)['Name'])

#print(df.head(10)['Name'] == 'Bench Press')
for i in df['Name']:
    if i == 'Bench Press':
        print(i)

for i in df:
    print(i)

    
data = {'Name': ['']}
headers = list(df.columns[1:])
print(headers)
Edf = pd.DataFrame(data,columns=headers)

print(Edf)
'''
#for i in range(len(df.head(1))):
    #df.to_csv(f'{df["Name"][i]}.csv')
count = 0
for i in df['Name']:
    if count < 1:
        df.to_csv(f'{i}.csv')
    else:
        exit
'''