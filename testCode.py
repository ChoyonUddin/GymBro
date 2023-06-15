#Pretty much a bunch of random code i was messing around with, keeping it stored to just in case i need it later
import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sb
import glob,os
import Date

#from math import linegraph
#Temporary class

#df = pd.DataFrame(pd.read_csv('CSVs/Bench_Press.csv'))

df = pd.DataFrame(pd.read_csv('CSVs/Bench_Press.csv').iloc[1:3,0:3:2])

#linegraph(data=df,x='Sets',y='Weight')
'''
#User input for data testing

# Adds row

# Creates new row to enter data for the csv
#Later on I'm not going to want to do a loop cause that forces me to actually input all data and I cant go back
#It's better to create them as fields and input the data through that way. That will allow me to edit the data. 
#Not only that I can confirm through a submit and go back to edit the data later

data = {i:[input(f'{i} ')] if i != 'Date' else [formattedDate] for i in Headers}
#currently creating a new csv but i want to just add a row
pd.DataFrame(data).to_csv('CSVs/Bench_Press.csv',mode='a',index=False,header=False)
#pd.DataFrame().add(1,fill_value=0)
#print(file='Bench_Press.csv')

#Removes row

#Overwrites row

#windows wsl2 - Windows 11 - ubuntu linux

'''










#Makes a dataframe from given columns and data and makes them into
#csvs using the names of the exercises from data.csv and saves it in folder 'CSVs'
#os.chdir literally is not optimal but Had create a quick brainless solution after losing data
'''

os.chdir('CSVs')
df = pd.DataFrame(pd.read_csv('data.csv'))

data = {'Date': [formattedDate]}
Headers = ['Set','Reps','Weight','Date','Max Lift','Body Weight','Fat%','Phase','Completed','Notes']

Edf = pd.DataFrame(data,columns=Headers).fillna('N/A')

for i in df['Name']:
    Edf.to_csv(f'{i.replace(" ","_")}.csv',index=False)
'''




'''#Might be useful for making a new exercise
df = pd.DataFrame(pd.read_csv('CSVs/Bench_Press.csv'))
#print(os.listdir("CSVs"))
print(df)
#User input for data
data = {i:[input(f'{i} ')] if i != 'Date' else [formattedDate] for i in df}
pd.DataFrame(data).to_csv('Bench_Press.csv')
'''


''' #Goofy Stuff
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
'''



#Mark later
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