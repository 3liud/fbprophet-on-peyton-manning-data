import pandas as pd 
from fbprophet import Prophet

df = pd.read_csv('peyton_manning.csv', sep='delimiter', engine = 'python' )
print(df.head())