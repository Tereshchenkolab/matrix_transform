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

com_12sl_dict120 = {}

for file in files120:
     com_12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 114, skipfooter = 0)
     com_12sl = com_12sl[~com_12sl[0].str.contains("Minnesota", na=False)]
     row = com_12sl[com_12sl[0] == 'Comments:'].index.tolist()[0]
     com_12sl.reset_index(drop=True, inplace=True)
     com_12sl_T = com_12sl.T
     if com_12sl.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_12sl_T.columns).all():
       com_12sl = com_12sl.T
       com_12sl.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_12sl = com_12sl.drop(columns=['drop1', 'drop2'])
       com_12sl = com_12sl.join(com_12sl['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_12sl = com_12sl.join(com_12sl['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_12sl = com_12sl.drop(columns=['ST_seg_1'])
       com_12sl = com_12sl.drop(columns=['ST_seg_2'])
     else:
       pass
     com_12sl['EcgID']=file
     cols = list(com_12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     com_12sl = com_12sl[cols]
     com_12sl_dict120.update({file: com_12sl})
     
com_12sl_df = pd.concat(com_12sl_dict120) 
com_12sl_df['EcgID'] = com_12sl_df['EcgID'].str.replace(r'.txt','')
com_12sl_df.columns.name = None
com_12sl_df.to_csv('Output/end_comms/com_12sl_120_df.csv', index=False) 

com_12sl_dict121 = {}

for file in files121:
     com_12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 114, skipfooter = 0)
     com_12sl = com_12sl[~com_12sl[0].str.contains("Minnesota", na=False)]
     row = com_12sl[com_12sl[0] == 'Comments:'].index.tolist()[0]
     com_12sl.reset_index(drop=True, inplace=True)
     com_12sl_T = com_12sl.T
     if com_12sl.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_12sl_T.columns).all():
       com_12sl = com_12sl.T
       com_12sl.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_12sl = com_12sl.drop(columns=['drop1', 'drop2'])
       com_12sl = com_12sl.join(com_12sl['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_12sl = com_12sl.join(com_12sl['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_12sl = com_12sl.drop(columns=['ST_seg_1'])
       com_12sl = com_12sl.drop(columns=['ST_seg_2'])
     else:
       pass
     com_12sl['EcgID']=file
     cols = list(com_12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     com_12sl = com_12sl[cols]
     com_12sl_dict121.update({file: com_12sl})
     
com_12sl_df = pd.concat(com_12sl_dict121) 
com_12sl_df['EcgID'] = com_12sl_df['EcgID'].str.replace(r'.txt','')
com_12sl_df.columns.name = None
com_12sl_df.to_csv('Output/end_comms/com_12sl_121_df.csv', index=False) 

com_12sl_dict122 = {}

for file in files122:
     com_12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 112, skipfooter = 0)
     com_12sl = com_12sl[~com_12sl[0].str.contains("Minnesota", na=False)]
     row = com_12sl[com_12sl[0] == 'Comments:'].index.tolist()[0]
     com_12sl.reset_index(drop=True, inplace=True)
     com_12sl_T = com_12sl.T
     if com_12sl.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_12sl_T.columns).all():
       com_12sl = com_12sl.T
       com_12sl.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_12sl = com_12sl.drop(columns=['drop1', 'drop2'])
       com_12sl = com_12sl.join(com_12sl['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_12sl = com_12sl.join(com_12sl['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_12sl = com_12sl.drop(columns=['ST_seg_1'])
       com_12sl = com_12sl.drop(columns=['ST_seg_2'])
     else:
       pass
     com_12sl['EcgID']=file
     cols = list(com_12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     com_12sl = com_12sl[cols]
     com_12sl_dict122.update({file: com_12sl})
     
com_12sl_df = pd.concat(com_12sl_dict122) 
com_12sl_df['EcgID'] = com_12sl_df['EcgID'].str.replace(r'.txt','')
com_12sl_df.columns.name = None
com_12sl_df.to_csv('Output/end_comms/com_12sl_122_df.csv', index=False) 

com_12sl_dict123 = {}

for file in files123:
     com_12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 112, skipfooter = 0)
     com_12sl = com_12sl[~com_12sl[0].str.contains("Minnesota", na=False)]
     row = com_12sl[com_12sl[0] == 'Comments:'].index.tolist()[0]
     com_12sl.reset_index(drop=True, inplace=True)
     com_12sl_T = com_12sl.T
     if com_12sl.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_12sl_T.columns).all():
       com_12sl = com_12sl.T
       com_12sl.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_12sl = com_12sl.drop(columns=['drop1', 'drop2'])
       com_12sl = com_12sl.join(com_12sl['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_12sl = com_12sl.join(com_12sl['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_12sl = com_12sl.drop(columns=['ST_seg_1'])
       com_12sl = com_12sl.drop(columns=['ST_seg_2'])
     else:
       pass
     com_12sl['EcgID']=file
     cols = list(com_12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     com_12sl = com_12sl[cols]
     com_12sl_dict123.update({file: com_12sl})
     
com_12sl_df = pd.concat(com_12sl_dict123) 
com_12sl_df['EcgID'] = com_12sl_df['EcgID'].str.replace(r'.txt','')
com_12sl_df.columns.name = None
com_12sl_df.to_csv('Output/end_comms/com_12sl_123_df.csv', index=False) 

com_12sl_dict124 = {}

for file in files124:
     com_12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 114, skipfooter = 0)
     com_12sl = com_12sl[~com_12sl[0].str.contains("Minnesota", na=False)]
     row = com_12sl[com_12sl[0] == 'Comments:'].index.tolist()[0]
     com_12sl.reset_index(drop=True, inplace=True)
     com_12sl_T = com_12sl.T
     if com_12sl.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_12sl_T.columns).all():
       com_12sl = com_12sl.T
       com_12sl.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_12sl = com_12sl.drop(columns=['drop1', 'drop2'])
       com_12sl = com_12sl.join(com_12sl['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_12sl = com_12sl.join(com_12sl['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_12sl = com_12sl.drop(columns=['ST_seg_1'])
       com_12sl = com_12sl.drop(columns=['ST_seg_2'])
     else:
       pass
     com_12sl['EcgID']=file
     cols = list(com_12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     com_12sl = com_12sl[cols]
     com_12sl_dict124.update({file: com_12sl})
     
com_12sl_df = pd.concat(com_12sl_dict124) 
com_12sl_df['EcgID'] = com_12sl_df['EcgID'].str.replace(r'.txt','')
com_12sl_df.columns.name = None
com_12sl_df.to_csv('Output/end_comms/com_12sl_124_df.csv', index=False)

com_12sl_dict125 = {}

for file in files125:
     com_12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 114, skipfooter = 0)
     com_12sl = com_12sl[~com_12sl[0].str.contains("Minnesota", na=False)]
     row = com_12sl[com_12sl[0] == 'Comments:'].index.tolist()[0]
     com_12sl.reset_index(drop=True, inplace=True)
     com_12sl_T = com_12sl.T
     if com_12sl.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_12sl_T.columns).all():
       com_12sl = com_12sl.T
       com_12sl.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_12sl = com_12sl.drop(columns=['drop1', 'drop2'])
       com_12sl = com_12sl.join(com_12sl['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_12sl = com_12sl.join(com_12sl['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_12sl = com_12sl.drop(columns=['ST_seg_1'])
       com_12sl = com_12sl.drop(columns=['ST_seg_2'])
     else:
       pass
     com_12sl['EcgID']=file
     cols = list(com_12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     com_12sl = com_12sl[cols]
     com_12sl_dict125.update({file: com_12sl})
     
com_12sl_df = pd.concat(com_12sl_dict125) 
com_12sl_df['EcgID'] = com_12sl_df['EcgID'].str.replace(r'.txt','')
com_12sl_df.columns.name = None
com_12sl_df.to_csv('Output/end_comms/com_12sl_125_df.csv', index=False)


com_12sl_dict127 = {}

for file in files127:
     com_12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 116, skipfooter = 0)
     com_12sl = com_12sl[~com_12sl[0].str.contains("Minnesota", na=False)]
     row = com_12sl[com_12sl[0] == 'Comments:'].index.tolist()[0]
     com_12sl.reset_index(drop=True, inplace=True)
     com_12sl_T = com_12sl.T
     if com_12sl.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_12sl_T.columns).all():
       com_12sl = com_12sl.T
       com_12sl.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_12sl = com_12sl.drop(columns=['drop1', 'drop2'])
       com_12sl = com_12sl.join(com_12sl['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_12sl = com_12sl.join(com_12sl['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_12sl = com_12sl.drop(columns=['ST_seg_1'])
       com_12sl = com_12sl.drop(columns=['ST_seg_2'])
     else:
       pass
     com_12sl['EcgID']=file
     cols = list(com_12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     com_12sl = com_12sl[cols]
     com_12sl_dict127.update({file: com_12sl})
     
com_12sl_df = pd.concat(com_12sl_dict127) 
com_12sl_df['EcgID'] = com_12sl_df['EcgID'].str.replace(r'.txt','')
com_12sl_df.columns.name = None
com_12sl_df.to_csv('Output/end_comms/com_12sl_127_df.csv', index=False)

com_12sl_dict128 = {}

for file in files128:
     com_12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 118, skipfooter = 0)
     com_12sl = com_12sl[~com_12sl[0].str.contains("Minnesota", na=False)]
     row = com_12sl[com_12sl[0] == 'Comments:'].index.tolist()[0]
     com_12sl.reset_index(drop=True, inplace=True)
     com_12sl_T = com_12sl.T
     if com_12sl.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_12sl_T.columns).all():
       com_12sl = com_12sl.T
       com_12sl.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_12sl = com_12sl.drop(columns=['drop1', 'drop2'])
       com_12sl = com_12sl.join(com_12sl['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_12sl = com_12sl.join(com_12sl['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_12sl = com_12sl.drop(columns=['ST_seg_1'])
       com_12sl = com_12sl.drop(columns=['ST_seg_2'])
     else:
       pass
     com_12sl['EcgID']=file
     cols = list(com_12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     com_12sl = com_12sl[cols]
     com_12sl_dict128.update({file: com_12sl})
     
com_12sl_df = pd.concat(com_12sl_dict128) 
com_12sl_df['EcgID'] = com_12sl_df['EcgID'].str.replace(r'.txt','')
com_12sl_df.columns.name = None
com_12sl_df.to_csv('Output/end_comms/com_12sl_128_df.csv', index=False)

com_12sl_dict129 = {}

for file in files129:
     com_12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 118, skipfooter = 0)
     com_12sl = com_12sl[~com_12sl[0].str.contains("Minnesota", na=False)]
     row = com_12sl[com_12sl[0] == 'Comments:'].index.tolist()[0]
     com_12sl.reset_index(drop=True, inplace=True)
     com_12sl_T = com_12sl.T
     if com_12sl.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_12sl_T.columns).all():
       com_12sl = com_12sl.T
       com_12sl.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_12sl = com_12sl.drop(columns=['drop1', 'drop2'])
       com_12sl = com_12sl.join(com_12sl['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_12sl = com_12sl.join(com_12sl['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_12sl = com_12sl.drop(columns=['ST_seg_1'])
       com_12sl = com_12sl.drop(columns=['ST_seg_2'])
     else:
       pass
     com_12sl['EcgID']=file
     cols = list(com_12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     com_12sl = com_12sl[cols]
     com_12sl_dict129.update({file: com_12sl})
     
com_12sl_df = pd.concat(com_12sl_dict129) 
com_12sl_df['EcgID'] = com_12sl_df['EcgID'].str.replace(r'.txt','')
com_12sl_df.columns.name = None
com_12sl_df.to_csv('Output/end_comms/com_12sl_129_df.csv', index=False)

com_12sl_dict130 = {}

for file in files130:
     com_12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 120, skipfooter = 0)
     com_12sl = com_12sl[~com_12sl[0].str.contains("Minnesota", na=False)]
     row = com_12sl[com_12sl[0] == 'Comments:'].index.tolist()[0]
     com_12sl.reset_index(drop=True, inplace=True)
     com_12sl_T = com_12sl.T
     if com_12sl.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_12sl_T.columns).all():
       com_12sl = com_12sl.T
       com_12sl.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_12sl = com_12sl.drop(columns=['drop1', 'drop2'])
       com_12sl = com_12sl.join(com_12sl['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_12sl = com_12sl.join(com_12sl['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_12sl = com_12sl.drop(columns=['ST_seg_1'])
       com_12sl = com_12sl.drop(columns=['ST_seg_2'])
     else:
       pass
     com_12sl['EcgID']=file
     cols = list(com_12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     com_12sl = com_12sl[cols]
     com_12sl_dict130.update({file: com_12sl})
     
com_12sl_df = pd.concat(com_12sl_dict130) 
com_12sl_df['EcgID'] = com_12sl_df['EcgID'].str.replace(r'.txt','')
com_12sl_df.columns.name = None
com_12sl_df.to_csv('Output/end_comms/com_12sl_130_df.csv', index=False)


com_12sl_dict131 = {}

for file in files131:
     com_12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 120, skipfooter = 0)
     com_12sl = com_12sl[~com_12sl[0].str.contains("Minnesota", na=False)]
     row = com_12sl[com_12sl[0] == 'Comments:'].index.tolist()[0]
     com_12sl.reset_index(drop=True, inplace=True)
     com_12sl_T = com_12sl.T
     if com_12sl.shape[0] == 4 and pd.Series([0,1,2,3]).isin(com_12sl_T.columns).all():
       com_12sl = com_12sl.T
       com_12sl.rename(columns={0: 'drop1', 1: 'drop2',2: 'ST_seg_1',3: 'ST_seg_2'}, inplace=True)
       com_12sl = com_12sl.drop(columns=['drop1', 'drop2'])
       com_12sl = com_12sl.join(com_12sl['ST_seg_1'].str.split("\\s+", expand=True).add_prefix('ST_seg_1_'))
       com_12sl = com_12sl.join(com_12sl['ST_seg_2'].str.split("\\s+", expand=True).add_prefix('ST_seg_2_'))
       com_12sl = com_12sl.drop(columns=['ST_seg_1'])
       com_12sl = com_12sl.drop(columns=['ST_seg_2'])
     else:
       pass
     com_12sl['EcgID']=file
     cols = list(com_12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     com_12sl = com_12sl[cols]
     com_12sl_dict131.update({file: com_12sl})
     
com_12sl_df = pd.concat(com_12sl_dict131) 
com_12sl_df['EcgID'] = com_12sl_df['EcgID'].str.replace(r'.txt','')
com_12sl_df.columns.name = None
com_12sl_df.to_csv('Output/end_comms/com_12sl_131_df.csv', index=False)
