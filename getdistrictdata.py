# script to parse India district level COVID test positivity data from https://www.mohfw.gov.in/
# the data is appended to districtdata.csv and archived in the archive folder

import pandas as pd
from datetime import datetime
import pytz
from urllib import request
from urllib.error import HTTPError

# get current date in IST
IST = pytz.timezone('Asia/Kolkata')
today = datetime.now(IST)
print('checking for new district data on', today)

# https://stackoverflow.com/a/20007730
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

monthname = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
date = ordinal(today.day) + monthname[today.month - 1]
currentdate = str(today.date())

try:
    url = 'https://www.mohfw.gov.in/pdf/COVID19DistrictWisePositivityAnalysis' + date + '.xlsx'
    df = pd.read_excel(url, engine = 'openpyxl', skiprows=[0,1,2,3], header=[0])
    over10percent = df[['State','District', 'Positivity']].dropna(thresh=1).iloc[:-1 , :].fillna(method='ffill')
    between5and10percent = df[['State.1','District.1', 'Positivity.1']].dropna(thresh=1).iloc[:-1 , :].fillna(method='ffill').rename(columns={"State.1": "State", "District.1": "District", "Positivity.1": "Positivity"})
    under5percent = df[['State.2','District.2', 'Positivity.2']].dropna(thresh=1).iloc[:-1 , :].fillna(method='ffill').rename(columns={"State.2": "State", "District.2": "District", "Positivity.2": "Positivity"})
    output = pd.concat([over10percent, between5and10percent, under5percent]).sort_values(by=['State', 'District']).rename(columns = {'Positivity': 'Test Positivity Rate'})
    output['Date'] = currentdate
    
    csv = pd.read_csv('districtdata.csv', header=0)
    prevdate = csv.iloc[-1,0]

    if (prevdate != currentdate):
        output.to_csv("districtdata.csv", columns = ['Date', 'State', 'District', 'Test Positivity Rate'], header = False, index = False, mode='a')
        print('added district data for', currentdate, 'to districtdata.csv')
        path = 'archive/' + url.split('/')[-1]
        request.urlretrieve(url, path)
        print('saved district data for', currentdate, 'to archive folder')

    else:
        print('already have district data for', currentdate)
        
except HTTPError as err:
    if err.code == 404:
            print('district data has not yet been updated for', currentdate)
    else:
        print(err)
