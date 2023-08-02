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


demog_dict120 = {}

for file in files120:
     demog = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 4, skipfooter = 108) #check skip parameters 
     demog[['Variable','Value']] = demog[0].str.split(':',expand=True)
     demog.Value.fillna(demog.Variable, inplace=True)
     demog = demog.drop(columns=[0])
     demog['Variable'] = demog['Variable'].astype('str')
     if demog['Variable'].str.match('sex').sum() == 0:
      demog = pd.DataFrame(np.insert(demog.values, (1), df_NA_sex.values, axis=0), columns=demog.columns)
     else:
        pass
     if len(demog) > 8:
       demog = demog.iloc[:-1]
     else:
        pass
     demog['Value'] = demog['Value'].str.replace('female', '')
     demog['Value'] = demog['Value'].str.replace('male', '')
     demog['Value'] = demog['Value'].str.replace('ms', '')
     demog['Value'] = demog['Value'].str.replace('BPM', '')
     demog['Value'] = demog['Value'].str.replace('P-R-T axes ', '')
     demog['Value'] = demog['Value'].str.replace('/', ' ')
     demog['Value'] = demog['Value'].str.strip()
     demog['Value'] = demog['Value'].str.replace(r'\s+', ' ', regex=True).str.strip()
     demog = demog.T
     demog = demog.drop('Variable')
     demog[['QT','QTc']] = demog[6].str.split(' ',expand=True)
     demog[['P.axes','R.axes','T.axes']] = demog[7].str.split(' ',expand=True)
     demog = demog.drop(columns=[6,7])
     demog.rename(columns={0: 'age', 1:'sex',2: 'race',3: 'Vent.rate',4: 'PR.interval', 5: 'QRS.duration'}, inplace=True)
     demog['EcgID']=file
     demog.index.name = None
     demog_dict120.update({file: demog})
     
demog_dict120_df = pd.concat(demog_dict120) 
demog_dict120_df['EcgID'] = demog_dict120_df['EcgID'].str.replace(r'.txt','')
demog_dict120_df.columns.name = None
demog_dict120_df.to_csv('Output/demog/demog_dict120_df.csv', index=False) 

demog_dict121 = {}

for file in files121:
     demog = pd.read_fwf("70606622.txt", header= None,colspecs = [(0, 100)], skiprows = 4, skipfooter = 108)
     demog[['Variable','Value']] = demog[0].str.split(':',expand=True)
     demog.Value.fillna(demog.Variable, inplace=True)
     demog = demog.drop(columns=[0])
     demog['Variable'] = demog['Variable'].astype('str')
     if demog['Variable'].str.match('sex').sum() == 0:
      demog = pd.DataFrame(np.insert(demog.values, (1), df_NA_sex.values, axis=0), columns=demog.columns)
     else:
        pass
     if len(demog) > 8:
       demog = demog.iloc[:-1]
     else:
        pass
     demog['Value'] = demog['Value'].str.replace('female', '')
     demog['Value'] = demog['Value'].str.replace('male', '')
     demog['Value'] = demog['Value'].str.replace('ms', '')
     demog['Value'] = demog['Value'].str.replace('BPM', '')
     demog['Value'] = demog['Value'].str.replace('P-R-T axes ', '')
     demog['Value'] = demog['Value'].str.replace('/', ' ')
     demog['Value'] = demog['Value'].str.strip()
     demog['Value'] = demog['Value'].str.replace(r'\s+', ' ', regex=True).str.strip()
     demog = demog.T
     demog = demog.drop('Variable')
     demog[['QT','QTc']] = demog[6].str.split(' ',expand=True)
     demog[['P.axes','R.axes','T.axes']] = demog[7].str.split(' ',expand=True)
     demog = demog.drop(columns=[6,7])
     demog.rename(columns={0: 'age', 1: 'sex',2: 'race', 3: 'Vent.rate',4: 'PR.interval', 5: 'QRS.duration'}, inplace=True)
     demog['EcgID']=file
     demog.index.name = None
     demog_dict121.update({file: demog})
     
demog_dict121_df = pd.concat(demog_dict121) 
demog_dict121_df['EcgID'] = demog_dict121_df['EcgID'].str.replace(r'.txt','')
demog_dict121_df.columns.name = None
demog_dict121_df.to_csv('Output/demog/demog_dict121_df.csv', index=False) 

demog_dict122 = {}

for file in files122:
     demog = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 4, skipfooter = 109) #check skip parameters 
     demog[['Variable','Value']] = demog[0].str.split(':',expand=True)
     demog.Value.fillna(demog.Variable, inplace=True)
     demog = demog.drop(columns=[0])
     demog['Variable'] = demog['Variable'].astype('str')
     if demog['Variable'].str.match('sex').sum() == 0:
      demog = pd.DataFrame(np.insert(demog.values, (1), df_NA_sex.values, axis=0), columns=demog.columns)
     else:
        pass
     if len(demog) > 8:
       demog = demog.iloc[:-1]
     else:
        pass
     demog['Value'] = demog['Value'].str.replace('female', '')
     demog['Value'] = demog['Value'].str.replace('male', '')
     demog['Value'] = demog['Value'].str.replace('ms', '')
     demog['Value'] = demog['Value'].str.replace('BPM', '')
     demog['Value'] = demog['Value'].str.replace('P-R-T axes ', '')
     demog['Value'] = demog['Value'].str.replace('/', ' ')
     demog['Value'] = demog['Value'].str.strip()
     demog['Value'] = demog['Value'].str.replace(r'\s+', ' ', regex=True).str.strip()
     demog = demog.T
     demog = demog.drop('Variable')
     demog[['QT','QTc']] = demog[6].str.split(' ',expand=True)
     demog[['P.axes','R.axes','T.axes']] = demog[7].str.split(' ',expand=True)
     demog = demog.drop(columns=[6,7])
     demog.rename(columns={0: 'age', 1: 'sex',2: 'race', 3: 'Vent.rate',4: 'PR.interval', 5: 'QRS.duration'}, inplace=True)
     demog['EcgID']=file
     demog.index.name = None
     demog_dict122.update({file: demog})
     
demog_dict122_df = pd.concat(demog_dict122) 
demog_dict122_df['EcgID'] = demog_dict122_df['EcgID'].str.replace(r'.txt','')
demog_dict122_df.columns.name = None
demog_dict122_df.to_csv('Output/demog/demog_dict122_df.csv', index=False) 

demog_dict123 = {}

for file in files123:
     demog = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 4, skipfooter = 110) #check skip parameters 
     demog[['Variable','Value']] = demog[0].str.split(':',expand=True)
     demog.Value.fillna(demog.Variable, inplace=True)
     demog = demog.drop(columns=[0])
     demog['Variable'] = demog['Variable'].astype('str')
     if demog['Variable'].str.match('sex').sum() == 0:
      demog = pd.DataFrame(np.insert(demog.values, (1), df_NA_sex.values, axis=0), columns=demog.columns)
     else:
        pass
     if len(demog) > 8:
       demog = demog.iloc[:-1]
     else:
        pass
     demog['Value'] = demog['Value'].str.replace('female', '')
     demog['Value'] = demog['Value'].str.replace('male', '')
     demog['Value'] = demog['Value'].str.replace('ms', '')
     demog['Value'] = demog['Value'].str.replace('BPM', '')
     demog['Value'] = demog['Value'].str.replace('P-R-T axes ', '')
     demog['Value'] = demog['Value'].str.replace('/', ' ')
     demog['Value'] = demog['Value'].str.strip()
     demog['Value'] = demog['Value'].str.replace(r'\s+', ' ', regex=True).str.strip()
     demog = demog.T
     demog = demog.drop('Variable')
     demog[['QT','QTc']] = demog[6].str.split(' ',expand=True)
     demog[['P.axes','R.axes','T.axes']] = demog[7].str.split(' ',expand=True)
     demog = demog.drop(columns=[6,7])
     demog.rename(columns={0: 'age', 1: 'sex',2: 'race', 3: 'Vent.rate',4: 'PR.interval', 5: 'QRS.duration'}, inplace=True)
     demog['EcgID']=file
     demog.index.name = None
     demog_dict123.update({file: demog})
     
demog_dict123_df = pd.concat(demog_dict123) 
demog_dict123_df['EcgID'] = demog_dict123_df['EcgID'].str.replace(r'.txt','')
demog_dict123_df.columns.name = None
demog_dict123_df.to_csv('Output/demog/demog_dict123_df.csv', index=False) 

demog_dict124 = {}

for file in files124:
     demog = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 4, skipfooter = 110) #check skip parameters 
     demog[['Variable','Value']] = demog[0].str.split(':',expand=True)
     demog.Value.fillna(demog.Variable, inplace=True)
     demog = demog.drop(columns=[0])
     demog['Variable'] = demog['Variable'].astype('str')
     if demog['Variable'].str.match('sex').sum() == 0:
      demog = pd.DataFrame(np.insert(demog.values, (1), df_NA_sex.values, axis=0), columns=demog.columns)
     else:
        pass
     if len(demog) > 8:
       demog = demog.iloc[:-1]
     else:
        pass
     demog['Value'] = demog['Value'].str.replace('female', '')
     demog['Value'] = demog['Value'].str.replace('male', '')
     demog['Value'] = demog['Value'].str.replace('ms', '')
     demog['Value'] = demog['Value'].str.replace('BPM', '')
     demog['Value'] = demog['Value'].str.replace('P-R-T axes ', '')
     demog['Value'] = demog['Value'].str.replace('/', ' ')
     demog['Value'] = demog['Value'].str.strip()
     demog['Value'] = demog['Value'].str.replace(r'\s+', ' ', regex=True).str.strip()
     demog = demog.T
     demog = demog.drop('Variable')
     demog[['QT','QTc']] = demog[6].str.split(' ',expand=True)
     demog[['P.axes','R.axes','T.axes']] = demog[7].str.split(' ',expand=True)
     demog = demog.drop(columns=[6,7])
     demog.rename(columns={0: 'age', 1: 'sex',2: 'race', 3: 'Vent.rate',4: 'PR.interval', 5: 'QRS.duration'}, inplace=True)
     demog['EcgID']=file
     demog.index.name = None
     demog_dict124.update({file: demog})
     
demog_dict124_df = pd.concat(demog_dict124) 
demog_dict124_df['EcgID'] = demog_dict124_df['EcgID'].str.replace(r'.txt','')
demog_dict124_df.columns.name = None
demog_dict124_df.to_csv('Output/demog/demog_dict124_df.csv', index=False) 

demog_dict125 = {}

for file in files125:
     demog = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 4, skipfooter = 111) #check skip parameters 
     demog[['Variable','Value']] = demog[0].str.split(':',expand=True)
     demog.Value.fillna(demog.Variable, inplace=True)
     demog = demog.drop(columns=[0])
     demog['Variable'] = demog['Variable'].astype('str')
     if demog['Variable'].str.match('sex').sum() == 0:
      demog = pd.DataFrame(np.insert(demog.values, (1), df_NA_sex.values, axis=0), columns=demog.columns)
     else:
        pass
     if len(demog) > 8:
       demog = demog.iloc[:-1]
     else:
        pass
     demog['Value'] = demog['Value'].str.replace('female', '')
     demog['Value'] = demog['Value'].str.replace('male', '')
     demog['Value'] = demog['Value'].str.replace('ms', '')
     demog['Value'] = demog['Value'].str.replace('BPM', '')
     demog['Value'] = demog['Value'].str.replace('P-R-T axes ', '')
     demog['Value'] = demog['Value'].str.replace('/', ' ')
     demog['Value'] = demog['Value'].str.strip()
     demog['Value'] = demog['Value'].str.replace(r'\s+', ' ', regex=True).str.strip()
     demog = demog.T
     demog = demog.drop('Variable')
     demog[['QT','QTc']] = demog[6].str.split(' ',expand=True)
     demog[['P.axes','R.axes','T.axes']] = demog[7].str.split(' ',expand=True)
     demog = demog.drop(columns=[6,7])
     demog.rename(columns={0: 'age', 1: 'sex',2: 'race', 3: 'Vent.rate',4: 'PR.interval', 5: 'QRS.duration'}, inplace=True)
     demog['EcgID']=file
     demog.index.name = None
     demog_dict125.update({file: demog})
     
demog_dict125_df = pd.concat(demog_dict125) 
demog_dict125_df['EcgID'] = demog_dict125_df['EcgID'].str.replace(r'.txt','')
demog_dict125_df.columns.name = None
demog_dict125_df.to_csv('Output/demog/demog_dict125_df.csv', index=False) 

demog_dict127 = {}

for file in files127:
     demog = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 4, skipfooter = 113) #check skip parameters 
     demog[['Variable','Value']] = demog[0].str.split(':',expand=True)
     demog.Value.fillna(demog.Variable, inplace=True)
     demog = demog.drop(columns=[0])
     demog['Variable'] = demog['Variable'].astype('str')
     if demog['Variable'].str.match('sex').sum() == 0:
      demog = pd.DataFrame(np.insert(demog.values, (1), df_NA_sex.values, axis=0), columns=demog.columns)
     else:
        pass
     if len(demog) > 8:
       demog = demog.iloc[:-1]
     else:
        pass
     demog['Value'] = demog['Value'].str.replace('female', '')
     demog['Value'] = demog['Value'].str.replace('male', '')
     demog['Value'] = demog['Value'].str.replace('ms', '')
     demog['Value'] = demog['Value'].str.replace('BPM', '')
     demog['Value'] = demog['Value'].str.replace('P-R-T axes ', '')
     demog['Value'] = demog['Value'].str.replace('/', ' ')
     demog['Value'] = demog['Value'].str.strip()
     demog['Value'] = demog['Value'].str.replace(r'\s+', ' ', regex=True).str.strip()
     demog = demog.T
     demog = demog.drop('Variable')
     demog[['QT','QTc']] = demog[6].str.split(' ',expand=True)
     demog[['P.axes','R.axes','T.axes']] = demog[7].str.split(' ',expand=True)
     demog = demog.drop(columns=[6,7])
     demog.rename(columns={0: 'age', 1: 'sex',2: 'race', 3: 'Vent.rate',4: 'PR.interval', 5: 'QRS.duration'}, inplace=True)
     demog['EcgID']=file
     demog.index.name = None
     demog_dict127.update({file: demog})
     
demog_dict127_df = pd.concat(demog_dict127) 
demog_dict127_df['EcgID'] = demog_dict127_df['EcgID'].str.replace(r'.txt','')
demog_dict127_df.columns.name = None
demog_dict127_df.to_csv('Output/demog/demog_dict127_df.csv', index=False) 

demog_dict128 = {}

for file in files128:
     demog = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 4, skipfooter = 114) #check skip parameters 
     demog[['Variable','Value']] = demog[0].str.split(':',expand=True)
     demog.Value.fillna(demog.Variable, inplace=True)
     demog = demog.drop(columns=[0])
     demog['Variable'] = demog['Variable'].astype('str')
     if demog['Variable'].str.match('sex').sum() == 0:
      demog = pd.DataFrame(np.insert(demog.values, (1), df_NA_sex.values, axis=0), columns=demog.columns)
     else:
        pass
     if len(demog) > 8:
       demog = demog.iloc[:-1]
     else:
        pass
     demog['Value'] = demog['Value'].str.replace('female', '')
     demog['Value'] = demog['Value'].str.replace('male', '')
     demog['Value'] = demog['Value'].str.replace('ms', '')
     demog['Value'] = demog['Value'].str.replace('BPM', '')
     demog['Value'] = demog['Value'].str.replace('P-R-T axes ', '')
     demog['Value'] = demog['Value'].str.replace('/', ' ')
     demog['Value'] = demog['Value'].str.strip()
     demog['Value'] = demog['Value'].str.replace(r'\s+', ' ', regex=True).str.strip()
     demog = demog.T
     demog = demog.drop('Variable')
     demog[['QT','QTc']] = demog[6].str.split(' ',expand=True)
     demog[['P.axes','R.axes','T.axes']] = demog[7].str.split(' ',expand=True)
     demog = demog.drop(columns=[6,7])
     demog.rename(columns={0: 'age', 1: 'sex',2: 'race', 3: 'Vent.rate',4: 'PR.interval', 5: 'QRS.duration'}, inplace=True)
     demog['EcgID']=file
     demog.index.name = None
     demog_dict128.update({file: demog})
     
demog_dict128_df = pd.concat(demog_dict128) 
demog_dict128_df['EcgID'] = demog_dict128_df['EcgID'].str.replace(r'.txt','')
demog_dict128_df.columns.name = None
demog_dict128_df.to_csv('Output/demog/demog_dict128_df.csv', index=False) 

demog_dict129 = {}

for file in files129:
     demog = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 4, skipfooter = 115) #check skip parameters 
     demog[['Variable','Value']] = demog[0].str.split(':',expand=True)
     demog.Value.fillna(demog.Variable, inplace=True)
     demog = demog.drop(columns=[0])
     demog['Variable'] = demog['Variable'].astype('str')
     if demog['Variable'].str.match('sex').sum() == 0:
      demog = pd.DataFrame(np.insert(demog.values, (1), df_NA_sex.values, axis=0), columns=demog.columns)
     else:
        pass
     if len(demog) > 8:
       demog = demog.iloc[:-1]
     else:
        pass
     demog['Value'] = demog['Value'].str.replace('female', '')
     demog['Value'] = demog['Value'].str.replace('male', '')
     demog['Value'] = demog['Value'].str.replace('ms', '')
     demog['Value'] = demog['Value'].str.replace('BPM', '')
     demog['Value'] = demog['Value'].str.replace('P-R-T axes ', '')
     demog['Value'] = demog['Value'].str.replace('/', ' ')
     demog['Value'] = demog['Value'].str.strip()
     demog['Value'] = demog['Value'].str.replace(r'\s+', ' ', regex=True).str.strip()
     demog = demog.T
     demog = demog.drop('Variable')
     demog[['QT','QTc']] = demog[6].str.split(' ',expand=True)
     demog[['P.axes','R.axes','T.axes']] = demog[7].str.split(' ',expand=True)
     demog = demog.drop(columns=[6,7])
     demog.rename(columns={0: 'age', 1: 'sex',2: 'race', 3: 'Vent.rate',4: 'PR.interval', 5: 'QRS.duration'}, inplace=True)
     demog['EcgID']=file
     demog.index.name = None
     demog_dict129.update({file: demog})
     
demog_dict129_df = pd.concat(demog_dict129) 
demog_dict129_df['EcgID'] = demog_dict129_df['EcgID'].str.replace(r'.txt','')
demog_dict129_df.columns.name = None
demog_dict129_df.to_csv('Output/demog/demog_dict129_df.csv', index=False) 

demog_dict130 = {}

for file in files130:
     demog = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 4, skipfooter = 116) #check skip parameters 
     demog[['Variable','Value']] = demog[0].str.split(':',expand=True)
     demog.Value.fillna(demog.Variable, inplace=True)
     demog = demog.drop(columns=[0])
     demog['Variable'] = demog['Variable'].astype('str')
     if demog['Variable'].str.match('sex').sum() == 0:
      demog = pd.DataFrame(np.insert(demog.values, (1), df_NA_sex.values, axis=0), columns=demog.columns)
     else:
        pass
     if len(demog) > 8:
       demog = demog.iloc[:-1]
     else:
        pass
     demog['Value'] = demog['Value'].str.replace('female', '')
     demog['Value'] = demog['Value'].str.replace('male', '')
     demog['Value'] = demog['Value'].str.replace('ms', '')
     demog['Value'] = demog['Value'].str.replace('BPM', '')
     demog['Value'] = demog['Value'].str.replace('P-R-T axes ', '')
     demog['Value'] = demog['Value'].str.replace('/', ' ')
     demog['Value'] = demog['Value'].str.strip()
     demog['Value'] = demog['Value'].str.replace(r'\s+', ' ', regex=True).str.strip()
     demog = demog.T
     demog = demog.drop('Variable')
     demog[['QT','QTc']] = demog[6].str.split(' ',expand=True)
     demog[['P.axes','R.axes','T.axes']] = demog[7].str.split(' ',expand=True)
     demog = demog.drop(columns=[6,7])
     demog.rename(columns={0: 'age', 1: 'sex',2: 'race', 3: 'Vent.rate',4: 'PR.interval', 5: 'QRS.duration'}, inplace=True)
     demog['EcgID']=file
     demog.index.name = None
     demog_dict130.update({file: demog})
     
demog_dict130_df = pd.concat(demog_dict130) 
demog_dict130_df['EcgID'] = demog_dict130_df['EcgID'].str.replace(r'.txt','')
demog_dict130_df.columns.name = None
demog_dict130_df.to_csv('Output/demog/demog_dict130_df.csv', index=False) 

demog_dict131 = {}

for file in files131:
     demog = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 4, skipfooter = 117) #check skip parameters 
     demog[['Variable','Value']] = demog[0].str.split(':',expand=True)
     demog.Value.fillna(demog.Variable, inplace=True)
     demog = demog.drop(columns=[0])
     demog['Variable'] = demog['Variable'].astype('str')
     if demog['Variable'].str.match('sex').sum() == 0:
      demog = pd.DataFrame(np.insert(demog.values, (1), df_NA_sex.values, axis=0), columns=demog.columns)
     else:
        pass
     if len(demog) > 8:
       demog = demog.iloc[:-1]
     else:
        pass
     demog['Value'] = demog['Value'].str.replace('female', '')
     demog['Value'] = demog['Value'].str.replace('male', '')
     demog['Value'] = demog['Value'].str.replace('ms', '')
     demog['Value'] = demog['Value'].str.replace('BPM', '')
     demog['Value'] = demog['Value'].str.replace('P-R-T axes ', '')
     demog['Value'] = demog['Value'].str.replace('/', ' ')
     demog['Value'] = demog['Value'].str.strip()
     demog['Value'] = demog['Value'].str.replace(r'\s+', ' ', regex=True).str.strip()
     demog = demog.T
     demog = demog.drop('Variable')
     demog[['QT','QTc']] = demog[6].str.split(' ',expand=True)
     demog[['P.axes','R.axes','T.axes']] = demog[7].str.split(' ',expand=True)
     demog = demog.drop(columns=[6,7])
     demog.rename(columns={0: 'age', 1: 'sex',2: 'race', 3: 'Vent.rate',4: 'PR.interval', 5: 'QRS.duration'}, inplace=True)
     demog['EcgID']=file
     demog.index.name = None
     demog_dict131.update({file: demog})
     
demog_dict131_df = pd.concat(demog_dict131) 
demog_dict131_df['EcgID'] = demog_dict131_df['EcgID'].str.replace(r'.txt','')
demog_dict131_df.columns.name = None
demog_dict131_df.to_csv('Output/demog/demog_dict131_df.csv', index=False) 
