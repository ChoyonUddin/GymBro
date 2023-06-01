import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sb
import glob,os
import Date
os.chdir('CSVs')

#Creates CSV files from header + Some other stuff I was messing around with 
'''
# Data
df = pd.DataFrame(pd.read_csv('data.csv'))

data = {'Date': [Date.formattedDate]}
headers = ['Set','Reps','Weight','Date','Max Lift','Body Weight','Fat%','Phase','Completed','Notes']
Edf = pd.DataFrame(data,columns=headers).fillna('N/A')


for i in df['Name']:
    Edf.to_csv(f'{i.replace(" ","_")}.csv',index=False)

    #what I got to do right now is to make a dataframe that has the name of the categories only 
    #I want to automatically do that so that Maybe I can find a way to make it easier
    #Basically I am creating an empty csv with just the column names and making a new csv using the name from df
    #1. I could just copy rather than convert 2. I could just get the names of the columns in an array
    #without making it a csv and use those 3. I could just get all the names of the df without looping
    

'''