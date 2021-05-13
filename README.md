# India COVID-19 Test Positivity Data

This project parses and archives daily district level COVID-19 test positivity data for India (downloaded from the [Ministry of Health](https://www.mohfw.gov.in/) webpage).

The government data consists of daily Excel files listing the test positivity rate for Indian districts reporting a positivity rate ≥ 10%.

This repository automatically runs a script to fetch the daily data update, parses the data into a CSV file, and archives the Excel file.

- The [archive](https://github.com/aatishb/indiatestpositivitydata/tree/main/archive) folder contains archives of each day's xlsx file released by the government
- [data.csv](https://github.com/aatishb/indiatestpositivitydata/blob/main/data.csv) contains the time-series data in CSV format. The date is in ISO format i.e. `YYYY-MM-DD`

## Manual Data Updates

The following steps were taken to clean the daily data in [data.csv](https://github.com/aatishb/indiatestpositivitydata/blob/main/data.csv)

- 2021-05-13: Renamed misnamed state 'A' to 'Tamil Nadu'
