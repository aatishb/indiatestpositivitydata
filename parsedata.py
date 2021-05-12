# script to parse COVID test positivity data from https://www.mohfw.gov.in/
# the data is appended to data.csv and archived in the archive folder

import pandas as pd
from datetime import datetime
import pytz
import urllib.request

# get current date in IST
IST = pytz.timezone('Asia/Kolkata')
today = datetime.now(IST)
# https://stackoverflow.com/a/20007730
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])
monthname = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
date = ordinal(today.day) + monthname[today.month - 1]

# parse URL for that date
print('checking for new data on', today)
url = 'https://www.mohfw.gov.in/pdf/10percentDistrictWiseCOVID19Positivity' + date + '.xlsx'
df = pd.read_excel(url, skiprows=[0,1,2], header=[0]).fillna(method='ffill')
df.drop(df.tail(1).index,inplace=True)
currentdate = today.strftime('%d/%m/%Y')
df['Date'] = currentdate

csv = pd.read_csv('data.csv', header=None)
prevdate = csv.iloc[-1,0]

if (prevdate != currentdate):
    df.to_csv("data.csv", columns = ['Date', 'State', 'District', 'Positivity'], header = False, index = False, mode='a')
    print('added data for', currentdate, 'to data.csv')
    path = '/archive' + url.split('/')[-1]
    urllib.request.urlretrieve(url, path)
    print('saved data for', currentdate, 'to archive folder')
    
else:
    print('already have data for', currentdate)