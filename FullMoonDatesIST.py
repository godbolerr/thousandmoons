import pandas as pd
import csv

from datetime import datetime
from dateutil import relativedelta
from _datetime import timedelta
from itertools import count


df = pd.read_csv('../FullMoonDates1900_2100.csv') 

fullmoondates = []

for row in df.itertuples(name="FullMoon" ):
    
   fullmoondate = row[1]
   newDate = datetime.strptime(fullmoondate, '%d-%m-%Y %H:%M')
   newrefDate = newDate + timedelta(hours=5) 
   newrefDate = newrefDate + timedelta(minutes=30) 
   fullmoondates.append(newrefDate)
   
   
fdf = pd.DataFrame(fullmoondates)

fdf.to_csv('../IST_FullMoonDates1900_2100.csv', index=False)