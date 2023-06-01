import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sb
import glob,os
from Date import formattedDate


df = pd.DataFrame(pd.read_csv('CSV/data.csv'))

data = {'Set':1,'Reps':12,'Weight':185,'Date':'05/30/23','Max Lift':-1,'Body Weight':200,'Fat%':20,'Phase':'cutting',
        'Completed':'Yes','Notes':'Test'}

print(os.listdir("CSVs"))

#User input for data
data2 = {i:input(f'{i} ') if i != 'Date' else formattedDate for i in df}

#windows wsl2 - Windows 11 - ubuntu linux

print(data2)