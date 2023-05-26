from main import np,sb,mpl,pd
#will change var names later
data = pd.read_csv('Exercise List.csv')
print(data)

df = pd.DataFrame(data)

newdf = df.copy()

newdf.to_csv('data.csv')


print(df)