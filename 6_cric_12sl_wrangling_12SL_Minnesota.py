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


 min12sl = pd.read_fwf("70723216.txt", header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     min12sl = min12sl[~min12sl[0].str.contains("No of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("No. of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("Comments", na=False)]
     row = min12sl[min12sl[0] == '12SL Statement Code:'].index.tolist()[0]
     min12sl = min12sl.iloc[row-1:]
     min12sl_T = min12sl.T



min12sl_dict120 = {}

for file in files120:
     min12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     min12sl = min12sl[~min12sl[0].str.contains("No of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("No. of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("Comments", na=False)]
     row = min12sl[min12sl[0] == '12SL Statement Code:'].index.tolist()[0]
     min12sl = min12sl.iloc[row-1:]
     min12sl_T = min12sl.T
     if min12sl.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif min12sl.shape[0] == 4 and pd.Series([1,2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 3 and pd.Series([1,2,4]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     min12sl['EcgID']=file
     cols = list(min12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     min12sl = min12sl[cols]
     min12sl_dict120.update({file: min12sl})
     
min12sl_df = pd.concat(min12sl_dict120) 
min12sl_df['EcgID'] = min12sl_df['EcgID'].str.replace(r'.txt','')
min12sl_df.columns.name = None
min12sl_df.to_csv('Output/min12sl/min12sl_120_df.csv', index=False) 

min12sl_dict121 = {}

for file in files121:
     min12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     min12sl = min12sl[~min12sl[0].str.contains("No of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("No. of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("Comments", na=False)]
     row = min12sl[min12sl[0] == '12SL Statement Code:'].index.tolist()[0]
     min12sl = min12sl.iloc[row-1:]
     min12sl_T = min12sl.T
     if min12sl.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif min12sl.shape[0] == 4 and pd.Series([1,2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 3 and pd.Series([1,2,4]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     min12sl['EcgID']=file
     cols = list(min12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     min12sl = min12sl[cols]
     min12sl_dict121.update({file: min12sl})
     
min12sl_df = pd.concat(min12sl_dict121) 
min12sl_df['EcgID'] = min12sl_df['EcgID'].str.replace(r'.txt','')
min12sl_df.columns.name = None
min12sl_df.to_csv('Output/min12sl/min12sl_121_df.csv', index=False) 

min12sl_dict122 = {}

for file in files122:
     min12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     min12sl = min12sl[~min12sl[0].str.contains("No of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("No. of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("Comments", na=False)]
     row = min12sl[min12sl[0] == '12SL Statement Code:'].index.tolist()[0]
     min12sl = min12sl.iloc[row-1:]
     min12sl_T = min12sl.T
     if min12sl.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif min12sl.shape[0] == 4 and pd.Series([1,2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 3 and pd.Series([1,2,4]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     min12sl['EcgID']=file
     cols = list(min12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     min12sl = min12sl[cols]
     min12sl_dict122.update({file: min12sl})
     
min12sl_df = pd.concat(min12sl_dict122) 
min12sl_df['EcgID'] = min12sl_df['EcgID'].str.replace(r'.txt','')
min12sl_df.columns.name = None
min12sl_df.to_csv('Output/min12sl/min12sl_122_df.csv', index=False) 


min12sl_dict123 = {}

for file in files123:
     min12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     min12sl = min12sl[~min12sl[0].str.contains("No of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("No. of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("Comments", na=False)]
     row = min12sl[min12sl[0] == '12SL Statement Code:'].index.tolist()[0]
     min12sl = min12sl.iloc[row-1:]
     min12sl_T = min12sl.T
     if min12sl.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif min12sl.shape[0] == 4 and pd.Series([1,2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 4 and pd.Series([2,3,4,6]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={2: 'drop1', 3: '12SL Statement Code_A',4:'12SL Statement Code_B',6: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 3 and pd.Series([1,2,4]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([3,4,6]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={3: 'drop1',4:'12SL Statement Code_A',6: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     min12sl['EcgID']=file
     cols = list(min12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     min12sl = min12sl[cols]
     min12sl_dict123.update({file: min12sl})
     
min12sl_df = pd.concat(min12sl_dict123) 
min12sl_df['EcgID'] = min12sl_df['EcgID'].str.replace(r'.txt','')
min12sl_df.columns.name = None
min12sl_df.to_csv('Output/min12sl/min12sl_123_df.csv', index=False) 

min12sl_dict124 = {}

for file in files124:
     min12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     min12sl = min12sl[~min12sl[0].str.contains("No of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("No. of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("Comments", na=False)]
     row = min12sl[min12sl[0] == '12SL Statement Code:'].index.tolist()[0]
     min12sl = min12sl.iloc[row-1:]
     min12sl_T = min12sl.T
     if min12sl.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif min12sl.shape[0] == 4 and pd.Series([1,2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 4 and pd.Series([2,3,4,6]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={2: 'drop1', 3: '12SL Statement Code_A',4:'12SL Statement Code_B',6: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 3 and pd.Series([1,2,4]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([3,4,6]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={3: 'drop1',4:'12SL Statement Code_A',6: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 4 and pd.Series([3,4,5,7]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={3: 'drop1', 4: '12SL Statement Code_A',5:'12SL Statement Code_B',7: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     else:
       pass
     min12sl['EcgID']=file
     cols = list(min12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     min12sl = min12sl[cols]
     min12sl_dict124.update({file: min12sl})
     
min12sl_df = pd.concat(min12sl_dict124) 
min12sl_df['EcgID'] = min12sl_df['EcgID'].str.replace(r'.txt','')
min12sl_df.columns.name = None
min12sl_df.to_csv('Output/min12sl/min12sl_124_df.csv', index=False) 

min12sl_dict125 = {}

for file in files125:
     min12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 103, skipfooter = 4)
     min12sl = min12sl[~min12sl[0].str.contains("No of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("No. of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("Comments", na=False)]
     row = min12sl[min12sl[0] == '12SL Statement Code:'].index.tolist()[0]
     min12sl = min12sl.iloc[row-1:]
     min12sl_T = min12sl.T
     if min12sl.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif min12sl.shape[0] == 4 and pd.Series([1,2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 4 and pd.Series([2,3,4,6]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={2: 'drop1', 3: '12SL Statement Code_A',4:'12SL Statement Code_B',6: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 3 and pd.Series([1,2,4]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([3,4,6]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={3: 'drop1',4:'12SL Statement Code_A',6: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([5,6,8]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={5: 'drop1',6:'12SL Statement Code_A',8: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     min12sl['EcgID']=file
     cols = list(min12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     min12sl = min12sl[cols]
     min12sl_dict125.update({file: min12sl})
     
min12sl_df = pd.concat(min12sl_dict125) 
min12sl_df['EcgID'] = min12sl_df['EcgID'].str.replace(r'.txt','')
min12sl_df.columns.name = None
min12sl_df.to_csv('Output/min12sl/min12sl_125_df.csv', index=False) 

min12sl_dict127 = {}

for file in files127:
     min12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 107, skipfooter = 4)
     min12sl = min12sl[~min12sl[0].str.contains("No of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("No. of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("Comments", na=False)]
     row = min12sl[min12sl[0] == '12SL Statement Code:'].index.tolist()[0]
     min12sl = min12sl.iloc[row-1:]
     min12sl.reset_index(drop=True, inplace=True)
     min12sl_T = min12sl.T
     if min12sl.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif min12sl.shape[0] == 4 and pd.Series([1,2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 4 and pd.Series([2,3,4,6]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={2: 'drop1', 3: '12SL Statement Code_A',4:'12SL Statement Code_B',6: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 3 and pd.Series([0,1,2]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={0: 'drop1', 1: '12SL Statement Code_A',2: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([3,4,6]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={3: 'drop1',4:'12SL Statement Code_A',6: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     min12sl['EcgID']=file
     cols = list(min12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     min12sl = min12sl[cols]
     min12sl_dict127.update({file: min12sl})
     
min12sl_df = pd.concat(min12sl_dict127) 
min12sl_df['EcgID'] = min12sl_df['EcgID'].str.replace(r'.txt','')
min12sl_df.columns.name = None
min12sl_df.to_csv('Output/min12sl/min12sl_127_df.csv', index=False) 

min12sl_dict128 = {}

for file in files128:
     min12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     min12sl = min12sl[~min12sl[0].str.contains("No of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("No. of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("Comments", na=False)]
     row = min12sl[min12sl[0] == '12SL Statement Code:'].index.tolist()[0]
     min12sl = min12sl.iloc[row-1:]
     min12sl.reset_index(drop=True, inplace=True)
     min12sl_T = min12sl.T
     if min12sl.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif min12sl.shape[0] == 4 and pd.Series([1,2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 4 and pd.Series([0,1,2,3]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={0: 'drop1', 1: '12SL Statement Code_A',2:'12SL Statement Code_B',3: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 3 and pd.Series([0,1,2]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={0: 'drop1', 1: '12SL Statement Code_A',2: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([3,4,6]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={3: 'drop1',4:'12SL Statement Code_A',6: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     min12sl['EcgID']=file
     cols = list(min12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     min12sl = min12sl[cols]
     min12sl_dict128.update({file: min12sl})
     
min12sl_df = pd.concat(min12sl_dict128) 
min12sl_df['EcgID'] = min12sl_df['EcgID'].str.replace(r'.txt','')
min12sl_df.columns.name = None
min12sl_df.to_csv('Output/min12sl/min12sl_128_df.csv', index=False) 

min12sl_dict129 = {}

for file in files129:
     min12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     min12sl = min12sl[~min12sl[0].str.contains("No of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("No. of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("Comments", na=False)]
     row = min12sl[min12sl[0] == '12SL Statement Code:'].index.tolist()[0]
     min12sl = min12sl.iloc[row-1:]
     min12sl.reset_index(drop=True, inplace=True)
     min12sl_T = min12sl.T
     if min12sl.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif min12sl.shape[0] == 4 and pd.Series([0,1,2,3]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={0: 'drop1', 1: '12SL Statement Code_A',2:'12SL Statement Code_B',3: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 4 and pd.Series([2,3,4,6]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={2: 'drop1', 3: '12SL Statement Code_A',4:'12SL Statement Code_B',6: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 3 and pd.Series([0,1,2]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={0: 'drop1', 1: '12SL Statement Code_A',2: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([3,4,6]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={3: 'drop1',4:'12SL Statement Code_A',6: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     min12sl['EcgID']=file
     cols = list(min12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     min12sl = min12sl[cols]
     min12sl_dict129.update({file: min12sl})
     
min12sl_df = pd.concat(min12sl_dict129) 
min12sl_df['EcgID'] = min12sl_df['EcgID'].str.replace(r'.txt','')
min12sl_df.columns.name = None
min12sl_df.to_csv('Output/min12sl/min12sl_129_df.csv', index=False) 

min12sl_dict130 = {}

for file in files130:
     min12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     min12sl = min12sl[~min12sl[0].str.contains("No of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("No. of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("Comments", na=False)]
     row = min12sl[min12sl[0] == '12SL Statement Code:'].index.tolist()[0]
     min12sl = min12sl.iloc[row-1:]
     min12sl.reset_index(drop=True, inplace=True)
     min12sl_T = min12sl.T
     if min12sl.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif min12sl.shape[0] == 4 and pd.Series([1,2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 4 and pd.Series([0,1,2,3]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={0: 'drop1', 1: '12SL Statement Code_A',2:'12SL Statement Code_B',3: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 3 and pd.Series([1,2,4]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([0,1,2]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={0: 'drop1',1:'12SL Statement Code_A',2: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     min12sl['EcgID']=file
     cols = list(min12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     min12sl = min12sl[cols]
     min12sl_dict130.update({file: min12sl})
     
min12sl_df = pd.concat(min12sl_dict130) 
min12sl_df['EcgID'] = min12sl_df['EcgID'].str.replace(r'.txt','')
min12sl_df.columns.name = None
min12sl_df.to_csv('Output/min12sl/min12sl_130_df.csv', index=False) 


min12sl_dict131 = {}

for file in files131:
     min12sl = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     min12sl = min12sl[~min12sl[0].str.contains("No of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("No. of", na=False)]
     min12sl = min12sl[~min12sl[0].str.contains("Comments", na=False)]
     row = min12sl[min12sl[0] == '12SL Statement Code:'].index.tolist()[0]
     min12sl = min12sl.iloc[row-1:]
     min12sl.reset_index(drop=True, inplace=True)
     min12sl_T = min12sl.T
     if min12sl.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif min12sl.shape[0] == 4 and pd.Series([1,2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 4 and pd.Series([2,3,4,6]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={2: 'drop1', 3: '12SL Statement Code_A',4:'12SL Statement Code_B',6: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.join(min12sl['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif min12sl.shape[0] == 3 and pd.Series([1,2,4]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1', 'drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([2,3,5]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     elif min12sl.shape[0] == 3 and pd.Series([0,1,2]).isin(min12sl_T.columns).all():
       min12sl = min12sl.T
       min12sl.rename(columns={0: 'drop1',1:'12SL Statement Code_A',2: 'drop2'}, inplace=True)
       min12sl = min12sl.drop(columns=['drop1','drop2'])
       min12sl = min12sl.join(min12sl['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       min12sl = min12sl.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     min12sl['EcgID']=file
     cols = list(min12sl.columns)
     cols = [cols[-1]] + cols[:-1]
     min12sl = min12sl[cols]
     min12sl_dict131.update({file: min12sl})
     
min12sl_df = pd.concat(min12sl_dict131) 
min12sl_df['EcgID'] = min12sl_df['EcgID'].str.replace(r'.txt','')
min12sl_df.columns.name = None
min12sl_df.to_csv('Output/min12sl/min12sl_131_df.csv', index=False) 
