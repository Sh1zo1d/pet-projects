




# Анализ_данных_о_сердечных_заболеваниях

## Описание проекта
Нужно разработать модель, которая будет предсказывать вероятность заболевания сердца у пациента по различным признакам

## Навыки и инструменты

* SMOTE
* SimpleImputer
* cross_val_score
* pandas
* ProfileReport
* os
* numpy
* RandomForestClassifier
* DecisionTreeClassifier
* GridSearchCV
* train_test_split
* balanced_accuracy_score
* accuracy_score
* f1_score
* precision_score
* recall_score
* fbeta_score
* roc_auc_score
* collections.Counter
* seaborn
* warnings
* matplotlib.pyplot
* OneHotEncoder
* BinaryEncoder
* plot_roc_curve
* plot_confusion_matrix
* import optuna
* classification_report
* SVC
* KNeighborsClassifier
* shuffle
* classification_report,roc_curve

## Общий вывод

Лучшая модель:

* RandomForestClassifier - Recall - 88.2%








<!--

# Описание преокта

Данные- https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data 


Это многомерный тип набора данных, что означает предоставление или включение различных отдельных математических или статистических переменных, многомерный анализ числовых данных. Он состоит из 14 атрибутов: возраст, пол, тип боли в груди, покойное артериальное давление, уровень холестерина в сыворотке крови, голодание крови на глаз, результаты покойной электрокардиографии, достигнутая максимальная частота сердечных сокращений, стенокардия, вызванная физической нагрузкой, депрессия ST, вызванная физической нагрузкой по сравнению с покоем, наклон вершины ST-сегмента при пиковой нагрузке, количество основных сосудов и талассемия. В этой базе данных содержится 76 атрибутов, но все опубликованные исследования относятся к использованию подмножества из 14 из них. База данных Кливленда - единственная, используемая исследователями машинного обучения на сегодняшний день. Одной из основных задач с использованием этого набора данных является прогнозирование на основе предоставленных атрибутов пациента, имеет ли этот конкретный человек сердечное заболевание или нет, а также экспериментальная задача диагностирования и выявления различных идей из этого набора данных, которые могли бы помочь в понимании проблемы более глубоко.


# Описание данных 


Column Descriptions:
* id (Unique id for each patient)
* age (Age of the patient in years)
* origin (place of study)
* sex (Male/Female)
* cp chest pain type ([typical angina, atypical angina, non-anginal, asymptomatic])
* trestbps resting blood pressure (resting blood pressure (in mm Hg on admission to the hospital))
* chol (serum cholesterol in mg/dl)
* fbs (if fasting blood sugar > 120 mg/dl)
* restecg (resting electrocardiographic results)
-- Values: [normal, stt abnormality, lv hypertrophy]
* thalach: maximum heart rate achieved
* exang: exercise-induced angina (True/ False)
* oldpeak: ST depression induced by exercise relative to rest
* slope: the slope of the peak exercise ST segment
* ca: number of major vessels (0-3) colored by fluoroscopy
* thal: [normal; fixed defect; reversible defect]
* num: the predicted attribute
