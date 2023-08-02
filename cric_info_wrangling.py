import numpy as np
import pandas as pd
import os

os.chdir("") # change to the direct path to your .csv files 
filenames = [ f for f in os.listdir( os.curdir ) if os.path.isfile(f) ]

dict1 = {}

for file in filenames:
     demo = pd.read_fwf(file, header= None,colspecs = [(0, 100)])
     demo[['Variable','Value']] = demo[0].str.split(':',expand=True)
     demo = demo.drop(columns=[0])
     demo = demo.set_index('Variable').T
     demo['EcgID']=file
     dict1.update({file: demo})

df = pd.concat(dict1) 

df['EcgID'] = df['EcgID'].str.replace(r'.txt','')
df.columns.name = None

df.to_csv('Output/CRIC_INFO_DEMO.csv', index=False)  


