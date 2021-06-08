from pytrends.request import TrendReq
from pytrends import dailydata
import pandas as pd
#ran keywords separately as giving a payload gave an 400 error
ao1 =dailydata.get_daily_data("Vaccine 5G", 2020, 3, 2021, 5, geo="",)
ao2 =dailydata.get_daily_data("plandemic", 2020, 3, 2021, 5, geo="",)
ao3 =dailydata.get_daily_data("anti mask", 2020, 3, 2021, 5, geo="",)
ao4 =dailydata.get_daily_data("Great Reset", 2020, 3, 2021, 5, geo="",)
ao5 =dailydata.get_daily_data("Bill Gates Vaccine", 2020, 3, 2021, 5, geo="",)
#saved all of them under a single csv file
ao = pd.concat([ao1,ao2,ao3,ao4,ao5], axis = 1)
ao.to_csv('jay.csv', sep=',',index=False)
