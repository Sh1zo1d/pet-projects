
# Binary Classification of Operator Tariffs

## Project Description
The goal of this project is to build a classification model that will determine the suitable tariff plan for mobile operator customers.

## Skills and Tools
* pandas
* numpy
* balanced_accuracy_score
* accuracy_score
* f1_score
* precision_score
* recall_score
* fbeta_score
* LogisticRegression
* RandomForestClassifier
* DecisionTreeClassifier
* train_test_split
* GridSearchCV
* RandomizedSearchCV
* cross_val_score
* collections.Counter
* seaborn
* pandas_profiling
* plot_roc_curve
* plot_confusion_matrix
* matplotlib.pyplot

## Key Findings

* The best random forest model with the following parameters:
  * n_estimators=3, max_depth=5
  * Mean Fbeta score on the validation set is 0.6162.




<!--
# Описание проекта:

* Цель данного проекта — построить модель для задачи классификации, которая определит подходящий тарифный план для клиентов оператора мобильной связи "Мегалайн". В распоряжении у нас имеются данные о поведении клиентов, которые уже используют тарифы "Смарт" и "Ультра".

* Задача состоит в том, чтобы создать модель, которая на основе анализа поведения клиентов сможет предсказать, какой тариф лучше всего подходит для новых пользователей. Для достижения успеха в проекте, нам необходимо достигнуть доли правильных ответов (accuracy) на тестовой выборке не менее 0.75.

* Важным этапом в решении задачи будет выбор и построение оптимальной модели, которая позволит достичь максимально возможной точности предсказаний и обеспечит удовлетворение поставленному условию. Мы будем использовать различные алгоритмы классификации и методы настройки гиперпараметров модели для достижения наилучшего результата.

* В процессе работы с данными предобработка не потребуется, так как она уже была выполнена. Наша задача сосредоточится на выборе и обучении оптимальной модели, а затем на оценке ее точности на тестовой выборке.


# Описание данных:
* Каждый объект в наборе данных — это информация о поведении одного пользователя за месяц. Известно:
* сalls — количество звонков,
* minutes — суммарная длительность звонков в минутах,
* messages — количество sms-сообщений,
* mb_used — израсходованный интернет-трафик в Мб,
* is_ultra — каким тарифом пользовался в течение месяца («Ультра» — 1, «Смарт» — 0).

