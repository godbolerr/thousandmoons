import requests
import pandas as pd
import time

dflist = []

for count in range(1900, 2001):
    
    api_url = "https://aa.usno.navy.mil/api/moon/phases/year?year=" + str(count)
    
    print(api_url)
    
    response = requests.get(api_url)
    
    json = response.json()
    
    df = pd.DataFrame(json['phasedata'])
    
    dflist.append(df)
    
    time.sleep(2)
    
alldf = pd.concat(dflist)
    
alldf.to_csv(r'phaseData1900_2001.csv')

