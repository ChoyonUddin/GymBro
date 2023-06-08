import pandas as pd
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import seaborn as sb
import glob,os,csv
from Date import formattedDate
from CreateCSV import Headers
from main import df
#takes range of data from one column
def linegraph(data,x,y):
    sb.lineplot(data,x=x,y=y)
    plt.show()
linegraph(data=df,x='Set',y='Weight')