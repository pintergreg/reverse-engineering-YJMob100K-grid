# YJMob100K: City-Scale and Longitudinal Dataset of Anonymized Human Mobility Trajectories

## Download

Assuming linux and available curl:

1. `curl -O "https://zenodo.org/records/10142719/files/yjmob100k-dataset1.csv.gz?download=1"`
2. `curl -O "https://zenodo.org/records/10142719/files/yjmob100k-dataset2.csv.gz?download=1"`
3. `curl -O "https://zenodo.org/records/10142719/files/cell_POIcat.csv.gz?download=1"`

Note that use at least version 2 (https://zenodo.org/records/10142719), as version 1 was used for the challenge and is restricted. Version 3 (https://zenodo.org/records/10836269) added dictionary for the POIs.

## Extract

Assuming linux and available gzip:

1. `gzip -d yjmob100k-dataset1.csv.gz`
2. `gzip -d yjmob100k-dataset2.csv.gz`
3. `gzip -d cell_POIcat.csv.gz`

## Description from Zenodo

The YJMob100K human mobility datasets (YJMob100K_dataset1.csv.gz and YJMob100K_dataset1.csv.gz) contain the movement of a total of 100,000 individuals across a 75 day period, discretized into 30-minute intervals and 500 meter grid cells. The first dataset contains the movement of 80,000 individuals across a 75-day business-as-usual period, while the second dataset contains the movement of 20,000 individuals across a 75-day period (including the last 15 days during an emergency) with unusual behavior.

While the name or location of the city is not disclosed, the participants are provided with points-of-interest (POIs; e.g., restaurants, parks) data for each grid cell (~85 dimensional vector) as supplementary information (cell_POIcat.csv.gz).

For details of the dataset, see arXiv preprint https://arxiv.org/abs/2307.03401

Researchers may use this dataset for publications and reports, as long as: 1) Users shall not carry out activities that involve unethical usage of the data, including attempts at re-identifying data subjects, harming individuals, or damaging companies, and 2) The Data Descriptor paper (https://arxiv.org/abs/2307.03401; citation below) needs to be cited when using the data for research and/or commercial purposes. Downloading this dataset implies agreement with the above two conditions.

> Yabe, T., Tsubouchi, K., Shimizu, T., Sekimoto, Y., Sezaki, K., Moro, E., & Pentland, A. (2023). Metropolitan scale and longitudinal dataset of anonymized human mobility trajectories. arXiv preprint arXiv:2307.03401. https://arxiv.org/abs/2307.03401
