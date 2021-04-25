import wbdata
import csv
import pandas as pd
import numpy as np
import lr

countries=([i['id'] for i in wbdata.get_country(incomelevel="MIC")]) #middle income scrape
countries.extend([i['id'] for i in wbdata.get_country(incomelevel="LIC")]) #low income scrape
variables = { "NY.GDP.PCAP.PP.CD": "GPC" , "HD.HCI.OVRL.FE": "HCIFem" , "IQ.CPA.TRAN.XQ": "corruption" , "NY.GDP.PETR.RT.ZS" : "oilrents" , "PV.EST": "absenceofpeace"} #my variables
df = wbdata.get_dataframe(variables, country=countries) #data frome
df.to_csv('hw2OBK.csv') #turnsintocsv

df.dropna(inplace = True) #drops NaNs
depvar = np.array(df.iloc[:, :1]) #dependent variable
invar = np.array(df.iloc[:,1:]) #independent variable
lr.lregress(depvar, invar)
