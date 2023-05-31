import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sb
import glob,os
import Date


df = pd.DataFrame(pd.read_csv('CSVs\Bench Press.csv'))
columns = list(df.columns)

data = {'Set':1,'Reps':12,'Weight':185,'Date':'05/30/23','Max Lift':-1,'Body Weight':200,'Fat%':20,'Phase':'cutting',
        'Completed':'Yes','Notes':'Test'}

#data2 = {i:input(f'{i} ') for i in df}

#windows wsl2 - Windows 11 - ubuntu linux

#print(data2)