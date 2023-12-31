# Car Market Value Estimation

## Project Description
Create a model based on historical data to determine the market value of a car.

## Skills and Tools
* pandas
* warnings
* sklearn.model_selection.train_test_split
* CatBoostRegressor
* LinearRegression
* RandomForestRegressor
* collections.Counter
* sklearn.metrics.mean_absolute_error
* sklearn.metrics.mean_squared_error
* sklearn.metrics.r2_score
* sklearn.model_selection.cross_val_score
* pandas_profiling
* LGBMRegressor
* re
* numpy
* pgeocode
* optuna
* seaborn
* matplotlib.pyplot
* category_encoders
* OneHotEncoder

## General Conclusion

* Best model: Catboost

  * RMSE = 1671.5349657268462

  * Training time = ~1 minute

  * Prediction time = ~312 milliseconds







<!--

# Описание проекта "Определение_рыночной_стоимости_автомобиля":

* Я работаю над интересным проектом - разработкой модели для сервиса по продаже автомобилей с пробегом "Не бит, не крашен". Наша цель - создать удобное приложение, которое поможет пользователям узнать рыночную стоимость их автомобилей.

* Мы хотим построить модель, которая будет способна предсказывать рыночную стоимость автомобилей на основе их технических характеристик, комплектации и цен схожих автомобилей. Это позволит нашим клиентам получить честную оценку своего авто перед продажей или обменом.

# Критерии успеха:

* Качество предсказаний - модель должна точно определять стоимость автомобилей, чтобы клиенты могли быть уверены в полученной информации.
* Время обучения модели - важный аспект, и нам необходимо разработать модель, которая обучается быстро, чтобы оперативно обновлять данные и улучшать предсказания.
* Время предсказания модели - также критично, ведь нашим пользователям нужны быстрые результаты.

# Описание данных:

## Признаки

* DateCrawled — дата скачивания анкеты из базы
* VehicleType — тип автомобильного кузова
* RegistrationYear — год регистрации автомобиля
* Gearbox — тип коробки передач
* Power — мощность (л. с.)
* Model — модель автомобиля
* Kilometer — пробег (км)
* RegistrationMonth — месяц регистрации автомобиля
* FuelType — тип топлива
* Brand — марка автомобиля
* Repaired — была машина в ремонте или нет
* DateCreated — дата создания анкеты
* NumberOfPictures — количество фотографий автомобиля
* PostalCode — почтовый индекс владельца анкеты (пользователя)
* LastSeen — дата последней активности пользователя

## Целевой признак

* Price — цена (евро)
