import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sb
import glob,os,csv
from Date import formattedDate
from CreateCSV import Headers
from tkinter import *
#user input the way I want it 
df = pd.DataFrame(pd.read_csv('CSVs/Bench_Press.csv'))
#print(df)

#Tkinter stuff
root = Tk()

#Labels
e = Entry(root,border=5,borderwidth=5,bg='white',fg='blue')
e.pack()
def onClick():
    my_label = Label(root,text= e.get())#.grid(column=1,row=1)
    my_label.pack()

#Button
my_button = Button(root,text="Click Me",command=onClick)
my_button.pack()

root.mainloop()

