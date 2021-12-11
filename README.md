# Quantitative Clustering and Classification study of Urban Functional Area
NYU Shanghai CSCI-SHU 360 Machine Learning project: by Alan, Ella and Steven. 

## Datasets
### Town level
* [Block.csv](Block.csv) : Before training, merged 点评, POI, Housing Price, town level.
* [拟合结果带街道.csv](拟合结果带街道.csv) : Used K-means and Gaussian Mixture to cluster towns. [Result visualization](#).
* [上海街道](/上海街道): Raw shapefiles of Town level Shanghai map.
* [采集结果](/采集结果): Raw data scrapped from 点评.
* [housing_f_t.xlsx](housing_f_t.xlsx): Raw data of housing price connect with town level and fishnet level.
### Fishnet level
* [POI_fishnet_steven.xlsx](POI_fishnet_steven.xlsx): POI values, calculated each fishnet cell.
* [poi_fishnet.xlsx](poi_fishnet.xlsx): similar to previous one.
* [fishnet4900_shanghai.shp](fishnet4900_shanghai.shp): Shapefile of fishnet.
* [POI_Fishnet_for_training.xls](POI_Fishnet_for_training.xls): Early clustering training dataset. 
* [fishnet_centroid.xlsx](fishnet_centroid.xlsx): Fishnet centroid positions.
* [fishnet_density.csv](fishnet_density.csv): Training attributes: 点评,POI,Housing mapped to each fishnet
* [poi_pure.csv](poi_pure.csv): Pure POI coordinates
* [poi.csv](poi.csv): POI coordinates and attribute values
* [housing_kriging.xlsx](housing_kriging.xlsx): Housing data fishnet, with Kriging interpol.
### Fishnet normalized
* [normalized_fishnet_town.csv](normalized_fishnet_town.csv): Early try of normalizing fishnet density
* [norm_f_town_district.csv](norm_f_town_district.csv): normalized data.

* [POI_Fishnet_for_training.csv](POI_Fishnet_for_training.csv): Training dataset that consists of 3 columns.

|k_index|POI_normalize|commercial_price|Ground_truth_label|housing_price        |
|-------|-------------|----------------|------------------|---------------------|
|1846|-0.456332229|-0.232740344|2  |2.2294739887415953   |
|1847|-0.446541948|-0.03508537|2  |1.1101016907979073   |
|1848|-0.285135448|-0.020974646|2  |1.157380772499592    |
|1849|0.51669039  |-0.092973206|2  |0.02686459639227951  |
|1850|0.782230116 |-0.171101576|2  |0.02686459639227951  |
|1851|-0.181002222|0.274272878|2  |0.02686459639227951  |
|1852|-0.25389548 |0.494809612|2  |1.157380772499592    |
|1853|0.084537503 |0          |2  |1.8267865167539685   |
|1854|0.027264229 |0.50115112 |2  |0.16032218247970148  |
|1855|-0.358028706|-0.225356818|2  |0.16032218247970148  |
|1856|-0.37364869 |-0.567579648|2  |0.4922316729195175   |
|1857|-0.045629029|0          |2  |1.2664371518217568   |


### Plots
* POI data, without normalization       
![POI data, without normalization](plots/poi_weight.png)
* POI data, normalized at district level
![POI data, normalized at district level](plots/norm_poi_district.png)
* POI data, normalized at town level
![POI data, normalized at town level](plots/norm_poi_town.png)
* Housing data, without normalization       
![Housing data, without normalize](plots/without_house.png)
* Housing data, normalized at district level
![Housing data, normalized at district level](plots/norm_house_district.png)
* Housing data, normalized at town level
![Housing data, normalized at town level](plots/norm_house_town.png)
## Code
* [dianping-scrapper.py](dianping-scrapper.py): 点评scrapping code.
* [alt.py](alt.py): same as above.
* [cookie.txt](cookie.txt): Cookie generated during scrapping
* [K_Means_街道.ipynb](K_Means_街道.ipynb): Training code. Town level, clustering.
* [poi_dp_house_pop_fish.ipynb](poi_dp_house_pop_fish.ipynb): Training code. Fishnet level, clustering.
* [poi_density_housing_normalize.ipynb](poi_density_housing_normalize.ipynb): Data processing code. Normalizing fishnet data. 
* [Density_POI.ipynb](Density_POI.ipynb): Pure POI data visualization. 

## Training Models
### 1. Town level, clustering, without normalize
* K-means: having k = 6.         
![kmeans 6 town](plots/town_km6.png)


* Gaussian Mixture: having k = 6. 
![kmeans 6 town](plots/town_gm6.png)

### 2. Fishnet level, classification models

* Ground truth                              
![gt](plots/ground_truth_label.png)

* K Nearest Neighbor                        
![knn](plots/KNN.png)

* Adaboost                          
![knn](plots/adaboost.png)

* Decision Tree                         
![dt](plots/decision_tree.png)

* Random Forest                             
![rf](plots/randomforest.png)

### 3. Fishnet level, clustering, without normalize
* K means: having k = 6                   
![kmeans 6 fishnet](plots/km6_fishnet.png)

* Gaussian Mixture: having k = 6          
![kmeans 6 fishnet](plots/gm6_fishnet.png)

* DBSCAN                                            
![dbscan_fishnet_eps0.2_min2](plots/dbscan_fishnet_eps0.2_min2.png)
![dbscan_fishnet_eps1_min10.png](plots/dbscan_fishnet_eps1_min10.png)

### 4. Fishnet level, clustering, with normalized data.

* K means: having k = 7                                
![kmeans 6 normalized](plots/km7_normalized.png)

* Gaussian Mixture: having k = 7                     
![kmeans 6 normalized](plots/gm7_normalized.png)

* DBSCAN                                             
![dbscan](plots/dbscan_normalized.png)
![dbscan1](plots/dbscan_normalized_1.png)

