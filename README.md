# Reverse-engineering the spatial dimension of the 'YJMob100K' data

## Data sources

1. Mobility data: [YJMob100K](https://zenodo.org/records/10836269)
    - [details](data/README.md) about how to prepare it
2. OpenStreetMap data
    - Copyrighted by OpenStreetMap contributors. It is available under the Open Database License (ODbL).
    - Administrative data is from OpenStreetMap
        - downloaded from [OSM-Boundaries](https://osm-boundaries.com/)
            - prefectures (admin level 4), then filtered manually
            - municipalities (admin level 7), then filtered manually
            - wards (admin level 8), then filtered to Nagoya
    - Coastline is downloaded from https://osmdata.openstreetmap.de/data/land-polygons.html
        - the islands of Japan was extracted using the prefecture boundaries
4. Census data
    - The [Population Census 2020, Population, Households, Sex, Age and Marital status, Table 1-1](https://www.e-stat.go.jp/en/stat-search/files?page=1&layout=datalist&toukei=00200521&tstat=000001136464&cycle=0&year=20200&month=24101210&tclass1=000001136466) was downloaded from the 
     Portal Site of Official Statistics of Japan website (https://www.e-stat.go.jp/)
