import pandas as pd
import numpy as np
#Tweet Data Preparation
covidfreq = pd.read_csv ("covidconspiracyturkeyfinal.csv")
covidfreq.drop_duplicates(subset=["tweet"]) #remove duplicate Tweets
print(covidfreq)
covid_freq = pd.crosstab(index=covidfreq["date"], columns="count") #take frequency of COVID-19 related conspiracy tweets taking the dates as basis
#covid_freq.to_csv("covdat.csv") #test csv


#downloaded USD/TRY parity from https://evds2.tcmb.gov.tr/index.php?/evds/serieMarket/#collapse_2
#Turkish Central Bank (as far as I know it has no API amd scraping would be counterintuitive)
exch = pd.read_csv ("USD-TRY.csv", sep=',', low_memory =False)
exch1 = exch.iloc[1:433,1:]#selects relevant dates and variables

#Oxford Data on Government Response and Covid-19 cases (API was json and did not include Government Response Index)

govres = pd.read_csv ("OxCGRT_latest.csv")
govres1 = govres.filter(['CountryName','Date',"ConfirmedCases" ,'StringencyIndex', "GovernmentResponseIndex","ConfirmedDeaths"]) #drops unnecessary variables
govres2= govres1.loc[govres1.CountryName =='Turkey']#Turkey only
govres3 = govres2[(govres2['Date']).between(20200311, 20210516)] #select dates
govres4 = govres3.drop(["CountryName","Date"], axis = 1) #drops other redundant variables
#govres2.to_csv("covdata.csv") #test csv

#Google Trends data
trends = pd.read_csv ("googletrend.csv")
trends2 = trends.filter(["Vaccine 5G", "plandemic", "anti mask", "Great Reset","Bill Gates Vaccine"]).sum(axis = 1 ) #multiplies all of the trends
#trends2.to_csv("fulltrend.csv") #test csv
trendsfin =  trends2.iloc[10:442] #picks relevant dates
govresdail = govres3.ConfirmedCases.diff()#finds daily number of cases
govresdail.iloc[0] = 1 #adds patient zero to the first date
#resets index numbers against any confusion
covid_freq.reset_index(drop=True, inplace=True)
exch1.reset_index(drop=True, inplace=True)
govres4.reset_index(drop=True, inplace=True)
trendsfin.reset_index(drop=True, inplace=True)
govresdail.reset_index(drop=True, inplace=True)
#combines the data under a single csv
cleandata= pd.concat([covid_freq,exch1,govres4,trendsfin,govresdail], axis = 1)
cleandata.to_csv("test.csv") #saves CSV
