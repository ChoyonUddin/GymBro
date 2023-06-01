import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sb
import glob,os,csv
from Date import formattedDate
from CreateCSV import Headers
#Temporary class

#df = pd.DataFrame(pd.read_csv('CSVs/Bench_Press.csv'))

#User input for data testing

#Creates new row to enter data for the csv
data = {i:[input(f'{i} ')] if i != 'Date' else [formattedDate] for i in Headers}
pd.DataFrame(data).to_csv('CSVs/Bench_Press.csv',mode='a',index=False,header=False)

#Removes row

#Overwrites row
#windows wsl2 - Windows 11 - ubuntu linux



















#data2 = {'Set':1,'Reps':12,'Weight':185,'Date':'05/30/23','Max Lift':-1,'Body Weight':200,'Fat%':20,'Phase':'cutting',
#        'Completed':'Yes','Notes':'Test'}