import pandas as pd
import numpy as np
import os

os.chdir("") # change to the direct path to your .csv files 
filenames = [ f for f in os.listdir( os.curdir ) if os.path.isfile(f) ]




files120 = []
files121 = []
files122 = []
files123 = []
files124 = []
files125 = []
files127 = []
files128 = []
files129 = []
files130 = []
files131 = []
filesUnknown = []

for file in filenames:
     text = pd.read_fwf(file, header= None)
     linenumber =  text.shape[0]
     if linenumber == 120:
       files120.append(file)
     elif linenumber == 121:
       files121.append(file)
     elif linenumber == 122:
       files122.append(file)
     elif linenumber == 123:
       files123.append(file)
     elif linenumber == 124:
       files124.append(file)
     elif linenumber == 125:
       files125.append(file)
     elif linenumber == 127:
       files127.append(file)
     elif linenumber == 128:
       files128.append(file)
     elif linenumber == 129:
       files129.append(file)
     elif linenumber == 130:
       files130.append(file)
     elif linenumber == 131:
       files131.append(file)
     else:
       filesUnknown.append(file)

len(filenames)

len(files120)
len(files121)
len(files122)
len(files123)
len(files124)
len(files125)
len(files127)
len(files128)
len(files129)
len(files130)
len(files131)
len(filesUnknown)






id_datetime_dict120 = {}

for file in files120:
     id_datetime = pd.read_fwf(file, header= None, colspecs = [(0, 17),(17,50)], names = ['id_101','ECG_DateTime'],skiprows = 1, skipfooter = 118)
     id_datetime['EcgID']=file
     id_datetime_dict120.update({file: id_datetime})
     
id_datetime120_df = pd.concat(id_datetime_dict120) 
id_datetime120_df['EcgID'] = id_datetime120_df['EcgID'].str.replace(r'.txt','')
id_datetime120_df.columns.name = None
id_datetime120_df.to_csv('Output/datetime/id_datetime120_df.csv', index=False) 


id_datetime_dict121 = {}

for file in files121:
     id_datetime = pd.read_fwf(file, header= None, colspecs = [(0, 17),(17,50)], names = ['id_101','ECG_DateTime'],skiprows = 1, skipfooter = 119)
     id_datetime['EcgID']=file
     id_datetime_dict121.update({file: id_datetime})
     
id_datetime121_df = pd.concat(id_datetime_dict121) 
id_datetime121_df['EcgID'] = id_datetime121_df['EcgID'].str.replace(r'.txt','')
id_datetime121_df.columns.name = None
id_datetime121_df.to_csv('Output/datetime/id_datetime121_df.csv', index=False)


id_datetime_dict122 = {}

for file in files122:
     id_datetime = pd.read_fwf(file, header= None, colspecs = [(0, 17),(17,50)], names = ['id_101','ECG_DateTime'],skiprows = 1, skipfooter = 120)
     id_datetime['EcgID']=file
     id_datetime_dict122.update({file: id_datetime})
     
id_datetime122_df = pd.concat(id_datetime_dict122) 
id_datetime122_df['EcgID'] = id_datetime122_df['EcgID'].str.replace(r'.txt','')
id_datetime122_df.columns.name = None
id_datetime122_df.to_csv('Output/datetime/id_datetime122_df.csv', index=False) 

id_datetime_dict123 = {}

for file in files123:
     id_datetime = pd.read_fwf(file, header= None, colspecs = [(0, 17),(17,50)], names = ['id_101','ECG_DateTime'],skiprows = 1, skipfooter = 121)
     id_datetime['EcgID']=file
     id_datetime_dict123.update({file: id_datetime})
     
id_datetime123_df = pd.concat(id_datetime_dict123) 
id_datetime123_df['EcgID'] = id_datetime123_df['EcgID'].str.replace(r'.txt','')
id_datetime123_df.columns.name = None
id_datetime123_df.to_csv('Output/datetime/id_datetime123_df.csv', index=False) 


id_datetime_dict124 = {}

for file in files124:
     id_datetime = pd.read_fwf(file, header= None, colspecs = [(0, 17),(17,50)], names = ['id_101','ECG_DateTime'],skiprows = 1, skipfooter = 122)
     id_datetime['EcgID']=file
     id_datetime_dict124.update({file: id_datetime})
     
id_datetime124_df = pd.concat(id_datetime_dict124) 
id_datetime124_df['EcgID'] = id_datetime124_df['EcgID'].str.replace(r'.txt','')
id_datetime124_df.columns.name = None
id_datetime124_df.to_csv('Output/datetime/id_datetime124_df.csv', index=False) 

id_datetime_dict125 = {}

for file in files125:
     id_datetime = pd.read_fwf(file, header= None, colspecs = [(0, 17),(17,50)], names = ['id_101','ECG_DateTime'],skiprows = 1, skipfooter = 123)
     id_datetime['EcgID']=file
     id_datetime_dict125.update({file: id_datetime})
     
id_datetime125_df = pd.concat(id_datetime_dict125) 
id_datetime125_df['EcgID'] = id_datetime125_df['EcgID'].str.replace(r'.txt','')
id_datetime125_df.columns.name = None
id_datetime125_df.to_csv('Output/datetime/id_datetime125_df.csv', index=False) 

id_datetime_dict127 = {}

for file in files127:
     id_datetime = pd.read_fwf(file, header= None, colspecs = [(0, 17),(17,50)], names = ['id_101','ECG_DateTime'],skiprows = 1, skipfooter = 125)
     id_datetime['EcgID']=file
     id_datetime_dict127.update({file: id_datetime})
     
id_datetime127_df = pd.concat(id_datetime_dict127) 
id_datetime127_df['EcgID'] = id_datetime127_df['EcgID'].str.replace(r'.txt','')
id_datetime127_df.columns.name = None
id_datetime127_df.to_csv('Output/datetime/id_datetime127_df.csv', index=False) 


id_datetime_dict128 = {}

for file in files128:
     id_datetime = pd.read_fwf(file, header= None, colspecs = [(0, 17),(17,50)], names = ['id_101','ECG_DateTime'],skiprows = 1, skipfooter = 126)
     id_datetime['EcgID']=file
     id_datetime_dict128.update({file: id_datetime})
     
id_datetime128_df = pd.concat(id_datetime_dict128) 
id_datetime128_df['EcgID'] = id_datetime128_df['EcgID'].str.replace(r'.txt','')
id_datetime128_df.columns.name = None
id_datetime128_df.to_csv('Output/datetime/id_datetime128_df.csv', index=False) 

id_datetime_dict129 = {}

for file in files129:
     id_datetime = pd.read_fwf(file, header= None, colspecs = [(0, 17),(17,50)], names = ['id_101','ECG_DateTime'],skiprows = 1, skipfooter = 127)
     id_datetime['EcgID']=file
     id_datetime_dict129.update({file: id_datetime})
     
id_datetime129_df = pd.concat(id_datetime_dict129) 
id_datetime129_df['EcgID'] = id_datetime129_df['EcgID'].str.replace(r'.txt','')
id_datetime129_df.columns.name = None
id_datetime129_df.to_csv('Output/datetime/id_datetime129_df.csv', index=False) 

id_datetime_dict130 = {}

for file in files130:
     id_datetime = pd.read_fwf(file, header= None, colspecs = [(0, 17),(17,50)], names = ['id_101','ECG_DateTime'],skiprows = 1, skipfooter = 128)
     id_datetime['EcgID']=file
     id_datetime_dict130.update({file: id_datetime})
     
id_datetime130_df = pd.concat(id_datetime_dict130) 
id_datetime130_df['EcgID'] = id_datetime130_df['EcgID'].str.replace(r'.txt','')
id_datetime130_df.columns.name = None
id_datetime130_df.to_csv('Output/datetime/id_datetime130_df.csv', index=False)


id_datetime_dict131 = {}

for file in files131:
     id_datetime = pd.read_fwf(file, header= None, colspecs = [(0, 17),(17,50)], names = ['id_101','ECG_DateTime'],skiprows = 1, skipfooter = 129)
     id_datetime['EcgID']=file
     id_datetime_dict131.update({file: id_datetime})
     
id_datetime131_df = pd.concat(id_datetime_dict131) 
id_datetime131_df['EcgID'] = id_datetime131_df['EcgID'].str.replace(r'.txt','')
id_datetime131_df.columns.name = None
id_datetime131_df.to_csv('Output/datetime/id_datetime131_df.csv', index=False)





