## India District-Level COVID-19 Test Positivity Data

This repository parses & archives COVID-19 test positivity percent for Indian districts and states. The test positivity is the fraction of Covid tests that are positive.

From 10th May onwards, the [Indian Ministry of Health](https://www.mohfw.gov.in/) has been uploading a daily Excel file that reports the 6-day average COVID-19 test positivity for Indian districts with a test positivity ≥ 10%. From 26th May onwards, this data set has been expanded to include data from all districts.

This repository automatically fetches the daily government data update, parses the data and appends it to a CSV file, and archives the government data file.

We also calculate the test positivity for Indian states & union territories using data collected by [covid19india.org](https://github.com/covid19india/api) as follows: `test positivity (7 day average) = new confirmed cases in the past week / tests conducted in the past week`. Note that there may be some discrepancies between states depending on whether they report the number of samples tested or the number of people tested.

## Data Files

- The [archive](https://github.com/aatishb/indiatestpositivitydata/tree/main/archive) folder contains an archive of the daily government Excel files with test positivity data for districts
- [districtdata.csv](https://github.com/aatishb/indiatestpositivitydata/blob/main/districtdata.csv) contains time-series test positivity data for districts
- [statedata.csv](https://github.com/aatishb/indiatestpositivitydata/blob/main/statedata.csv) contains time-series test positivity data, weekly confirmed cases, and weekly tests for states & union territories

The date is in ISO format i.e. `YYYY-MM-DD`. Test positivity is calculated as a 1 week average for the 7 days prior to the date on which the data is reported. For example, the test positivity reported on June 8 is calculated from the new cases and new tests on June 1 through June 7.

## Data Sources
- District Data: [Indian Ministry of Health](https://www.mohfw.gov.in/)
- State Data: [covid19india.org](https://api.covid19india.org/)
 
## Manual Data Updates

The following steps were taken to clean the daily data in [districtdata.csv](https://github.com/aatishb/indiatestpositivitydata/blob/main/districtdata.csv)

- 2021-05-13: Renamed misnamed state 'A' to 'Tamil Nadu'

## Known Data Issues & Format Changes

Prior to May 26th, the Ministry of Health only included data from districts with test positivity >= 10%, and did not include district-level data for Telangana.

- May 26th: source data format changed (includes data from almost all districts)
- May 27th: source data format changed (added columns for % of testing by RT-PCR and Rapid Antigen)
- May 29th: souce data format changed (added rows of summary text on top)
