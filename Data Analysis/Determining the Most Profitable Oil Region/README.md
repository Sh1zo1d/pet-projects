# Choosing a Drilling Location for an Oil Well

## Project Description
The goal of this project is to determine the best location for drilling an oil well.

## Skills and Tools
* pandas
* numpy 
* train_test_split
* r2_score
* mean_squared_error
* mean_absolute_error
* mean_absolute_percentage_error
* seaborn 
* warnings
* matplotlib.pyplot 
* ProfileReport
* LinearRegression

## Key Findings

* The best region for exploration is the second one with an average profit of 497 million rubles.

<!--

# Описание проекта "Выбор_локации_для_скважины":

* Нефтедобывающая компания «ГлавРосГосНефть» стоит перед важным решением — выбором места для бурения новой нефтяной скважины. Для определения наилучшего местоположения, обычно используются следующие шаги:

1. Сбор характеристик скважин в избранном регионе, включая качество нефти и объём её запасов.
2. Построение модели для предсказания объёма запасов нефти в новых скважинах.
3. Выбор скважин с самыми высокими оценками значений, основанными на предсказанных объёмах запасов.
4. Определение региона с максимальной суммарной прибылью отобранных скважин.

# Условия задачи:

* Для обучения модели разрешено использовать только линейную регрессию, так как другие модели считаются недостаточно предсказуемыми для данной задачи.
* При разведке каждого региона исследуется 500 точек. С помощью машинного обучения из этих точек будет выбрано 200 лучших для разработки скважин.
* Бюджет на разработку скважин в каждом регионе составляет 10 млрд рублей.
* При текущих ценах на нефть, один баррель сырья приносит 450 рублей дохода. Учитывая, что объём продукции указан в тысячах баррелей, доход с каждой единицы продукта составляет 450 тыс. рублей.
* После оценки рисков необходимо выбрать только те регионы, где вероятность убытков меньше 2.5%. Среди этих регионов будет выбран тот, который обещает наибольшую среднюю прибыль.

# Описание данных:

* id — уникальный идентификатор скважины
* f0, f1, f2 — три признака точек (неважно, что они означают, но сами признаки значимы)
* product — объём запасов в скважине (тыс. баррелей)















