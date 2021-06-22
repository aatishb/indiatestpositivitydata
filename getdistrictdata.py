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
date1 = ordinal(today.day) + monthname[today.month - 1]
date2 = str(today.day) + monthname[today.month - 1].lower()
currentdate = str(today.date())

csv = pd.read_csv('districtdata.csv', header=0)
prevdate = csv.iloc[-1,0]

if (prevdate != currentdate):
    for date in [date1, date2, 'district' + date2]:
        url = 'https://www.mohfw.gov.in/pdf/COVID19DistrictWisePositivityAnalysis' + date + '.xlsx'
        try:
            df = pd.read_excel(url, engine = 'openpyxl')
            print('accessed url: ', url)

            # find first row of data and header row
            firstrow = df[df.isin(['ANDAMAN AND NICOBAR ISLANDS']).any(axis=1)].index[0]
            headerrow = firstrow - 1

            # set header to header row
            df.columns = df.iloc[headerrow]
            # start data from first row of data
            df = df[df.index >= firstrow]

            # rename duplicate columns
            columns = []
            count = {}
            for c in df.columns:
                if c in columns:
                    columns.append(c + '.' + str(count[c]))
                    count[c] += 1
                else:    
                    columns.append(c)
                    count[c] = 1;

            df.columns = columns

            over10percent = df[['State','District', 'Positivity']].dropna(thresh=1).iloc[:-1 , :].fillna(method='ffill')
            over10percent['Positivity'] = over10percent['Positivity']/100
            
            between5and10percent = df[['State.1','District.1', 'Positivity.1']].dropna(thresh=1).iloc[:-1 , :].fillna(method='ffill').rename(columns={"State.1": "State", "District.1": "District", "Positivity.1": "Positivity"})
            between5and10percent['Positivity'] = between5and10percent['Positivity']/100
            
            under5percent = df[['State.2','District.2', 'Positivity.2']].dropna(thresh=1).iloc[:-1 , :].fillna(method='ffill').rename(columns={"State.2": "State", "District.2": "District", "Positivity.2": "Positivity"})
            under5percent['Positivity'] = under5percent['Positivity']/100
            
            output = pd.concat([over10percent, between5and10percent, under5percent]).sort_values(by=['State', 'District']).rename(columns = {'Positivity': 'Test Positivity Rate'})
            output['Date'] = currentdate
            output.to_csv("districtdata.csv", columns = ['Date', 'State', 'District', 'Test Positivity Rate'], header = False, index = False, mode='a')
            print('added district data for', currentdate, 'to districtdata.csv')

            path = 'archive/' + url.split('/')[-1]
            request.urlretrieve(url, path)
            print('saved district data for', currentdate, 'to archive folder')

        except HTTPError as err:
            if err.code == 404:
                    print('404 error: ', url)
            else:
                print(err)
    
else:
    print('already have district data for', currentdate)
