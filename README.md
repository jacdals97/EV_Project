# EV Project

## Description

We present a collection of datasets encompassing several dimensions linked to electric vehicles (EVs) including interest, EV charging infrastructure, purchases of EVs and relevant regional demographics. At an aggregate level we present a long format dataset that allows for temporal and spatial analysis  at the resolution of city, municipality and region across Denmark. The data is acquired through Google Trends, Facebook Marketing, PlugShare and Danmarks Statistik. The acquisitions are achieved by either web scraping, API calls, downloading of open data or manual annotation. Each data source produces a raw dataset from which the aggregated dataset is built. As such we present an additional 3-4 datasets including a 5 year weekly time series on Google Trends data from 319 Danish cities, a dataset documenting the Danish EV charging infrastructure and a proof of concept dataset on EV consumer audience sizes in Danish cities and municipalities. The entire collection of datasets allows for various hypotheses to be tested regarding electric vehicles.

## Project Organization
The organization of the project is as follows:

```
├── EVDK.csv
├── EVDK_2021.csv
├── data_combining.ipynb
├── README.md
├── Danmarks_Statistik
│   ├── 2021102813564349600816BIL710.xlsx
│   ├── DST_pop.xlsx
│   └── DST_wrangling.Rmd
├── Datasets
│   ├── aggregated
│   │   ├── FB_estimates.csv
│   │   ├── ev_population.csv
│   │   ├── muni_aggr_charging_data.csv
│   │   ├── population_stats.csv
│   │   └── preproccesed_trends_data.csv
│   └── src
│       ├── charging_stations.csv
│       └── trends_data.csv
├── chargers
│   ├── backup.pickle
│   ├── charger_links.csv
│   ├── charger_links_generation.ipynb
│   ├── charger_scraper.py
│   ├── charging_stations
│   ├── meters.pickle
│   ├── raw_data
│   ├── stander_data_generation.ipynb
│   └── standers.pickle
├── facebook
│   ├── City_id_and_name.txt
│   ├── FB_estimates.csv
│   ├── FB_estimates_121221.txt
│   ├── get_FB_estimates.ipynb
│   └── paramters_for_deliveryestimate_v3.npy
├── helpers
│   ├── FB_with_no_Municipality.csv
│   ├── FB_with_no_Municipality_done.csv
│   ├── Regions_and_Municipalities
│   │   ├── Municipalities.csv
│   │   └── Regions_and_municipalities.csv
│   ├── cities_for_manual_inspection.csv
│   ├── cities_for_manual_inspection_done.csv
│   ├── cities_in_multiple_municipalities.csv
│   ├── cities_in_multiple_municipalities_done.csv
│   ├── cities_missing_municipality.csv
│   └── cities_missing_municipality_done.csv
└── trends
    ├── Stable_trends
    │   ├── Stable_trends_timeseries.ipynb
    │   ├── figs
    │   └── stable_topics.csv
    ├── get_trends.ipynb
    ├── sports_trends_f.csv
    └── trends_preprocessing.ipynb
```
The following is a chart visualising the different levels of aggregating and summarisation of the dataset. Each cylinder is a .pickle, .csv or otherwise structured dataset.

<img width="612" alt="Screenshot 2021-12-16 at 14 33 20" src="https://user-images.githubusercontent.com/25800085/146381446-023d05ea-f1d8-47e8-b3ad-154ee1df66a2.png">

## Data availability
The data is also available at https://www.kaggle.com/askebredahlnielsen/electric-vehicles-in-denmark?fbclid=IwAR0-H8-BF_aD3lw_tTwCoMBplwYqCvb6Nl-bklifs92yQGCS8h_3cTFlYfM
