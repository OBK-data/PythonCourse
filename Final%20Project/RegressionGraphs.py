import statsmodels.api as sm
import statsmodels.formula.api as smf
import pandas as pd
from scipy.stats import kurtosis, skew
import matplotlib.pyplot as plt

#Get the Data for Analysis
data = pd.read_csv ("test.csv", sep=',', low_memory =False, header = 0)
#Renaming all varibles for eaasiness
data.columns = ["Days", "ConspiracyFrequency", "USDTRYExchangeRate", "USDTRYExchangeChange","TotalConfirmedCases","Stringencyindex","Governmentresponseindex","Totaldeaths","GoogleSeach", "DailyConfirmedCases"]

# Line Graph for Stringency and Tweets (dependent variable and independent variable)
fig, ax = plt.subplots()
ax.plot(data["ConspiracyFrequency"], color='red')
ax.tick_params(axis='y', labelcolor='red')
ax2 = ax.twinx()
ax2.plot(data["Stringencyindex"], color='green')
ax2.tick_params(axis='y', labelcolor='green')
plt.show()

# Historgram for Dependent Variable

plt.hist(data.ConspiracyFrequency,bins=12,
         color='#213887',label="Conspiracy Tweets")

plt.xlabel("Count")
plt.ylabel("Numbers")
plt.legend()
plt.title("Conspiracy Tweet Distrubiton")

plt.show()
#checking Skew and Kurtosis to see fit for normal distrubtion
print( 'Kurtosis {}'.format( kurtosis(data.ConspiracyFrequency) ))
print( 'Skew: {}'.format( skew(data.ConspiracyFrequency) ))
#Because it does not fit, I will use negative binomial. My data is a count data which makes it eligable to Poisson and Negative Binomial Regression. However, my data is highly overdispersed so I will use a negative binomial regression.
model = smf.glm(formula = "ConspiracyFrequency ~ USDTRYExchangeRate + Stringencyindex + GoogleSeach + DailyConfirmedCases", data=data, family=sm.families.NegativeBinomial()).fit()
print(model.summary())
#Model 2 Regression (Government Response instead of Stringency)
model2 = smf.glm(formula = "ConspiracyFrequency ~ USDTRYExchangeRate + Governmentresponseindex + GoogleSeach + DailyConfirmedCases", data=data, family=sm.families.NegativeBinomial()).fit()
print(model2.summary())
#Model 3 Regression (Total Cases instead of Daily Cases)
model3 = smf.glm(formula = "ConspiracyFrequency ~ USDTRYExchangeRate + Stringencyindex + GoogleSeach +TotalConfirmedCases", data=data, family=sm.families.NegativeBinomial()).fit()
print(model3.summary())
#Model 4 Regression (Total Deaths instead of Daily Cases)
model4 = smf.glm(formula = "ConspiracyFrequency ~ USDTRYExchangeRate + Stringencyindex + GoogleSeach + Totaldeaths", data=data, family=sm.families.NegativeBinomial()).fit()
print(model4.summary())
