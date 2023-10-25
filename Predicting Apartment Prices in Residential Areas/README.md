# PySpark Big Data Processing System

## Project Description
The task is to train a linear regression model on housing data in California in 1990 and predict the median housing cost.

## Skills and Tools
* Pyspark

## Overall Conclusion

The best model turned out to be without standardization:

* Root Mean Squared Error (RMSE): 69780.1
* Coefficient of Determination (R2): 0.632608
* Mean Absolute Error (MAE): 50100.9







<!--
# Описание данных

В колонках датасета содержатся следующие данные:
* longitude — широта;
* latitude — долгота;
* housing_median_age — медианный возраст жителей жилого массива;
* total_rooms — общее количество комнат в домах жилого массива;
* total_bedrooms — общее количество спален в домах жилого массива;
* population — количество человек, которые проживают в жилом массиве;
* households — количество домовладений в жилом массиве;
* median_income — медианный доход жителей жилого массива;
* median_house_value — медианная стоимость дома в жилом массиве;
* ocean_proximity — близость к океану.

На основе данных нужно предсказать медианную стоимость дома в жилом массиве — median_house_value. Для оценки качества модели используются метрики RMSE, MAE и R2.
