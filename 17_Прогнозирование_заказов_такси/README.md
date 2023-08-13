# Прогнозирование_заказов_такси

## Описание проекта
Необходимо разработать модель для прогнозирования количества заказов такси на следующий час в аэропортах. Цель проекта - обеспечить компанию эффективными прогнозами, которые позволят привлекать больше водителей в период пиковой нагрузки.


## Навыки и инструменты
* pandas
* holidays
* typing.Union
* re
* warnings
* collections.Counter
* numpy
* matplotlib.pyplot
* statsmodels.tsa.seasonal.seasonal_decompose
* mean_squared_error
* make_scorer
* train_test_split
* GridSearchCV
* TimeSeriesSplit
* RandomizedSearchCV
* cross_val_score
* RandomForestRegressor
* LinearRegression
* CatBoostRegressor
* optuna

from itertools import product

## Общий вывод
Лучшая модель: 
* RandomForestRegressor = RMSE - 35.844583
