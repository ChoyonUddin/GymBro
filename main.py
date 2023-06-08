import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sb
import glob,os,csv
from Date import formattedDate
from CreateCSV import Headers
#from math import linegraph
#Temporary class

#df = pd.DataFrame(pd.read_csv('CSVs/Bench_Press.csv'))

df = pd.DataFrame(pd.read_csv('CSVs/Bench_Press.csv').iloc[1:3,0:3:2])

#linegraph(data=df,x='Sets',y='Weight')
'''
#User input for data testing

# Adds row

# Creates new row to enter data for the csv
data = {i:[input(f'{i} ')] if i != 'Date' else [formattedDate] for i in Headers}
#currently creating a new csv but i want to just add a row
pd.DataFrame(data).to_csv('CSVs/Bench_Press.csv',mode='a',index=False,header=False)
#pd.DataFrame().add(1,fill_value=0)
#print(file='Bench_Press.csv')

#Removes row

#Overwrites row

#windows wsl2 - Windows 11 - ubuntu linux

'''

















#data2 = {'Set':1,'Reps':12,'Weight':185,'Date':'05/30/23','Max Lift':-1,'Body Weight':200,'Fat%':20,'Phase':'cutting',
#        'Completed':'Yes','Notes':'Test'}