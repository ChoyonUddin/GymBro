import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sb

df = pd.DataFrame((pd.read_csv('data.csv')))
print(df.head(5))
print(df.head(5).fillna("This value is missing"))