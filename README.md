# India COVID-19 Test Positivity Data

This project parses and archives district level test COVID-19 positivity data for India from https://www.mohfw.gov.in/

The government data includes districts reporting a COVID-19 test positivity rate ≥ 10%

This script runs every 4 hours to check for & fetch a daily data update.

- The [archive](https://github.com/aatishb/indiatestpositivitydata/tree/main/archive) folder contains archives of each day's xlsx file released by the government
- [data.csv](https://github.com/aatishb/indiatestpositivitydata/blob/main/data.csv) contains the time-series data in CSV format. The date is in ISO format i.e. `YYYY-MM-DD`

## Manual Data Updates

The following steps were taken to clean the daily data in [data.csv](https://github.com/aatishb/indiatestpositivitydata/blob/main/data.csv)

- 2021-05-13: Renamed misnamed state 'A' to 'Tamil Nadu'
