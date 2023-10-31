# Image Search

## Project Description
Users upload their photos to the hosting service and accompany them with detailed descriptions: they specify the shooting location, camera model, and so on. The distinctive feature of the service is the description: it can be provided not only by the person who uploads the photo but also by other users of the portal. The essence of the search is as follows: a user of the service enters a description of the desired scene. The service displays several photos with the same or similar scene.

## Skills and Tools
* pandas
* numpy
* os
* math
* collections.Counter
* torchvision.models
* torchvision.transforms
* torch.nn
* matplotlib.pyplot
* tqdm.auto.tqdm
* PIL.Image
* nltk
* time
* random
* stopwords
* GroupShuffleSplit
* TfidfVectorizer
* mean_squared_error
* torch
* random
* LinearRegression
* Ridge
* CatBoostRegressor
* RandomForestRegressor
* WordNetLemmatizer
* scipy
* re
* seaborn as sns

## General Conclusion

* Boosting (CatBoostRegressor): RMSE: 0.11422264868523815, Execution Time: 412.53947710990906 sec
* Random Forest Regressor: RMSE: 0.12220017624756276, Execution Time: 154.18005514144897 sec
* Boosting (CatBoostRegressor) showed the best result with the lowest RMSE value
* Random Forest Regressor also demonstrated a good result, close to boosting.
* Linear regression and Ridge regression show higher RMSE values
* The neural network shows promising results
