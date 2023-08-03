import pandas as pd
import numpy as np
import os

os.chdir("") # change to the direct path to your .csv files 
filenames = [ f for f in os.listdir( os.curdir ) if os.path.isfile(f) ]
len(filenames)

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

com_ecg_dict120 = {}

for file in files120:
     com_ecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 114, skipfooter = 0)
     com_ecg = com_ecg[~com_ecg[0].str.contains("Minnesota", na=False)]
     row = com_ecg[com_ecg[0] == 'Comments:'].index.tolist()[0]
     com_ecg.reset_index(drop=True, inplace=True)
     com_ecg_T = com_ecg.T
     if com_ecg.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_ecg_T.columns).all():
       com_ecg = com_ecg.T
       com_ecg.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_ecg = com_ecg.drop(columns=['drop1', 'drop2'])
       com_ecg = com_ecg.join(com_ecg['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_ecg = com_ecg.join(com_ecg['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_ecg = com_ecg.drop(columns=['ST_seg_1'])
       com_ecg = com_ecg.drop(columns=['ST_seg_2'])
     else:
       pass
     com_ecg['EcgID']=file
     cols = list(com_ecg.columns)
     cols = [cols[-1]] + cols[:-1]
     com_ecg = com_ecg[cols]
     com_ecg_dict120.update({file: com_ecg})
     
com_ecg_df = pd.concat(com_ecg_dict120) 
com_ecg_df['EcgID'] = com_ecg_df['EcgID'].str.replace(r'.txt','')
com_ecg_df.columns.name = None
com_ecg_df.to_csv('Output/end_comms/com_ecg_120_df.csv', index=False) 

com_ecg_dict121 = {}

for file in files121:
     com_ecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 114, skipfooter = 0)
     com_ecg = com_ecg[~com_ecg[0].str.contains("Minnesota", na=False)]
     row = com_ecg[com_ecg[0] == 'Comments:'].index.tolist()[0]
     com_ecg.reset_index(drop=True, inplace=True)
     com_ecg_T = com_ecg.T
     if com_ecg.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_ecg_T.columns).all():
       com_ecg = com_ecg.T
       com_ecg.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_ecg = com_ecg.drop(columns=['drop1', 'drop2'])
       com_ecg = com_ecg.join(com_ecg['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_ecg = com_ecg.join(com_ecg['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_ecg = com_ecg.drop(columns=['ST_seg_1'])
       com_ecg = com_ecg.drop(columns=['ST_seg_2'])
     else:
       pass
     com_ecg['EcgID']=file
     cols = list(com_ecg.columns)
     cols = [cols[-1]] + cols[:-1]
     com_ecg = com_ecg[cols]
     com_ecg_dict121.update({file: com_ecg})
     
com_ecg_df = pd.concat(com_ecg_dict121) 
com_ecg_df['EcgID'] = com_ecg_df['EcgID'].str.replace(r'.txt','')
com_ecg_df.columns.name = None
com_ecg_df.to_csv('Output/end_comms/com_ecg_121_df.csv', index=False) 

com_ecg_dict122 = {}

for file in files122:
     com_ecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 112, skipfooter = 0)
     com_ecg = com_ecg[~com_ecg[0].str.contains("Minnesota", na=False)]
     row = com_ecg[com_ecg[0] == 'Comments:'].index.tolist()[0]
     com_ecg.reset_index(drop=True, inplace=True)
     com_ecg_T = com_ecg.T
     if com_ecg.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_ecg_T.columns).all():
       com_ecg = com_ecg.T
       com_ecg.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_ecg = com_ecg.drop(columns=['drop1', 'drop2'])
       com_ecg = com_ecg.join(com_ecg['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_ecg = com_ecg.join(com_ecg['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_ecg = com_ecg.drop(columns=['ST_seg_1'])
       com_ecg = com_ecg.drop(columns=['ST_seg_2'])
     else:
       pass
     com_ecg['EcgID']=file
     cols = list(com_ecg.columns)
     cols = [cols[-1]] + cols[:-1]
     com_ecg = com_ecg[cols]
     com_ecg_dict122.update({file: com_ecg})
     
com_ecg_df = pd.concat(com_ecg_dict122) 
com_ecg_df['EcgID'] = com_ecg_df['EcgID'].str.replace(r'.txt','')
com_ecg_df.columns.name = None
com_ecg_df.to_csv('Output/end_comms/com_ecg_122_df.csv', index=False) 

com_ecg_dict123 = {}

for file in files123:
     com_ecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 112, skipfooter = 0)
     com_ecg = com_ecg[~com_ecg[0].str.contains("Minnesota", na=False)]
     row = com_ecg[com_ecg[0] == 'Comments:'].index.tolist()[0]
     com_ecg.reset_index(drop=True, inplace=True)
     com_ecg_T = com_ecg.T
     if com_ecg.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_ecg_T.columns).all():
       com_ecg = com_ecg.T
       com_ecg.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_ecg = com_ecg.drop(columns=['drop1', 'drop2'])
       com_ecg = com_ecg.join(com_ecg['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_ecg = com_ecg.join(com_ecg['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_ecg = com_ecg.drop(columns=['ST_seg_1'])
       com_ecg = com_ecg.drop(columns=['ST_seg_2'])
     else:
       pass
     com_ecg['EcgID']=file
     cols = list(com_ecg.columns)
     cols = [cols[-1]] + cols[:-1]
     com_ecg = com_ecg[cols]
     com_ecg_dict123.update({file: com_ecg})
     
com_ecg_df = pd.concat(com_ecg_dict123) 
com_ecg_df['EcgID'] = com_ecg_df['EcgID'].str.replace(r'.txt','')
com_ecg_df.columns.name = None
com_ecg_df.to_csv('Output/end_comms/com_ecg_123_df.csv', index=False) 

com_ecg_dict124 = {}

for file in files124:
     com_ecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 114, skipfooter = 0)
     com_ecg = com_ecg[~com_ecg[0].str.contains("Minnesota", na=False)]
     row = com_ecg[com_ecg[0] == 'Comments:'].index.tolist()[0]
     com_ecg.reset_index(drop=True, inplace=True)
     com_ecg_T = com_ecg.T
     if com_ecg.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_ecg_T.columns).all():
       com_ecg = com_ecg.T
       com_ecg.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_ecg = com_ecg.drop(columns=['drop1', 'drop2'])
       com_ecg = com_ecg.join(com_ecg['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_ecg = com_ecg.join(com_ecg['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_ecg = com_ecg.drop(columns=['ST_seg_1'])
       com_ecg = com_ecg.drop(columns=['ST_seg_2'])
     else:
       pass
     com_ecg['EcgID']=file
     cols = list(com_ecg.columns)
     cols = [cols[-1]] + cols[:-1]
     com_ecg = com_ecg[cols]
     com_ecg_dict124.update({file: com_ecg})
     
com_ecg_df = pd.concat(com_ecg_dict124) 
com_ecg_df['EcgID'] = com_ecg_df['EcgID'].str.replace(r'.txt','')
com_ecg_df.columns.name = None
com_ecg_df.to_csv('Output/end_comms/com_ecg_124_df.csv', index=False)

com_ecg_dict125 = {}

for file in files125:
     com_ecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 114, skipfooter = 0)
     com_ecg = com_ecg[~com_ecg[0].str.contains("Minnesota", na=False)]
     row = com_ecg[com_ecg[0] == 'Comments:'].index.tolist()[0]
     com_ecg.reset_index(drop=True, inplace=True)
     com_ecg_T = com_ecg.T
     if com_ecg.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_ecg_T.columns).all():
       com_ecg = com_ecg.T
       com_ecg.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_ecg = com_ecg.drop(columns=['drop1', 'drop2'])
       com_ecg = com_ecg.join(com_ecg['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_ecg = com_ecg.join(com_ecg['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_ecg = com_ecg.drop(columns=['ST_seg_1'])
       com_ecg = com_ecg.drop(columns=['ST_seg_2'])
     else:
       pass
     com_ecg['EcgID']=file
     cols = list(com_ecg.columns)
     cols = [cols[-1]] + cols[:-1]
     com_ecg = com_ecg[cols]
     com_ecg_dict125.update({file: com_ecg})
     
com_ecg_df = pd.concat(com_ecg_dict125) 
com_ecg_df['EcgID'] = com_ecg_df['EcgID'].str.replace(r'.txt','')
com_ecg_df.columns.name = None
com_ecg_df.to_csv('Output/end_comms/com_ecg_125_df.csv', index=False)


com_ecg_dict127 = {}

for file in files127:
     com_ecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 116, skipfooter = 0)
     com_ecg = com_ecg[~com_ecg[0].str.contains("Minnesota", na=False)]
     row = com_ecg[com_ecg[0] == 'Comments:'].index.tolist()[0]
     com_ecg.reset_index(drop=True, inplace=True)
     com_ecg_T = com_ecg.T
     if com_ecg.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_ecg_T.columns).all():
       com_ecg = com_ecg.T
       com_ecg.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_ecg = com_ecg.drop(columns=['drop1', 'drop2'])
       com_ecg = com_ecg.join(com_ecg['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_ecg = com_ecg.join(com_ecg['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_ecg = com_ecg.drop(columns=['ST_seg_1'])
       com_ecg = com_ecg.drop(columns=['ST_seg_2'])
     else:
       pass
     com_ecg['EcgID']=file
     cols = list(com_ecg.columns)
     cols = [cols[-1]] + cols[:-1]
     com_ecg = com_ecg[cols]
     com_ecg_dict127.update({file: com_ecg})
     
com_ecg_df = pd.concat(com_ecg_dict127) 
com_ecg_df['EcgID'] = com_ecg_df['EcgID'].str.replace(r'.txt','')
com_ecg_df.columns.name = None
com_ecg_df.to_csv('Output/end_comms/com_ecg_127_df.csv', index=False)

com_ecg_dict128 = {}

for file in files128:
     com_ecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 118, skipfooter = 0)
     com_ecg = com_ecg[~com_ecg[0].str.contains("Minnesota", na=False)]
     row = com_ecg[com_ecg[0] == 'Comments:'].index.tolist()[0]
     com_ecg.reset_index(drop=True, inplace=True)
     com_ecg_T = com_ecg.T
     if com_ecg.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_ecg_T.columns).all():
       com_ecg = com_ecg.T
       com_ecg.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_ecg = com_ecg.drop(columns=['drop1', 'drop2'])
       com_ecg = com_ecg.join(com_ecg['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_ecg = com_ecg.join(com_ecg['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_ecg = com_ecg.drop(columns=['ST_seg_1'])
       com_ecg = com_ecg.drop(columns=['ST_seg_2'])
     else:
       pass
     com_ecg['EcgID']=file
     cols = list(com_ecg.columns)
     cols = [cols[-1]] + cols[:-1]
     com_ecg = com_ecg[cols]
     com_ecg_dict128.update({file: com_ecg})
     
com_ecg_df = pd.concat(com_ecg_dict128) 
com_ecg_df['EcgID'] = com_ecg_df['EcgID'].str.replace(r'.txt','')
com_ecg_df.columns.name = None
com_ecg_df.to_csv('Output/end_comms/com_ecg_128_df.csv', index=False)

com_ecg_dict129 = {}

for file in files129:
     com_ecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 118, skipfooter = 0)
     com_ecg = com_ecg[~com_ecg[0].str.contains("Minnesota", na=False)]
     row = com_ecg[com_ecg[0] == 'Comments:'].index.tolist()[0]
     com_ecg.reset_index(drop=True, inplace=True)
     com_ecg_T = com_ecg.T
     if com_ecg.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_ecg_T.columns).all():
       com_ecg = com_ecg.T
       com_ecg.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_ecg = com_ecg.drop(columns=['drop1', 'drop2'])
       com_ecg = com_ecg.join(com_ecg['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_ecg = com_ecg.join(com_ecg['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_ecg = com_ecg.drop(columns=['ST_seg_1'])
       com_ecg = com_ecg.drop(columns=['ST_seg_2'])
     else:
       pass
     com_ecg['EcgID']=file
     cols = list(com_ecg.columns)
     cols = [cols[-1]] + cols[:-1]
     com_ecg = com_ecg[cols]
     com_ecg_dict129.update({file: com_ecg})
     
com_ecg_df = pd.concat(com_ecg_dict129) 
com_ecg_df['EcgID'] = com_ecg_df['EcgID'].str.replace(r'.txt','')
com_ecg_df.columns.name = None
com_ecg_df.to_csv('Output/end_comms/com_ecg_129_df.csv', index=False)

com_ecg_dict130 = {}

for file in files130:
     com_ecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 120, skipfooter = 0)
     com_ecg = com_ecg[~com_ecg[0].str.contains("Minnesota", na=False)]
     row = com_ecg[com_ecg[0] == 'Comments:'].index.tolist()[0]
     com_ecg.reset_index(drop=True, inplace=True)
     com_ecg_T = com_ecg.T
     if com_ecg.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_ecg_T.columns).all():
       com_ecg = com_ecg.T
       com_ecg.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_ecg = com_ecg.drop(columns=['drop1', 'drop2'])
       com_ecg = com_ecg.join(com_ecg['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_ecg = com_ecg.join(com_ecg['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_ecg = com_ecg.drop(columns=['ST_seg_1'])
       com_ecg = com_ecg.drop(columns=['ST_seg_2'])
     else:
       pass
     com_ecg['EcgID']=file
     cols = list(com_ecg.columns)
     cols = [cols[-1]] + cols[:-1]
     com_ecg = com_ecg[cols]
     com_ecg_dict130.update({file: com_ecg})
     
com_ecg_df = pd.concat(com_ecg_dict130) 
com_ecg_df['EcgID'] = com_ecg_df['EcgID'].str.replace(r'.txt','')
com_ecg_df.columns.name = None
com_ecg_df.to_csv('Output/end_comms/com_ecg_130_df.csv', index=False)


com_ecg_dict131 = {}

for file in files131:
     com_ecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 120, skipfooter = 0)
     com_ecg = com_ecg[~com_ecg[0].str.contains("Minnesota", na=False)]
     row = com_ecg[com_ecg[0] == 'Comments:'].index.tolist()[0]
     com_ecg.reset_index(drop=True, inplace=True)
     com_ecg_T = com_ecg.T
     if com_ecg.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_ecg_T.columns).all():
       com_ecg = com_ecg.T
       com_ecg.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_ecg = com_ecg.drop(columns=['drop1', 'drop2'])
       com_ecg = com_ecg.join(com_ecg['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_ecg = com_ecg.join(com_ecg['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_ecg = com_ecg.drop(columns=['ST_seg_1'])
       com_ecg = com_ecg.drop(columns=['ST_seg_2'])
     else:
       pass
     com_ecg['EcgID']=file
     cols = list(com_ecg.columns)
     cols = [cols[-1]] + cols[:-1]
     com_ecg = com_ecg[cols]
     com_ecg_dict131.update({file: com_ecg})
     
com_ecg_df = pd.concat(com_ecg_dict131) 
com_ecg_df['EcgID'] = com_ecg_df['EcgID'].str.replace(r'.txt','')
com_ecg_df.columns.name = None
com_ecg_df.to_csv('Output/end_comms/com_ecg_131_df.csv', index=False)
