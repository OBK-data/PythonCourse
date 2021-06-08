import os
import twint
import unicodedata

#I had to run the program for each term separately becuase twint did not work properly with mulitple keywords (I have tried to feed the keywords as list, using OR operator between each keywords, doing a for loop for each keywords which either did not work or gave English tweets. )
#Some examples of non-working variations
#c.Search = "plandemi lang:tr" or "plandemic lang:tr" or "bill gates covid-19 lang:tr" or "great reset lang:tr" or "aşı 5G lang:tr" or "bill gates çip lang:tr" or "salgın yalanı lang:tr" or "maske yalanı lang:tr" or "bill gates aşı lang:tr" or "büyük sıfırlama lang:tr" or "yeni dünya düzeni lang:tr" or "aşı mikroçip lang:tr" or "aşı çip lang:tr" or "biyolojik silah koronavirüs" or "biyolojik silah covid-19"
#This solely found plandemic tweets/changing "or" with "and" gives no results
#c.Search = "plandemi or plandemic or bill gates covid-19  or great reset  or aşı 5G  or bill gates çip  or salgın yalanı or maske yalanı  or bill gates aşı or büyük sıfırlama  or yeni dünya düzeni  or aşı mikroçip or aşı çip  or biyolojik silah koronavirüs or biyolojik silah covid-19 lang:tr"
#This gave an error
#keywords= ["plandemi lang:tr","plandemic lang:tr","bill gates covid-19 lang:tr","great reset lang:tr","aşı 5G lang:tr","bill gates çip lang:tr","salgın yalanı lang:tr","maske yalanı lang:tr","bill gates aşı lang:tr","büyük sıfırlama lang:tr","yeni dünya düzeni lang:tr", "aşı mikroçip lang:tr","aşı çip lang:tr", "yapay virüs lang:tr","biyolojik silah covid-19"]
#c.Search = keywords
#found no tweets
#keywords= ["plandemi ","plandemic","bill gates covid-19","great reset ","aşı 5G","bill gates çip ","salgın yalanı","maske yalanı","bill gates aşı","büyük sıfırlama","yeni dünya düzeni", "aşı mikroçip","aşı çip ", "yapay virüs","biyolojik silah covid-19"]
c = twint.Config()
#c.Search = "plandemi lang:tr"
#c.Search = "plandemic lang:tr"
#c.Search = "bill gates covid-19 lang:tr"
#c.Search = "great reset lang:tr"
#c.Search = "aşı 5G lang:tr"
#c.Search = "bill gates çip lang:tr"
#c.Search = "salgın yalanı lang:tr"
#c.Search = "maske yalanı lang:tr"
#c.Search = "bill gates aşı lang:tr"
#c.Search = "büyük sıfırlama lang:tr"
#c.Search = "yeni dünya düzeni lang:tr"
#c.Search = "aşı mikroçip lang:tr"
#c.Search = "aşı çip lang:tr"
#c.Search = "yapay virüs lang:tr"
#c.Search = "biyolojik silah covid-19"
#c.Search = "biyolojik silah covid-19"
keywords= ["plandemi ","plandemic","bill gates covid-19","great reset ","aşı 5G","bill gates çip ","salgın yalanı","maske yalanı","bill gates aşı","büyük sıfırlama","yeni dünya düzeni", "aşı mikroçip","aşı çip ", "yapay virüs","biyolojik silah covid-19"]
c.Search = keywords
c.Lang = tr
c.Since = "2020-03-11 00:00:01"
c.Until = "2021-05-15 23:59:59"
c.Store_csv = True
c.Output ="C:/Users/Bulut/Desktop/R Course/INTL 550/covidconspiracyturkeyfinaaaaaaaaaaaaaaaaaaal.csv" #save csv
c.Resume = "convidfinallveaaaaaaaaaaaaaaaaaaa.txt" #resumption text which I changed for each variable because of connection loss.
twint.run.Search(c)
