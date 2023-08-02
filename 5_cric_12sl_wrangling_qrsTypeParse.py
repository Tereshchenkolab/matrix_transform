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

qrs = pd.read_fwf("70649816.txt", header= None, colspecs = [(0, 100)], skiprows = 90, skipfooter = 15)
     qrs = qrs[~qrs[0].str.contains("12SL", na=False)]
     qrs[0] = qrs[0].str.replace('-', ' -', regex=True)


qrs_dict120 = {}

for file in files120:
     qrs = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 90, skipfooter = 17)
     qrs = qrs[~qrs[0].str.contains("12SL", na=False)]
     qrs[0] = qrs[0].str.replace('-', ' -', regex=True)
     if qrs.shape[0] == 9:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5a'])
     elif qrs.shape[0] == 10:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a',9: 'QRSType1_5b'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5a', 'QRSType1_5b'])
     else:
       pass
     qrs['EcgID']=file
     cols = list(qrs.columns)
     cols = [cols[-1]] + cols[:-1]
     qrs = qrs[cols]
     qrs_dict120.update({file: qrs})
     
qrs_120_df = pd.concat(qrs_dict120) 
qrs_120_df['EcgID'] = qrs_120_df['EcgID'].str.replace(r'.txt','')
qrs_120_df.columns.name = None
qrs_120_df.to_csv('Output/qrs/qrs_120_df.csv', index=False) 

qrs_dict121 = {}

for file in files121:
     qrs = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 90, skipfooter = 15)
     qrs = qrs[~qrs[0].str.contains("12SL", na=False)]
     qrs[0] = qrs[0].str.replace('-', ' -', regex=True)
     if qrs.shape[0] == 9:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5a'])
     elif qrs.shape[0] == 10:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a',9: 'QRSType1_5b'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5a', 'QRSType1_5b'])
     else:
       pass
     qrs['EcgID']=file
     cols = list(qrs.columns)
     cols = [cols[-1]] + cols[:-1]
     qrs = qrs[cols]
     qrs_dict121.update({file: qrs})
     
qrs_121_df = pd.concat(qrs_dict121) 
qrs_121_df['EcgID'] = qrs_121_df['EcgID'].str.replace(r'.txt','')
qrs_121_df.columns.name = None
qrs_121_df.to_csv('Output/qrs/qrs_121_df.csv', index=False) 


qrs_dict122 = {}

for file in files122:
     qrs = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 90, skipfooter = 17)
     qrs = qrs[~qrs[0].str.contains("12SL", na=False)]
     qrs[0] = qrs[0].str.replace('-', ' -', regex=True)
     if qrs.shape[0] == 9:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5a'])
     elif qrs.shape[0] == 10:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a',9: 'QRSType1_5b'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5a', 'QRSType1_5b'])
     else:
       pass
     qrs['EcgID']=file
     cols = list(qrs.columns)
     cols = [cols[-1]] + cols[:-1]
     qrs = qrs[cols]
     qrs_dict122.update({file: qrs})
     
qrs_122_df = pd.concat(qrs_dict122) 
qrs_122_df['EcgID'] = qrs_122_df['EcgID'].str.replace(r'.txt','')
qrs_122_df.columns.name = None
qrs_122_df.to_csv('Output/qrs/qrs_122_df.csv', index=False) 


qrs_dict123 = {}

for file in files123:
     qrs = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 90, skipfooter = 16)
     qrs = qrs[~qrs[0].str.contains("12SL", na=False)]
     qrs[0] = qrs[0].str.replace('-', ' -', regex=True)
     if qrs.shape[0] == 9:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5a'])
     elif qrs.shape[0] == 10:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a',9: 'QRSType1_5b'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5a', 'QRSType1_5b'])
     elif qrs.shape[0] == 11:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a',9: 'QRSType1_5b',10: 'QRSType1_5c'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.join(qrs['QRSType1_5c'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoC_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5a', 'QRSType1_5b', 'QRSType1_5c'])
     else:
       pass
     qrs['EcgID']=file
     cols = list(qrs.columns)
     cols = [cols[-1]] + cols[:-1]
     qrs = qrs[cols]
     qrs_dict123.update({file: qrs})
     
qrs_123_df = pd.concat(qrs_dict123) 
qrs_123_df['EcgID'] = qrs_123_df['EcgID'].str.replace(r'.txt','')
qrs_123_df.columns.name = None
qrs_123_df.to_csv('Output/qrs/qrs_123_df.csv', index=False) 

qrs_dict124 = {}

for file in files124:
     qrs = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 90, skipfooter = 15)
     qrs = qrs[~qrs[0].str.contains("12SL", na=False)]
     qrs[0] = qrs[0].str.replace('-', ' -', regex=True)
     if qrs.shape[0] == 9:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5a'])
     elif qrs.shape[0] == 10:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a',9: 'QRSType1_5b'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5a', 'QRSType1_5b'])
     elif qrs.shape[0] == 11:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a',9: 'QRSType1_5b',10: 'QRSType1_5c'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.join(qrs['QRSType1_5c'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoC_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5a', 'QRSType1_5b', 'QRSType1_5c'])
     else:
       pass
     qrs['EcgID']=file
     cols = list(qrs.columns)
     cols = [cols[-1]] + cols[:-1]
     qrs = qrs[cols]
     qrs_dict124.update({file: qrs})
     
qrs_124_df = pd.concat(qrs_dict124) 
qrs_124_df['EcgID'] = qrs_124_df['EcgID'].str.replace(r'.txt','')
qrs_124_df.columns.name = None
qrs_124_df.to_csv('Output/qrs/qrs_124_df.csv', index=False) 

qrs_dict125 = {}

for file in files125:
     qrs = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 90, skipfooter = 15)
     qrs = qrs[~qrs[0].str.contains("12SL", na=False)]
     qrs[0] = qrs[0].str.replace('-', ' -', regex=True)
     if qrs.shape[0] == 9:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5a'])
     elif qrs.shape[0] == 10:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a',9: 'QRSType1_5b'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5a', 'QRSType1_5b'])
     elif qrs.shape[0] == 11:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a',9: 'QRSType1_5b',10: 'QRSType1_5c'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.join(qrs['QRSType1_5c'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoC_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5a', 'QRSType1_5b', 'QRSType1_5c'])
     elif qrs.shape[0] == 12:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a',9: 'QRSType1_5b',10: 'QRSType1_5c',11: 'QRSType1_5d'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.join(qrs['QRSType1_5c'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoC_'))
       qrs = qrs.join(qrs['QRSType1_5d'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoD_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5a', 'QRSType1_5b', 'QRSType1_5c', 'QRSType1_5d'])
     elif qrs.shape[0] == 13:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a',9: 'QRSType1_5b',10: 'QRSType1_5c',11: 'QRSType1_5d',12: 'QRSType1_5e'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.join(qrs['QRSType1_5c'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoC_'))
       qrs = qrs.join(qrs['QRSType1_5d'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoD_'))
       qrs = qrs.join(qrs['QRSType1_5e'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoE_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5a', 'QRSType1_5b', 'QRSType1_5c', 'QRSType1_5d','QRSType1_5e'])
     else:
       pass
     qrs['EcgID']=file
     cols = list(qrs.columns)
     cols = [cols[-1]] + cols[:-1]
     qrs = qrs[cols]
     qrs_dict125.update({file: qrs})
     
qrs_125_df = pd.concat(qrs_dict125) 
qrs_125_df['EcgID'] = qrs_125_df['EcgID'].str.replace(r'.txt','')
qrs_125_df.columns.name = None
qrs_125_df.to_csv('Output/qrs/qrs_125_df.csv', index=False) 

qrs_dict127 = {}

for file in files127:
     qrs = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 90, skipfooter = 14)
     qrs = qrs[~qrs[0].str.contains("12SL", na=False)]
     qrs[0] = qrs[0].str.replace('-', ' -', regex=True)
     if qrs.shape[0] == 9:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5'])
     elif qrs.shape[0] == 10:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a',9: 'QRSType1_5b'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5'])
     elif qrs.shape[0] == 12:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a',9: 'QRSType1_5b',10: 'QRSType1_5c',11: 'QRSType1_5d'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.join(qrs['QRSType1_5c'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoC_'))
       qrs = qrs.join(qrs['QRSType1_5d'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoD_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5a', 'QRSType1_5b', 'QRSType1_5c', 'QRSType1_5d'])
     elif qrs.shape[0] == 15:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'QRSNumber_add',8:'drop5', 9: 'QRSTYP_add',10: 'drop6',11: 'QRSTIM: (msec)_add',12: 'drop7',13:'drop8',14:'QRSType1_5a'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5','drop6','drop7','drop8'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSNumber_add'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_Add_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTYP_add'].str.split("\\s+", expand=True).add_prefix('QRSTYP_Add_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)_add'].str.split("\\s+", expand=True).add_prefix('QRSTIM_Add_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.drop(columns=['QRS','QRSNumber_add','QRSTYP','QRSTYP_add','QRSTIM: (msec)','QRSTIM: (msec)_add','QRSType1_5a'])
     elif qrs.shape[0] == 16:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'QRSNumber_add',8:'drop5', 9: 'QRSTYP_add',10: 'drop6',11: 'QRSTIM: (msec)_add',12: 'drop7',13:'drop8',14:'QRSType1_5a',15:'QRSType1_5b'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5','drop6','drop7','drop8'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSNumber_add'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_Add_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTYP_add'].str.split("\\s+", expand=True).add_prefix('QRSTYP_Add_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)_add'].str.split("\\s+", expand=True).add_prefix('QRSTIM_Add_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.drop(columns=['QRS','QRSNumber_add','QRSTYP','QRSTYP_add','QRSTIM: (msec)','QRSTIM: (msec)_add','QRSType1_5a','QRSType1_5b'])
     else:
       pass
     qrs['EcgID']=file
     cols = list(qrs.columns)
     cols = [cols[-1]] + cols[:-1]
     qrs = qrs[cols]
     qrs_dict127.update({file: qrs})
     
qrs_127_df = pd.concat(qrs_dict127) 
qrs_127_df['EcgID'] = qrs_127_df['EcgID'].str.replace(r'.txt','')
qrs_127_df.columns.name = None
qrs_127_df.to_csv('Output/qrs/qrs_127_df.csv', index=False) 

qrs_dict128 = {}

for file in files128:
     qrs = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 90, skipfooter = 15)
     qrs = qrs[~qrs[0].str.contains("12SL", na=False)]
     qrs[0] = qrs[0].str.replace('-', ' -', regex=True)
     if qrs.shape[0] == 9:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5'])
     elif qrs.shape[0] == 10:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a',9: 'QRSType1_5b'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5'])
     elif qrs.shape[0] == 15:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'QRSNumber_add',8:'drop5', 9: 'QRSTYP_add',10: 'drop6',11: 'QRSTIM: (msec)_add',12: 'drop7',13:'drop8',14:'QRSType1_5a'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5','drop6','drop7','drop8'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSNumber_add'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_Add_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTYP_add'].str.split("\\s+", expand=True).add_prefix('QRSTYP_Add_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)_add'].str.split("\\s+", expand=True).add_prefix('QRSTIM_Add_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.drop(columns=['QRS','QRSNumber_add','QRSTYP','QRSTYP_add','QRSTIM: (msec)','QRSTIM: (msec)_add','QRSType1_5a'])
     elif qrs.shape[0] == 16:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'QRSNumber_add',8:'drop5', 9: 'QRSTYP_add',10: 'drop6',11: 'QRSTIM: (msec)_add',12: 'drop7',13:'drop8',14:'QRSType1_5a',15:'QRSType1_5b'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5','drop6','drop7','drop8'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSNumber_add'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_Add_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTYP_add'].str.split("\\s+", expand=True).add_prefix('QRSTYP_Add_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)_add'].str.split("\\s+", expand=True).add_prefix('QRSTIM_Add_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.drop(columns=['QRS','QRSNumber_add','QRSTYP','QRSTYP_add','QRSTIM: (msec)','QRSTIM: (msec)_add','QRSType1_5a','QRSType1_5b'])
     else:
       pass
     qrs['EcgID']=file
     cols = list(qrs.columns)
     cols = [cols[-1]] + cols[:-1]
     qrs = qrs[cols]
     qrs_dict128.update({file: qrs})
     
qrs_128_df = pd.concat(qrs_dict128) 
qrs_128_df['EcgID'] = qrs_128_df['EcgID'].str.replace(r'.txt','')
qrs_128_df.columns.name = None
qrs_128_df.to_csv('Output/qrs/qrs_128_df.csv', index=False) 

qrs_dict129 = {}

for file in files129:
     qrs = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 90, skipfooter = 16)
     qrs = qrs[~qrs[0].str.contains("12SL", na=False)]
     qrs[0] = qrs[0].str.replace('-', ' -', regex=True)
     if qrs.shape[0] == 9:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5'])
     elif qrs.shape[0] == 10:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a',9: 'QRSType1_5b'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5'])
     elif qrs.shape[0] == 15:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'QRSNumber_add',8:'drop5', 9: 'QRSTYP_add',10: 'drop6',11: 'QRSTIM: (msec)_add',12: 'drop7',13:'drop8',14:'QRSType1_5a'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5','drop6','drop7','drop8'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSNumber_add'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_Add_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTYP_add'].str.split("\\s+", expand=True).add_prefix('QRSTYP_Add_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)_add'].str.split("\\s+", expand=True).add_prefix('QRSTIM_Add_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.drop(columns=['QRS','QRSNumber_add','QRSTYP','QRSTYP_add','QRSTIM: (msec)','QRSTIM: (msec)_add','QRSType1_5a'])
     elif qrs.shape[0] == 16:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'QRSNumber_add',8:'drop5', 9: 'QRSTYP_add',10: 'drop6',11: 'QRSTIM: (msec)_add',12: 'drop7',13:'drop8',14:'QRSType1_5a',15:'QRSType1_5b'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5','drop6','drop7','drop8'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSNumber_add'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_Add_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTYP_add'].str.split("\\s+", expand=True).add_prefix('QRSTYP_Add_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)_add'].str.split("\\s+", expand=True).add_prefix('QRSTIM_Add_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.drop(columns=['QRS','QRSNumber_add','QRSTYP','QRSTYP_add','QRSTIM: (msec)','QRSTIM: (msec)_add','QRSType1_5a','QRSType1_5b'])
     else:
       pass
     qrs['EcgID']=file
     cols = list(qrs.columns)
     cols = [cols[-1]] + cols[:-1]
     qrs = qrs[cols]
     qrs_dict129.update({file: qrs})
     
qrs_129_df = pd.concat(qrs_dict129) 
qrs_129_df['EcgID'] = qrs_129_df['EcgID'].str.replace(r'.txt','')
qrs_129_df.columns.name = None
qrs_129_df.to_csv('Output/qrs/qrs_129_df.csv', index=False) 

qrs_dict130 = {}

for file in files130:
     qrs = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 90, skipfooter = 16)
     qrs = qrs[~qrs[0].str.contains("12SL", na=False)]
     qrs[0] = qrs[0].str.replace('-', ' -', regex=True)
     if qrs.shape[0] == 9:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5'])
     elif qrs.shape[0] == 10:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a',9: 'QRSType1_5b'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5'])
     elif qrs.shape[0] == 15:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'QRSNumber_add',8:'drop5', 9: 'QRSTYP_add',10: 'drop6',11: 'QRSTIM: (msec)_add',12: 'drop7',13:'drop8',14:'QRSType1_5a'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5','drop6','drop7','drop8'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSNumber_add'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_Add_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTYP_add'].str.split("\\s+", expand=True).add_prefix('QRSTYP_Add_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)_add'].str.split("\\s+", expand=True).add_prefix('QRSTIM_Add_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.drop(columns=['QRS','QRSNumber_add','QRSTYP','QRSTYP_add','QRSTIM: (msec)','QRSTIM: (msec)_add','QRSType1_5a'])
     elif qrs.shape[0] == 16:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'QRSNumber_add',8:'drop5', 9: 'QRSTYP_add',10: 'drop6',11: 'QRSTIM: (msec)_add',12: 'drop7',13:'drop8',14:'QRSType1_5a',15:'QRSType1_5b'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5','drop6','drop7','drop8'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSNumber_add'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_Add_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTYP_add'].str.split("\\s+", expand=True).add_prefix('QRSTYP_Add_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)_add'].str.split("\\s+", expand=True).add_prefix('QRSTIM_Add_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.drop(columns=['QRS','QRSNumber_add','QRSTYP','QRSTYP_add','QRSTIM: (msec)','QRSTIM: (msec)_add','QRSType1_5a','QRSType1_5b'])
     elif qrs.shape[0] == 17:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'QRSNumber_add',8:'drop5', 9: 'QRSTYP_add',10: 'drop6',11: 'QRSTIM: (msec)_add',12: 'drop7',13:'drop8',14:'QRSType1_5a',15:'QRSType1_5b',16:'QRSType1_5c'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5','drop6','drop7','drop8'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSNumber_add'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_Add_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTYP_add'].str.split("\\s+", expand=True).add_prefix('QRSTYP_Add_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)_add'].str.split("\\s+", expand=True).add_prefix('QRSTIM_Add_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.join(qrs['QRSType1_5c'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoC_'))
       qrs = qrs.drop(columns=['QRS','QRSNumber_add','QRSTYP','QRSTYP_add','QRSTIM: (msec)','QRSTIM: (msec)_add','QRSType1_5a','QRSType1_5b','QRSType1_5c'])
     else:
       pass
     qrs['EcgID']=file
     cols = list(qrs.columns)
     cols = [cols[-1]] + cols[:-1]
     qrs = qrs[cols]
     qrs_dict130.update({file: qrs})
     
qrs_130_df = pd.concat(qrs_dict130) 
qrs_130_df['EcgID'] = qrs_130_df['EcgID'].str.replace(r'.txt','')
qrs_130_df.columns.name = None
qrs_130_df.to_csv('Output/qrs/qrs_130_df.csv', index=False) 

qrs_dict131 = {}

for file in files131:
     qrs = pd.read_fwf(file, header= None, colspecs = [(0, 100)], skiprows = 90, skipfooter = 15)
     qrs = qrs[~qrs[0].str.contains("12SL", na=False)]
     qrs[0] = qrs[0].str.replace('-', ' -', regex=True)
     if qrs.shape[0] == 9:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5'])
     elif qrs.shape[0] == 10:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'drop5',8: 'QRSType1_5a',9: 'QRSType1_5b'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.drop(columns=['QRS', 'QRSTYP','QRSTIM: (msec)', 'QRSType1_5'])
     elif qrs.shape[0] == 15:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'QRSNumber_add',8:'drop5', 9: 'QRSTYP_add',10: 'drop6',11: 'QRSTIM: (msec)_add',12: 'drop7',13:'drop8',14:'QRSType1_5a'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5','drop6','drop7','drop8'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSNumber_add'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_Add_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTYP_add'].str.split("\\s+", expand=True).add_prefix('QRSTYP_Add_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)_add'].str.split("\\s+", expand=True).add_prefix('QRSTIM_Add_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.drop(columns=['QRS','QRSNumber_add','QRSTYP','QRSTYP_add','QRSTIM: (msec)','QRSTIM: (msec)_add','QRSType1_5a'])
     elif qrs.shape[0] == 16:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'QRSNumber_add',8:'drop5', 9: 'QRSTYP_add',10: 'drop6',11: 'QRSTIM: (msec)_add',12: 'drop7',13:'drop8',14:'QRSType1_5a',15:'QRSType1_5b'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5','drop6','drop7','drop8'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSNumber_add'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_Add_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTYP_add'].str.split("\\s+", expand=True).add_prefix('QRSTYP_Add_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)_add'].str.split("\\s+", expand=True).add_prefix('QRSTIM_Add_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.drop(columns=['QRS','QRSNumber_add','QRSTYP','QRSTYP_add','QRSTIM: (msec)','QRSTIM: (msec)_add','QRSType1_5a','QRSType1_5b'])
     elif qrs.shape[0] == 17:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'QRSNumber_add',8:'drop5', 9: 'QRSTYP_add',10: 'drop6',11: 'QRSTIM: (msec)_add',12: 'drop7',13:'drop8',14:'QRSType1_5a',15:'QRSType1_5b',16:'QRSType1_5c'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5','drop6','drop7','drop8'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSNumber_add'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_Add_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTYP_add'].str.split("\\s+", expand=True).add_prefix('QRSTYP_Add_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)_add'].str.split("\\s+", expand=True).add_prefix('QRSTIM_Add_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.join(qrs['QRSType1_5c'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoC_'))
       qrs = qrs.drop(columns=['QRS','QRSNumber_add','QRSTYP','QRSTYP_add','QRSTIM: (msec)','QRSTIM: (msec)_add','QRSType1_5a','QRSType1_5b','QRSType1_5c'])
     elif qrs.shape[0] == 18:
       qrs = qrs.T
       qrs.rename(columns={0: 'drop1', 1: 'QRS',2: 'drop2', 3: 'QRSTYP',4: 'drop3', 5: 'QRSTIM: (msec)',6: 'drop4', 7: 'QRSNumber_add',8:'drop5', 9: 'QRSTYP_add',10: 'drop6',11: 'QRSTIM: (msec)_add',12: 'drop7',13:'drop8',14:'QRSType1_5a',15:'QRSType1_5b',16:'QRSType1_5c',17:'QRSType1_5d'}, inplace=True)
       qrs = qrs.drop(columns=['drop1', 'drop2','drop3', 'drop4','drop5','drop6','drop7','drop8'])
       qrs = qrs.join(qrs['QRS'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_'))
       qrs = qrs.join(qrs['QRSNumber_add'].str.split("\\s+", expand=True).add_prefix('QRSNUMBER_Add_'))
       qrs = qrs.join(qrs['QRSTYP'].str.split("\\s+", expand=True).add_prefix('QRSTYP_'))
       qrs = qrs.join(qrs['QRSTYP_add'].str.split("\\s+", expand=True).add_prefix('QRSTYP_Add_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)'].str.split("\\s+", expand=True).add_prefix('QRSTIM_'))
       qrs = qrs.join(qrs['QRSTIM: (msec)_add'].str.split("\\s+", expand=True).add_prefix('QRSTIM_Add_'))
       qrs = qrs.join(qrs['QRSType1_5a'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoA_'))
       qrs = qrs.join(qrs['QRSType1_5b'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoB_'))
       qrs = qrs.join(qrs['QRSType1_5c'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoC_'))
       qrs = qrs.join(qrs['QRSType1_5d'].str.split("\\s+", expand=True).add_prefix('QRSType1_5_infoD_'))
       qrs = qrs.drop(columns=['QRS','QRSNumber_add','QRSTYP','QRSTYP_add','QRSTIM: (msec)','QRSTIM: (msec)_add','QRSType1_5a','QRSType1_5b','QRSType1_5c','QRSType1_5d'])
     else:
       pass
     qrs['EcgID']=file
     cols = list(qrs.columns)
     cols = [cols[-1]] + cols[:-1]
     qrs = qrs[cols]
     qrs_dict131.update({file: qrs})
     
qrs_131_df = pd.concat(qrs_dict131) 
qrs_131_df['EcgID'] = qrs_131_df['EcgID'].str.replace(r'.txt','')
qrs_131_df.columns.name = None
qrs_131_df.to_csv('Output/qrs/qrs_131_df.csv', index=False) 
