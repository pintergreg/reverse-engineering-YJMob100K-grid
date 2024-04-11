# Reverse-engineering the observation area of the 'YJMob100K' data

## Usage

The [`pyproject.toml`](pyproject.toml) document the required dependencies. It's suggested to use the [Poetry](https://python-poetry.org/) packaging tool. In this case, just issue the `poetry install` command to set up a virtual environment with all the necessary dependencies.

After the development environment has set up, run the notebooks in the following order to reproduce the results.

1. [plot_heatmaps.ipynb](src/plot_heatmaps.ipynb)
    - this will reproduce the heatmaps [Figure 6] from the [data description paper](https://arxiv.org/abs/2307.03401),
    - do the inverse-transformed plots, and
    - some related plots for the paper
2. [generate_grid.ipnyb](src/generate_grid.ipynb)
   - this will locate the observation area within Japan and generate the grid

These two notebooks contain the main work. The [detect_homes.ipynb](src/detect_homes.ipynb), [validate_home_detection.ipynb](src/validate_home_detection.ipynb) and the [calculate_grid_complexity.ipynb](src/calculate_grid_complexity.ipynb) are optional steps to reproduce the figure in the technical validation section of the paper.

## Results

The results are included to be available without executing the code.
Most notably, the [reproduced grid](output/grid_bl_2449.geojson).

<!-- ## Citation

Use the following BibTeX entry to cite the paper.

<details>
  <summary>BibTeX</summary>
  <pre>

  </pre>
</details>

The code can be cited via [GitHub](https://github.com/pintergreg/reverse-engineering-YJMob100K-grid). -->

## Data sources

1. Mobility data: [YJMob100K](https://zenodo.org/records/10836269)
    - [details](data/yjmob100k/README.md) about how to prepare it
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

## License

- The code is licensed under [BSD-3-Clause](LICENSE)
- The documentation and figures are [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- The shape files are from OpenStreetMap and licensed under the Open Data Commons Open Database License ([ODbL](https://opendatacommons.org/licenses/odbl/1-0/))
- The census data was downloaded from the Portal Site of Official Statistics of Japan website (https://www.e-stat.go.jp/)
