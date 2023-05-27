import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sb
import glob,os

os.chdir('C:\Programming\Python\Personal\GymBro\CSVs')
df = pd.DataFrame((pd.read_csv('data.csv')))
#print(glob.glob('*.csv'))
print(list(df.columns[1:]))
'''
#df.head(5).fillna("This value is missing")
print(df.loc[df['Name'] == 'Bench Press'])
df.head(5).to_csv('New Data.csv')
#print(df.head(5)['Name'])

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