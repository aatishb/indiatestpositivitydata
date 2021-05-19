## India COVID-19 Test Positivity Data
### This repository parses & archives daily district-level COVID-19 Test Positivity Rates for India.

The **COVID-19 Test Positivity Rate** is the share of COVID-19 tests that are positive.

From 10th May onwards, the [Indian Ministry of Health](https://www.mohfw.gov.in/) has been uploading a daily Excel file reporting a 6-day average COVID-19 test positivity rate (for districts with a test positivity rate ≥ 10%). These Excel files are only available for a day and are not archived by the government.

This GitHub  repository automatically runs a script to fetch the daily government data update, parses and appends the data to a CSV file, and archives the Excel file. This allows you to analyze this data as a time-series.

We also calculate the state test positivity rates from the case & test numbers collected by [covid19india.org](https://github.com/covid19india/api). The state-level test positivity rate is computed as follows: `test positivity rate (7 day average) = new confirmed cases in the past week / tests conducted in the past week`. Note that there may be some discrepancies between states depending on whether they report the number of samples tested or the number of people tested.

## Data Files

- The [archive](https://github.com/aatishb/indiatestpositivitydata/tree/main/archive) folder contains archives of each day's xlsx file released by the government
- [districtdata.csv](https://github.com/aatishb/indiatestpositivitydata/blob/main/districtdata.csv) contains time-series test positivity data for districts.
- [statedata.csv](https://github.com/aatishb/indiatestpositivitydata/blob/main/statedata.csv) contains time-series test positivity data, weekly confirmed cases, and weekly tests for states & union territories.

The date is in ISO format i.e. `YYYY-MM-DD`. District-level data is for the 6 day period not including the date on which the data is reported, while state-level data is for the 7 day period including the date on which the data is reported.

## Data Sources
- District Data: [Indian Ministry of Health](https://www.mohfw.gov.in/)
- State Data: [covid19india.org](https://github.com/covid19india/api) (manually collected from state health ministries)
 
## Manual Data Updates

The following steps were taken to clean the daily data in [districtdata.csv](https://github.com/aatishb/indiatestpositivitydata/blob/main/data.csv)

- 2021-05-13: Renamed misnamed state 'A' to 'Tamil Nadu'

## Known Data Issues

The Ministry of Health data does not currently include district-level data for Telangana. This data can be found on the Telangana Department of Health [Media Bulletins](https://covid19.telangana.gov.in/announcements/media-bulletins/).
