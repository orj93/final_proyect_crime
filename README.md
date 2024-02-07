Analysis of Los Angeles crime gangs by machine learning models.  

In this project different crimes in LA area are analyzed in order to group them in different profiles with the goal of predicting possible criminals in the future.  

For correctly running this code requirements.txt libraries are needed.  

This repository contains a 'src' file where we can find:  

1. Data load from the SODA api. URL: https://data.lacity.org/Public-Safety/Crime-Data-from-2020-to-Present/2nrs-mtv8/data_preview  
    
2. SQL query selecting the last 4 years crimes (since 2020)  
    
3. Statistical analysis  
    
4. Exploratory data analysis  
    
5. Model creation based upon 5 different crimes  
    
6. An streamlit deploynent python script  
    
Besides the src this repository also contains a 'data' which was not uploaded to github due to its large memory and a 'models' file with the five different models obtained in it
For the model developpment we have created 10 groups of LA gangs/profiles (k=10) according to some variables like area, geographic coordinates, descent, sex and age of the victim, then considering the data of future crimes we could predict to what profile the gang/criminal belongs.  


This project is deployed on render. URL: https://la-crime-analysis-oqan.onrender.com
This project is deployed on [here](https://la-crime-analysis-oqan.onrender.com)
