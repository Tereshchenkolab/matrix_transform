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


pqrst_dict120 = {}

for file in files120:
     pqrst = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 82, skipfooter = 31)
     if pqrst.shape[0] > 6:
       pqrst = pqrst.tail(-1)
     else:
        pass
     pqrst[['Variable','Value']] = pqrst[0].str.split("\\s+",expand=True)
     pqrst = pqrst.drop(columns=[0])
     pqrst = pqrst.set_index('Variable').T
     pqrst['EcgID']=file
     pqrst_dict120.update({file: pqrst})
     
pqrst_120_df = pd.concat(pqrst_dict120) 
pqrst_120_df['EcgID'] = pqrst_120_df['EcgID'].str.replace(r'.txt','')
pqrst_120_df.columns.name = None
pqrst_120_df.to_csv('Output/pqrst/pqrst_120_df.csv', index=False) 

pqrst_dict121 = {}

for file in files121:
     pqrst = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 82, skipfooter = 31)
     if pqrst.shape[0] > 6:
       pqrst = pqrst.tail(-1)
     else:
        pass
     pqrst[['Variable','Value']] = pqrst[0].str.split("\\s+",expand=True)
     pqrst = pqrst.drop(columns=[0])
     pqrst = pqrst.set_index('Variable').T
     pqrst['EcgID']=file
     pqrst_dict121.update({file: pqrst})
     
pqrst_121_df = pd.concat(pqrst_dict121) 
pqrst_121_df['EcgID'] = pqrst_121_df['EcgID'].str.replace(r'.txt','')
pqrst_121_df.columns.name = None
pqrst_121_df.to_csv('Output/pqrst/pqrst_121_df.csv', index=False) 

pqrst_dict122 = {}

for file in files122:
     pqrst = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 82, skipfooter = 31)
     if pqrst.shape[0] > 6:
       pqrst = pqrst.tail(-1)
     else:
        pass
     pqrst[['Variable','Value']] = pqrst[0].str.split("\\s+",expand=True)
     pqrst = pqrst.drop(columns=[0])
     pqrst = pqrst.set_index('Variable').T
     pqrst['EcgID']=file
     pqrst_dict122.update({file: pqrst})
     
pqrst_122_df = pd.concat(pqrst_dict122) 
pqrst_122_df['EcgID'] = pqrst_122_df['EcgID'].str.replace(r'.txt','')
pqrst_122_df.columns.name = None
pqrst_122_df.to_csv('Output/pqrst/pqrst_122_df.csv', index=False) 

pqrst_dict123 = {}

for file in files123:
     pqrst = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 82, skipfooter = 32)
     if pqrst.shape[0] > 6:
       pqrst = pqrst.tail(-1)
     else:
        pass
     pqrst[['Variable','Value']] = pqrst[0].str.split("\\s+",expand=True)
     pqrst = pqrst.drop(columns=[0])
     pqrst = pqrst.set_index('Variable').T
     pqrst['EcgID']=file
     pqrst_dict123.update({file: pqrst})
     
pqrst_123_df = pd.concat(pqrst_dict123) 
pqrst_123_df['EcgID'] = pqrst_123_df['EcgID'].str.replace(r'.txt','')
pqrst_123_df.columns.name = None
pqrst_123_df.to_csv('Output/pqrst/pqrst_123_df.csv', index=False) 

pqrst_dict124 = {}

for file in files124:
     pqrst = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 82, skipfooter = 33)
     if pqrst.shape[0] > 6:
       pqrst = pqrst.tail(-1)
     else:
        pass
     pqrst[['Variable','Value']] = pqrst[0].str.split("\\s+",expand=True)
     pqrst = pqrst.drop(columns=[0])
     pqrst = pqrst.set_index('Variable').T
     pqrst['EcgID']=file
     pqrst_dict124.update({file: pqrst})
     
pqrst_124_df = pd.concat(pqrst_dict124) 
pqrst_124_df['EcgID'] = pqrst_124_df['EcgID'].str.replace(r'.txt','')
pqrst_124_df.columns.name = None
pqrst_124_df.to_csv('Output/pqrst/pqrst_124_df.csv', index=False)

pqrst_dict125 = {}

for file in files125:
     pqrst = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 82, skipfooter = 34)
     if pqrst.shape[0] > 6:
       pqrst = pqrst.tail(-1)
     else:
        pass
     pqrst[['Variable','Value']] = pqrst[0].str.split("\\s+",expand=True)
     pqrst = pqrst.drop(columns=[0])
     pqrst = pqrst.set_index('Variable').T
     pqrst['EcgID']=file
     pqrst_dict125.update({file: pqrst})
     
pqrst_125_df = pd.concat(pqrst_dict125) 
pqrst_125_df['EcgID'] = pqrst_125_df['EcgID'].str.replace(r'.txt','')
pqrst_125_df.columns.name = None
pqrst_125_df.to_csv('Output/pqrst/pqrst_125_df.csv', index=False)

pqrst_dict127 = {}

for file in files127:
     pqrst = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 82, skipfooter = 37)
     if pqrst.shape[0] > 6:
       pqrst = pqrst.tail(-1)
     else:
        pass
     pqrst[['Variable','Value']] = pqrst[0].str.split("\\s+",expand=True)
     pqrst = pqrst.drop(columns=[0])
     pqrst = pqrst.set_index('Variable').T
     pqrst['EcgID']=file
     pqrst_dict127.update({file: pqrst})
     
pqrst_127_df = pd.concat(pqrst_dict127) 
pqrst_127_df['EcgID'] = pqrst_127_df['EcgID'].str.replace(r'.txt','')
pqrst_127_df.columns.name = None
pqrst_127_df.to_csv('Output/pqrst/pqrst_127_df.csv', index=False)

pqrst_dict128 = {}

for file in files128:
     pqrst = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 82, skipfooter = 38)
     if pqrst.shape[0] > 6:
       pqrst = pqrst.tail(-1)
     else:
        pass
     pqrst[['Variable','Value']] = pqrst[0].str.split("\\s+",expand=True)
     pqrst = pqrst.drop(columns=[0])
     pqrst = pqrst.set_index('Variable').T
     pqrst['EcgID']=file
     pqrst_dict128.update({file: pqrst})
     
pqrst_128_df = pd.concat(pqrst_dict128) 
pqrst_128_df['EcgID'] = pqrst_128_df['EcgID'].str.replace(r'.txt','')
pqrst_128_df.columns.name = None
pqrst_128_df.to_csv('Output/pqrst/pqrst_128_df.csv', index=False)

pqrst_dict129 = {}

for file in files129:
     pqrst = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 82, skipfooter = 39)
     if pqrst.shape[0] > 6:
       pqrst = pqrst.tail(-1)
     else:
        pass
     pqrst[['Variable','Value']] = pqrst[0].str.split("\\s+",expand=True)
     pqrst = pqrst.drop(columns=[0])
     pqrst = pqrst.set_index('Variable').T
     pqrst['EcgID']=file
     pqrst_dict129.update({file: pqrst})
     
pqrst_129_df = pd.concat(pqrst_dict129) 
pqrst_129_df['EcgID'] = pqrst_129_df['EcgID'].str.replace(r'.txt','')
pqrst_129_df.columns.name = None
pqrst_129_df.to_csv('Output/pqrst/pqrst_129_df.csv', index=False)

pqrst_dict130 = {}

for file in files130:
     pqrst = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 82, skipfooter = 40)
     if pqrst.shape[0] > 6:
       pqrst = pqrst.tail(-1)
     else:
        pass
     pqrst[['Variable','Value']] = pqrst[0].str.split("\\s+",expand=True)
     pqrst = pqrst.drop(columns=[0])
     pqrst = pqrst.set_index('Variable').T
     pqrst['EcgID']=file
     pqrst_dict130.update({file: pqrst})
     
pqrst_130_df = pd.concat(pqrst_dict130) 
pqrst_130_df['EcgID'] = pqrst_130_df['EcgID'].str.replace(r'.txt','')
pqrst_130_df.columns.name = None
pqrst_130_df.to_csv('Output/pqrst/pqrst_130_df.csv', index=False)

pqrst_dict131 = {}

for file in files131:
     pqrst = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 82, skipfooter = 41)
     if pqrst.shape[0] > 6:
       pqrst = pqrst.tail(-1)
     else:
        pass
     pqrst[['Variable','Value']] = pqrst[0].str.split("\\s+",expand=True)
     pqrst = pqrst.drop(columns=[0])
     pqrst = pqrst.set_index('Variable').T
     pqrst['EcgID']=file
     pqrst_dict131.update({file: pqrst})
     
pqrst_131_df = pd.concat(pqrst_dict131) 
pqrst_131_df['EcgID'] = pqrst_131_df['EcgID'].str.replace(r'.txt','')
pqrst_131_df.columns.name = None
pqrst_131_df.to_csv('Output/pqrst/pqrst_131_df.csv', index=False)
