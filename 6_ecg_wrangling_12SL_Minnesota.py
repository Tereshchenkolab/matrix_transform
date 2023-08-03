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


 minecg = pd.read_fwf("70723216.txt", header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     minecg = minecg[~minecg[0].str.contains("No of", na=False)]
     minecg = minecg[~minecg[0].str.contains("No. of", na=False)]
     minecg = minecg[~minecg[0].str.contains("Comments", na=False)]
     row = minecg[minecg[0] == '12SL Statement Code:'].index.tolist()[0]
     minecg = minecg.iloc[row-1:]
     minecg_T = minecg.T



minecg_dict120 = {}

for file in files120:
     minecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     minecg = minecg[~minecg[0].str.contains("No of", na=False)]
     minecg = minecg[~minecg[0].str.contains("No. of", na=False)]
     minecg = minecg[~minecg[0].str.contains("Comments", na=False)]
     row = minecg[minecg[0] == '12SL Statement Code:'].index.tolist()[0]
     minecg = minecg.iloc[row-1:]
     minecg_T = minecg.T
     if minecg.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif minecg.shape[0] == 4 and pd.Series([1,2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 3 and pd.Series([1,2,4]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     minecg['EcgID']=file
     cols = list(minecg.columns)
     cols = [cols[-1]] + cols[:-1]
     minecg = minecg[cols]
     minecg_dict120.update({file: minecg})
     
minecg_df = pd.concat(minecg_dict120) 
minecg_df['EcgID'] = minecg_df['EcgID'].str.replace(r'.txt','')
minecg_df.columns.name = None
minecg_df.to_csv('Output/minecg/minecg_120_df.csv', index=False) 

minecg_dict121 = {}

for file in files121:
     minecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     minecg = minecg[~minecg[0].str.contains("No of", na=False)]
     minecg = minecg[~minecg[0].str.contains("No. of", na=False)]
     minecg = minecg[~minecg[0].str.contains("Comments", na=False)]
     row = minecg[minecg[0] == '12SL Statement Code:'].index.tolist()[0]
     minecg = minecg.iloc[row-1:]
     minecg_T = minecg.T
     if minecg.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif minecg.shape[0] == 4 and pd.Series([1,2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 3 and pd.Series([1,2,4]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     minecg['EcgID']=file
     cols = list(minecg.columns)
     cols = [cols[-1]] + cols[:-1]
     minecg = minecg[cols]
     minecg_dict121.update({file: minecg})
     
minecg_df = pd.concat(minecg_dict121) 
minecg_df['EcgID'] = minecg_df['EcgID'].str.replace(r'.txt','')
minecg_df.columns.name = None
minecg_df.to_csv('Output/minecg/minecg_121_df.csv', index=False) 

minecg_dict122 = {}

for file in files122:
     minecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     minecg = minecg[~minecg[0].str.contains("No of", na=False)]
     minecg = minecg[~minecg[0].str.contains("No. of", na=False)]
     minecg = minecg[~minecg[0].str.contains("Comments", na=False)]
     row = minecg[minecg[0] == '12SL Statement Code:'].index.tolist()[0]
     minecg = minecg.iloc[row-1:]
     minecg_T = minecg.T
     if minecg.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif minecg.shape[0] == 4 and pd.Series([1,2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 3 and pd.Series([1,2,4]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     minecg['EcgID']=file
     cols = list(minecg.columns)
     cols = [cols[-1]] + cols[:-1]
     minecg = minecg[cols]
     minecg_dict122.update({file: minecg})
     
minecg_df = pd.concat(minecg_dict122) 
minecg_df['EcgID'] = minecg_df['EcgID'].str.replace(r'.txt','')
minecg_df.columns.name = None
minecg_df.to_csv('Output/minecg/minecg_122_df.csv', index=False) 


minecg_dict123 = {}

for file in files123:
     minecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     minecg = minecg[~minecg[0].str.contains("No of", na=False)]
     minecg = minecg[~minecg[0].str.contains("No. of", na=False)]
     minecg = minecg[~minecg[0].str.contains("Comments", na=False)]
     row = minecg[minecg[0] == '12SL Statement Code:'].index.tolist()[0]
     minecg = minecg.iloc[row-1:]
     minecg_T = minecg.T
     if minecg.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif minecg.shape[0] == 4 and pd.Series([1,2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 4 and pd.Series([2,3,4,6]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={2: 'drop1', 3: '12SL Statement Code_A',4:'12SL Statement Code_B',6: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 3 and pd.Series([1,2,4]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([3,4,6]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={3: 'drop1',4:'12SL Statement Code_A',6: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     minecg['EcgID']=file
     cols = list(minecg.columns)
     cols = [cols[-1]] + cols[:-1]
     minecg = minecg[cols]
     minecg_dict123.update({file: minecg})
     
minecg_df = pd.concat(minecg_dict123) 
minecg_df['EcgID'] = minecg_df['EcgID'].str.replace(r'.txt','')
minecg_df.columns.name = None
minecg_df.to_csv('Output/minecg/minecg_123_df.csv', index=False) 

minecg_dict124 = {}

for file in files124:
     minecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     minecg = minecg[~minecg[0].str.contains("No of", na=False)]
     minecg = minecg[~minecg[0].str.contains("No. of", na=False)]
     minecg = minecg[~minecg[0].str.contains("Comments", na=False)]
     row = minecg[minecg[0] == '12SL Statement Code:'].index.tolist()[0]
     minecg = minecg.iloc[row-1:]
     minecg_T = minecg.T
     if minecg.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif minecg.shape[0] == 4 and pd.Series([1,2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 4 and pd.Series([2,3,4,6]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={2: 'drop1', 3: '12SL Statement Code_A',4:'12SL Statement Code_B',6: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 3 and pd.Series([1,2,4]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([3,4,6]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={3: 'drop1',4:'12SL Statement Code_A',6: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 4 and pd.Series([3,4,5,7]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={3: 'drop1', 4: '12SL Statement Code_A',5:'12SL Statement Code_B',7: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     else:
       pass
     minecg['EcgID']=file
     cols = list(minecg.columns)
     cols = [cols[-1]] + cols[:-1]
     minecg = minecg[cols]
     minecg_dict124.update({file: minecg})
     
minecg_df = pd.concat(minecg_dict124) 
minecg_df['EcgID'] = minecg_df['EcgID'].str.replace(r'.txt','')
minecg_df.columns.name = None
minecg_df.to_csv('Output/minecg/minecg_124_df.csv', index=False) 

minecg_dict125 = {}

for file in files125:
     minecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 103, skipfooter = 4)
     minecg = minecg[~minecg[0].str.contains("No of", na=False)]
     minecg = minecg[~minecg[0].str.contains("No. of", na=False)]
     minecg = minecg[~minecg[0].str.contains("Comments", na=False)]
     row = minecg[minecg[0] == '12SL Statement Code:'].index.tolist()[0]
     minecg = minecg.iloc[row-1:]
     minecg_T = minecg.T
     if minecg.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif minecg.shape[0] == 4 and pd.Series([1,2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 4 and pd.Series([2,3,4,6]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={2: 'drop1', 3: '12SL Statement Code_A',4:'12SL Statement Code_B',6: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 3 and pd.Series([1,2,4]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([3,4,6]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={3: 'drop1',4:'12SL Statement Code_A',6: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([5,6,8]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={5: 'drop1',6:'12SL Statement Code_A',8: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     minecg['EcgID']=file
     cols = list(minecg.columns)
     cols = [cols[-1]] + cols[:-1]
     minecg = minecg[cols]
     minecg_dict125.update({file: minecg})
     
minecg_df = pd.concat(minecg_dict125) 
minecg_df['EcgID'] = minecg_df['EcgID'].str.replace(r'.txt','')
minecg_df.columns.name = None
minecg_df.to_csv('Output/minecg/minecg_125_df.csv', index=False) 

minecg_dict127 = {}

for file in files127:
     minecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 107, skipfooter = 4)
     minecg = minecg[~minecg[0].str.contains("No of", na=False)]
     minecg = minecg[~minecg[0].str.contains("No. of", na=False)]
     minecg = minecg[~minecg[0].str.contains("Comments", na=False)]
     row = minecg[minecg[0] == '12SL Statement Code:'].index.tolist()[0]
     minecg = minecg.iloc[row-1:]
     minecg.reset_index(drop=True, inplace=True)
     minecg_T = minecg.T
     if minecg.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif minecg.shape[0] == 4 and pd.Series([1,2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 4 and pd.Series([2,3,4,6]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={2: 'drop1', 3: '12SL Statement Code_A',4:'12SL Statement Code_B',6: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 3 and pd.Series([0,1,2]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={0: 'drop1', 1: '12SL Statement Code_A',2: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([3,4,6]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={3: 'drop1',4:'12SL Statement Code_A',6: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     minecg['EcgID']=file
     cols = list(minecg.columns)
     cols = [cols[-1]] + cols[:-1]
     minecg = minecg[cols]
     minecg_dict127.update({file: minecg})
     
minecg_df = pd.concat(minecg_dict127) 
minecg_df['EcgID'] = minecg_df['EcgID'].str.replace(r'.txt','')
minecg_df.columns.name = None
minecg_df.to_csv('Output/minecg/minecg_127_df.csv', index=False) 

minecg_dict128 = {}

for file in files128:
     minecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     minecg = minecg[~minecg[0].str.contains("No of", na=False)]
     minecg = minecg[~minecg[0].str.contains("No. of", na=False)]
     minecg = minecg[~minecg[0].str.contains("Comments", na=False)]
     row = minecg[minecg[0] == '12SL Statement Code:'].index.tolist()[0]
     minecg = minecg.iloc[row-1:]
     minecg.reset_index(drop=True, inplace=True)
     minecg_T = minecg.T
     if minecg.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif minecg.shape[0] == 4 and pd.Series([1,2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 4 and pd.Series([0,1,2,3]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={0: 'drop1', 1: '12SL Statement Code_A',2:'12SL Statement Code_B',3: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 3 and pd.Series([0,1,2]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={0: 'drop1', 1: '12SL Statement Code_A',2: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([3,4,6]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={3: 'drop1',4:'12SL Statement Code_A',6: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     minecg['EcgID']=file
     cols = list(minecg.columns)
     cols = [cols[-1]] + cols[:-1]
     minecg = minecg[cols]
     minecg_dict128.update({file: minecg})
     
minecg_df = pd.concat(minecg_dict128) 
minecg_df['EcgID'] = minecg_df['EcgID'].str.replace(r'.txt','')
minecg_df.columns.name = None
minecg_df.to_csv('Output/minecg/minecg_128_df.csv', index=False) 

minecg_dict129 = {}

for file in files129:
     minecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     minecg = minecg[~minecg[0].str.contains("No of", na=False)]
     minecg = minecg[~minecg[0].str.contains("No. of", na=False)]
     minecg = minecg[~minecg[0].str.contains("Comments", na=False)]
     row = minecg[minecg[0] == '12SL Statement Code:'].index.tolist()[0]
     minecg = minecg.iloc[row-1:]
     minecg.reset_index(drop=True, inplace=True)
     minecg_T = minecg.T
     if minecg.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif minecg.shape[0] == 4 and pd.Series([0,1,2,3]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={0: 'drop1', 1: '12SL Statement Code_A',2:'12SL Statement Code_B',3: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 4 and pd.Series([2,3,4,6]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={2: 'drop1', 3: '12SL Statement Code_A',4:'12SL Statement Code_B',6: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 3 and pd.Series([0,1,2]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={0: 'drop1', 1: '12SL Statement Code_A',2: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([3,4,6]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={3: 'drop1',4:'12SL Statement Code_A',6: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     minecg['EcgID']=file
     cols = list(minecg.columns)
     cols = [cols[-1]] + cols[:-1]
     minecg = minecg[cols]
     minecg_dict129.update({file: minecg})
     
minecg_df = pd.concat(minecg_dict129) 
minecg_df['EcgID'] = minecg_df['EcgID'].str.replace(r'.txt','')
minecg_df.columns.name = None
minecg_df.to_csv('Output/minecg/minecg_129_df.csv', index=False) 

minecg_dict130 = {}

for file in files130:
     minecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     minecg = minecg[~minecg[0].str.contains("No of", na=False)]
     minecg = minecg[~minecg[0].str.contains("No. of", na=False)]
     minecg = minecg[~minecg[0].str.contains("Comments", na=False)]
     row = minecg[minecg[0] == '12SL Statement Code:'].index.tolist()[0]
     minecg = minecg.iloc[row-1:]
     minecg.reset_index(drop=True, inplace=True)
     minecg_T = minecg.T
     if minecg.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif minecg.shape[0] == 4 and pd.Series([1,2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 4 and pd.Series([0,1,2,3]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={0: 'drop1', 1: '12SL Statement Code_A',2:'12SL Statement Code_B',3: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 3 and pd.Series([1,2,4]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([0,1,2]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={0: 'drop1',1:'12SL Statement Code_A',2: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     minecg['EcgID']=file
     cols = list(minecg.columns)
     cols = [cols[-1]] + cols[:-1]
     minecg = minecg[cols]
     minecg_dict130.update({file: minecg})
     
minecg_df = pd.concat(minecg_dict130) 
minecg_df['EcgID'] = minecg_df['EcgID'].str.replace(r'.txt','')
minecg_df.columns.name = None
minecg_df.to_csv('Output/minecg/minecg_130_df.csv', index=False) 


minecg_dict131 = {}

for file in files131:
     minecg = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 101, skipfooter = 4)
     minecg = minecg[~minecg[0].str.contains("No of", na=False)]
     minecg = minecg[~minecg[0].str.contains("No. of", na=False)]
     minecg = minecg[~minecg[0].str.contains("Comments", na=False)]
     row = minecg[minecg[0] == '12SL Statement Code:'].index.tolist()[0]
     minecg = minecg.iloc[row-1:]
     minecg.reset_index(drop=True, inplace=True)
     minecg_T = minecg.T
     if minecg.shape[0] == 4 and pd.Series([1, 2,4,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2',5:'Minnestoa Code'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['Minnestoa Code'].str.split("\\s+", expand=True).add_prefix('minnesota_code_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A', 'Minnestoa Code'])
     elif minecg.shape[0] == 4 and pd.Series([1,2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',3:'12SL Statement Code_B',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 4 and pd.Series([2,3,4,6]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={2: 'drop1', 3: '12SL Statement Code_A',4:'12SL Statement Code_B',6: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.join(minecg['12SL Statement Code_B'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeB_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A','12SL Statement Code_B'])
     elif minecg.shape[0] == 3 and pd.Series([1,2,4]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={1: 'drop1', 2: '12SL Statement Code_A',4: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1', 'drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([2,3,5]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={2: 'drop1',3:'12SL Statement Code_A',5: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     elif minecg.shape[0] == 3 and pd.Series([0,1,2]).isin(minecg_T.columns).all():
       minecg = minecg.T
       minecg.rename(columns={0: 'drop1',1:'12SL Statement Code_A',2: 'drop2'}, inplace=True)
       minecg = minecg.drop(columns=['drop1','drop2'])
       minecg = minecg.join(minecg['12SL Statement Code_A'].str.split("\\s+", expand=True).add_prefix('12Sl_statementCodeA_'))
       minecg = minecg.drop(columns=['12SL Statement Code_A'])
     else:
       pass
     minecg['EcgID']=file
     cols = list(minecg.columns)
     cols = [cols[-1]] + cols[:-1]
     minecg = minecg[cols]
     minecg_dict131.update({file: minecg})
     
minecg_df = pd.concat(minecg_dict131) 
minecg_df['EcgID'] = minecg_df['EcgID'].str.replace(r'.txt','')
minecg_df.columns.name = None
minecg_df.to_csv('Output/minecg/minecg_131_df.csv', index=False) 
