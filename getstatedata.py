# script to calculate India state level test positivity data
# state case data https://api.covid19india.org/csv/latest/states.csv
# state testing data https://api.covid19india.org/csv/latest/statewise_tested_numbers_data.csv
# the data is output to statedata.csv

import pandas as pd
from datetime import date, datetime, timedelta
import pytz
from urllib.error import HTTPError

# https://www.w3resource.com/python-exercises/date-time-exercise/python-date-time-exercise-50.php
def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

states = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'India', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal']

IST = pytz.timezone('Asia/Kolkata')
today = datetime.now(IST)
print('checking for new state data on', today)

try:
  cases = pd.read_csv('https://api.covid19india.org/csv/latest/states.csv')
  cases.index = pd.to_datetime(cases['Date'], dayfirst = True)

  tests = pd.read_csv('https://api.covid19india.org/csv/latest/statewise_tested_numbers_data.csv')
  tests.index = pd.to_datetime(tests['Updated On'], dayfirst = True)

  df = pd.DataFrame(columns = ['Date' , 'State', 'Weekly Cases' , 'Weekly Tests', 'Test Positivity Rate'])

  for dt in daterange(date(2021, 4, 1), today.date()):
      for state in states:

          datestring = dt.strftime("%Y-%m-%d")
          
          statecases = cases[cases['State'] == state]['Confirmed']
          stateweeklycases = statecases - statecases.shift(7)

          statetests = tests[tests['State'] == state]['Total Tested']
          stateweeklytests = statetests - statetests.shift(7)

          currentstateweeklycases = stateweeklycases[stateweeklycases.index == datestring]
          currentstateweeklytests = stateweeklytests[stateweeklytests.index == datestring]

          if (currentstateweeklycases.size == 1 and currentstateweeklytests.size == 1):
              if (currentstateweeklycases.iloc[0] > 0 and currentstateweeklytests.iloc[0] > 0):
                  df = df.append({'Date': datestring,
                             'State': state,
                             'Weekly Cases': round(currentstateweeklycases.iloc[0]),
                             'Weekly Tests': round(currentstateweeklytests.iloc[0]),
                             'Test Positivity Rate': round(currentstateweeklycases.iloc[0] / currentstateweeklytests.iloc[0],3)
                            }, ignore_index=True)

  df.to_csv("statedata.csv", columns = ['Date', 'State', 'Weekly Cases', 'Weekly Tests', 'Test Positivity Rate'], header = True, index = False)
  print('output state data to file')

except HTTPError as err:
    print(err)
