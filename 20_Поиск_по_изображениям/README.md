# Поиск_по_изображениям

## Описание проекта
Пользователи размещают свои фотографии на хостинге и сопровождают их полным описанием: указывают место съёмок, модель камеры и т. д. Отличительная особенность сервиса — описание: его может предоставить не только тот, кто размещает фотографию, но и другие пользователи портала. Суть поиска заключается в следующем: пользователь сервиса вводит описание нужной сцены. Сервис выводит несколько фотографий с такой же или похожей сценой.

## Навыки и инструменты
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

## Общий вывод



* Бустинг (CatBoostRegressor): RMSE: 0.11422264868523815, Время выполнения: 412.53947710990906 сек
* Random Forest регрессор: RMSE: 0.12220017624756276, Время выполнения: 154.18005514144897 сек
* Бустинг (CatBoostRegressor) показал лучший результат с наименьшим значением RMSE
* Random Forest регрессор также показал хороший результат, близкий к бустингу.
* Линейная регрессия и Ridge регрессия демонстрируют более высокие значения RMSE
* Нейронная сеть показывает перспективные результаты
