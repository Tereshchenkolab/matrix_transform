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


leads_dict120 = {}

for file in files120:
     leads = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 14, skipfooter = 38)
     leads[['Variable','I','II','V1','V2','V3','V4','V5','V6','III','aVR','aVL','aVF']] = leads[0].str.split("\\s+",expand=True)
     leads = leads.drop(columns=[0])
     if leads.shape[0] > 54:
       leads = leads.tail(-1)
     else:
        pass
     leads = leads.to_numpy().flatten()
     leads = pd.DataFrame(leads).T
     leads.columns = ['leads_'+str(i) for i in range(0,702)]
     leads['EcgID']=file
     leads_dict120.update({file: leads})
     
leads_dict120_df = pd.concat(leads_dict120) 
leads_dict120_df['EcgID'] = leads_dict120_df['EcgID'].str.replace(r'.txt','')
leads_dict120_df.columns.name = None
leads_dict120_df.to_csv('Output/leads/leads_dict120_df.csv', index=False) 


leads_dict121 = {}

for file in files121:
     leads = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 14, skipfooter = 38)
     leads[['Variable','I','II','V1','V2','V3','V4','V5','V6','III','aVR','aVL','aVF']] = leads[0].str.split("\\s+",expand=True)
     leads = leads.drop(columns=[0])
     if leads.shape[0] > 54:
       leads = leads.tail(-1)
     else:
        pass
     leads = leads.to_numpy().flatten()
     leads = pd.DataFrame(leads).T
     leads.columns = ['leads_'+str(i) for i in range(0,702)]
     leads['EcgID']=file
     leads_dict121.update({file: leads})
     
leads_dict121_df = pd.concat(leads_dict121) 
leads_dict121_df['EcgID'] = leads_dict121_df['EcgID'].str.replace(r'.txt','')
leads_dict121_df.columns.name = None
leads_dict121_df.to_csv('Output/leads/leads_dict121_df.csv', index=False) 

leads_dict122 = {}

for file in files122:
     leads = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 14, skipfooter = 39)
     leads[['Variable','I','II','V1','V2','V3','V4','V5','V6','III','aVR','aVL','aVF']] = leads[0].str.split("\\s+",expand=True)
     leads = leads.drop(columns=[0])
     if leads.shape[0] > 54:
       leads = leads.tail(-1)
     else:
        pass
     leads = leads.to_numpy().flatten()
     leads = pd.DataFrame(leads).T
     leads.columns = ['leads_'+str(i) for i in range(0,702)]
     leads['EcgID']=file
     leads_dict122.update({file: leads})
     
leads_dict122_df = pd.concat(leads_dict122) 
leads_dict122_df['EcgID'] = leads_dict122_df['EcgID'].str.replace(r'.txt','')
leads_dict122_df.columns.name = None
leads_dict122_df.to_csv('Output/leads/leads_dict122_df.csv', index=False) 

leads_dict123 = {}

for file in files123:
     leads = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 14, skipfooter = 40)
     leads[['Variable','I','II','V1','V2','V3','V4','V5','V6','III','aVR','aVL','aVF']] = leads[0].str.split("\\s+",expand=True)
     leads = leads.drop(columns=[0])
     if leads.shape[0] > 54:
       leads = leads.tail(-1)
     else:
        pass
     leads = leads.to_numpy().flatten()
     leads = pd.DataFrame(leads).T
     leads.columns = ['leads_'+str(i) for i in range(0,702)]
     leads['EcgID']=file
     leads_dict123.update({file: leads})
     
leads_dict123_df = pd.concat(leads_dict123) 
leads_dict123_df['EcgID'] = leads_dict123_df['EcgID'].str.replace(r'.txt','')
leads_dict123_df.columns.name = None
leads_dict123_df.to_csv('Output/leads/leads_dict123_df.csv', index=False) 

leads_dict124 = {}

for file in files124:
     leads = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 14, skipfooter = 41)
     leads[['Variable','I','II','V1','V2','V3','V4','V5','V6','III','aVR','aVL','aVF']] = leads[0].str.split("\\s+",expand=True)
     leads = leads.drop(columns=[0])
     if leads.shape[0] > 54:
       leads = leads.tail(-1)
     else:
        pass
     leads = leads.to_numpy().flatten()
     leads = pd.DataFrame(leads).T
     leads.columns = ['leads_'+str(i) for i in range(0,702)]
     leads['EcgID']=file
     leads_dict124.update({file: leads})
     
leads_dict124_df = pd.concat(leads_dict124) 
leads_dict124_df['EcgID'] = leads_dict124_df['EcgID'].str.replace(r'.txt','')
leads_dict124_df.columns.name = None
leads_dict124_df.to_csv('Output/leads/leads_dict124_df.csv', index=False) 

leads_dict125 = {}

for file in files125:
     leads = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 14, skipfooter = 42)
     leads[['Variable','I','II','V1','V2','V3','V4','V5','V6','III','aVR','aVL','aVF']] = leads[0].str.split("\\s+",expand=True)
     leads = leads.drop(columns=[0])
     if leads.shape[0] > 54:
       leads = leads.tail(-1)
     else:
        pass
     leads = leads.to_numpy().flatten()
     leads = pd.DataFrame(leads).T
     leads.columns = ['leads_'+str(i) for i in range(0,702)]
     leads['EcgID']=file
     leads_dict125.update({file: leads})
     
leads_dict125_df = pd.concat(leads_dict125) 
leads_dict125_df['EcgID'] = leads_dict125_df['EcgID'].str.replace(r'.txt','')
leads_dict125_df.columns.name = None
leads_dict125_df.to_csv('Output/leads/leads_dict125_df.csv', index=False) 

leads_dict127 = {}

for file in files127:
     leads = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 14, skipfooter = 44)
     leads[['Variable','I','II','V1','V2','V3','V4','V5','V6','III','aVR','aVL','aVF']] = leads[0].str.split("\\s+",expand=True)
     leads = leads.drop(columns=[0])
     if leads.shape[0] > 54:
       leads = leads.tail(-1)
     else:
        pass
     leads = leads.to_numpy().flatten()
     leads = pd.DataFrame(leads).T
     leads.columns = ['leads_'+str(i) for i in range(0,702)]
     leads['EcgID']=file
     leads_dict127.update({file: leads})
     
leads_dict127_df = pd.concat(leads_dict127) 
leads_dict127_df['EcgID'] = leads_dict127_df['EcgID'].str.replace(r'.txt','')
leads_dict127_df.columns.name = None
leads_dict127_df.to_csv('Output/leads/leads_dict127_df.csv', index=False) 

leads_dict128 = {}

for file in files128:
     leads = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 14, skipfooter = 45)
     leads[['Variable','I','II','V1','V2','V3','V4','V5','V6','III','aVR','aVL','aVF']] = leads[0].str.split("\\s+",expand=True)
     leads = leads.drop(columns=[0])
     if leads.shape[0] > 54:
       leads = leads.tail(-1)
     else:
        pass
     leads = leads.to_numpy().flatten()
     leads = pd.DataFrame(leads).T
     leads.columns = ['leads_'+str(i) for i in range(0,702)]
     leads['EcgID']=file
     leads_dict128.update({file: leads})
     
leads_dict128_df = pd.concat(leads_dict128) 
leads_dict128_df['EcgID'] = leads_dict128_df['EcgID'].str.replace(r'.txt','')
leads_dict128_df.columns.name = None
leads_dict128_df.to_csv('Output/leads/leads_dict128_df.csv', index=False) 

leads_dict129 = {}

for file in files129:
     leads = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 14, skipfooter = 46)
     leads[['Variable','I','II','V1','V2','V3','V4','V5','V6','III','aVR','aVL','aVF']] = leads[0].str.split("\\s+",expand=True)
     leads = leads.drop(columns=[0])
     if leads.shape[0] > 54:
       leads = leads.tail(-1)
     else:
        pass
     leads = leads.to_numpy().flatten()
     leads = pd.DataFrame(leads).T
     leads.columns = ['leads_'+str(i) for i in range(0,702)]
     leads['EcgID']=file
     leads_dict129.update({file: leads})
     
leads_dict129_df = pd.concat(leads_dict129) 
leads_dict129_df['EcgID'] = leads_dict129_df['EcgID'].str.replace(r'.txt','')
leads_dict129_df.columns.name = None
leads_dict129_df.to_csv('Output/leads/leads_dict129_df.csv', index=False) 

leads_dict130 = {}

for file in files130:
     leads = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 14, skipfooter = 47)
     leads[['Variable','I','II','V1','V2','V3','V4','V5','V6','III','aVR','aVL','aVF']] = leads[0].str.split("\\s+",expand=True)
     leads = leads.drop(columns=[0])
     if leads.shape[0] > 54:
       leads = leads.tail(-1)
     else:
        pass
     leads = leads.to_numpy().flatten()
     leads = pd.DataFrame(leads).T
     leads.columns = ['leads_'+str(i) for i in range(0,702)]
     leads['EcgID']=file
     leads_dict130.update({file: leads})
     
leads_dict130_df = pd.concat(leads_dict130) 
leads_dict130_df['EcgID'] = leads_dict130_df['EcgID'].str.replace(r'.txt','')
leads_dict130_df.columns.name = None
leads_dict130_df.to_csv('Output/leads/leads_dict130_df.csv', index=False) 

leads_dict131 = {}

for file in files131:
     leads = pd.read_fwf(file, header= None,colspecs = [(0, 100)], skiprows = 14, skipfooter = 48)
     leads[['Variable','I','II','V1','V2','V3','V4','V5','V6','III','aVR','aVL','aVF']] = leads[0].str.split("\\s+",expand=True)
     leads = leads.drop(columns=[0])
     if leads.shape[0] > 54:
       leads = leads.tail(-1)
     else:
        pass
     leads = leads.to_numpy().flatten()
     leads = pd.DataFrame(leads).T
     leads.columns = ['leads_'+str(i) for i in range(0,702)]
     leads['EcgID']=file
     leads_dict131.update({file: leads})
     
leads_dict131_df = pd.concat(leads_dict131) 
leads_dict131_df['EcgID'] = leads_dict131_df['EcgID'].str.replace(r'.txt','')
leads_dict131_df.columns.name = None
leads_dict131_df.to_csv('Output/leads/leads_dict131_df.csv', index=False) 



