## India COVID-19 Test Positivity Rate

This repository parses & archives daily district-level COVID-19 test positivity rates for India. The test positivity rate is the share of Covid tests that are positive.

From 10th May onwards, the [Indian Ministry of Health](https://www.mohfw.gov.in/) has been uploading a daily Excel file that reports the 6-day average COVID-19 test positivity rate (for Indian districts with a test positivity rate ≥ 10%).

This repository automatically fetches the daily government data update, parses the data and appends it to a CSV file, and archives the government data file.

We also calculate the test positivity rates for Indian states & union territories using data collected by [covid19india.org](https://github.com/covid19india/api). The positivity rate is calculated as follows: `test positivity rate (7 day average) = new confirmed cases in the past week / tests conducted in the past week`. Note that there may be some discrepancies between states depending on whether they report the number of samples tested or the number of people tested.

## Data Files

- The [archive](https://github.com/aatishb/indiatestpositivitydata/tree/main/archive) folder contains an archive of the daily government Excel files with test positivity data for districts
- [districtdata.csv](https://github.com/aatishb/indiatestpositivitydata/blob/main/districtdata.csv) contains time-series test positivity data for districts
- [statedata.csv](https://github.com/aatishb/indiatestpositivitydata/blob/main/statedata.csv) contains time-series test positivity data, weekly confirmed cases, and weekly tests for states & union territories

The date is in ISO format i.e. `YYYY-MM-DD`. District-level data is for the 6 day period preceding the date on which the data is reported, while state-level data is for the 7 day period including the date on which the data is reported.

## Data Sources
- District Data: [Indian Ministry of Health](https://www.mohfw.gov.in/)
- State Data: [covid19india.org](https://github.com/covid19india/api) (collected from state health ministries by volunteers)
 
## Manual Data Updates

The following steps were taken to clean the daily data in [districtdata.csv](https://github.com/aatishb/indiatestpositivitydata/blob/main/data.csv)

- 2021-05-13: Renamed misnamed state 'A' to 'Tamil Nadu'

## Known Data Issues

The Ministry of Health data does not currently include district-level data for Telangana. This data can be found on the Telangana Department of Health [Media Bulletins](https://covid19.telangana.gov.in/announcements/media-bulletins/).
