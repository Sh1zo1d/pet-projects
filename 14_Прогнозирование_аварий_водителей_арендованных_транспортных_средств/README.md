# Accident Prediction for Rental Vehicle Drivers

## Project Description
The goal is to create a system capable of assessing the risk of accidents along a selected route. Risk is defined as the probability of an accident resulting in any vehicle damage.

## Skills and Tools
* pandas 
* matplotlib.pyplot
* sqlalchemy
* seaborn
* warnings 
* RandomForestClassifier
* LogisticRegression
* balanced_accuracy_score
* accuracy_score
* classification_report
* roc_auc_score
* LinearRegression
* GridSearchCV
* LogisticRegression
* precision_score
* recall_score
* fbeta_score
* f1_score
* make_scorer
* ColumnTransformer
* make_column_transformer
* Pipeline
* CatBoostClassifier
* StandardScaler
* OneHotEncoder
* train_test_split
* cross_val_score
* BinaryEncoder
* optuna
* LGBMClassifier
* collections.Counter
* re
* calendar
* math
* numpy

## General Conclusion

To improve the model's quality, it is essential to equip vehicles with sensors and cameras that collect data on weather conditions, the vehicle's status, and assess the driver's mood based on facial expressions.

Key metrics for the best model:

* Logistic Regression:
  * f1-0 - 0.61
  * f1-1 - 46

Where f1-0 represents predictions for non-offending accidents, and f1-1 represents the opposite.

If you have access to data on a person's condition before renting a car, you could potentially increase successful predictions to 60-70%.


<!--
# Описание проекта:

* Требуется разработать систему, способную оценивать вероятность ДТП с повреждениями транспортных средств по заданному маршруту. Система должна предоставлять водителю предупреждение и рекомендации по маршруту в случае высокого уровня риска. Главная цель проекта - исследовать возможность предсказания вероятности ДТП с использованием исторических данных для конкретного региона.


# Краткое описание таблиц:

collisions — общая информация о ДТП

* Имеет уникальный case_id. Эта таблица описывает общую информацию о ДТП. Например, где оно произошло и когда.


parties — информация об участниках ДТП:

* Имеет неуникальный case_id, который сопоставляется с соответствующим ДТП в таблице collisions. Каждая строка здесь описывает одну из сторон, участвующих в ДТП. Если столкнулись две машины, в этой таблице должно быть две строки с совпадением case_id. Если нужен уникальный идентификатор, это case_id and party_number.

vehicles — информация о пострадавших машинах:

* Имеет неуникальные case_id и неуникальные party_number, которые сопоставляются с таблицей collisions и таблицей parties. Если нужен уникальный идентификатор, это case_id and party_number.
