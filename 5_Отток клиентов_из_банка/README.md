# Customer Churn Prediction for a Bank

## Project Description
The goal of this project is to build a model that predicts whether a customer will leave the bank in the near future or not.

## Skills and Tools
* SMOTE
* pandas 
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
* fbeta_score,roc_auc_score
* collections.Counter
* seaborn
* warnings
* matplotlib.pyplot
* OneHotEncoder
* BinaryEncoder
* ProfileReport
* plot_roc_curve
* plot_confusion_matrix
* optuna
* classification_report
* SVC
* KNeighborsClassifier
* shuffle

## Key Findings

The best preprocessing option: UpSampling

Optimal parameters were selected for the RandomForestClassifier algorithm:

* Number of trees (n_estimators): 116
* Maximum tree depth (max_depth): 9
* Tree splitting criterion (criterion): gini
* Class weights (class_weight): {0: 1, 1: 1.3}
* The model demonstrated moderate quality, providing reliable predictions of class 0 with an accuracy of 0.91 and recall of 0.87. These metrics are quite satisfactory.

* However, it is important to note the relatively low ability of the model to predict the secondary class 1, which is reflected in the F1-score of approximately 0.61.

* The final F1-score is approximately 0.61, emphasizing that the model consistently strikes a balance between precision and recall in classifying the data.


<!--


*Описание проекта:

* Для «Бета-Банка» стало актуальным уменьшение оттока клиентов, поскольку они уходят из банка каждый месяц. Хотя эти уходы небольшие, они заметны. Маркетологи банка пришли к выводу, что удержание текущих клиентов обходится дешевле, чем привлечение новых.

* Цель данного проекта — построить модель, которая позволит спрогнозировать, уйдет ли клиент из «Бета-Банка» в ближайшее время или нет. Для этого предоставлены исторические данные о поведении клиентов и фактах расторжения договоров с банком.

* Главная метрика, которую мы будем использовать для оценки качества модели, — F1-мера. Наша задача — достичь предельно высокого значения F1-меры, равного не менее 0.59, чтобы успешно выполнить проект. Мы также измерим AUC-ROC и сравним его значение с F1-мерой, чтобы более полно оценить производительность модели.

* В ходе выполнения проекта мы будем использовать различные алгоритмы классификации и настраивать их гиперпараметры для получения наилучших результатов. Основное внимание будет уделено обработке данных, созданию и обучению моделей, а также оценке их точности на тестовой выборке.



# Описание данных:

## Признаки
	* RowNumber — индекс строки в данных
	* CustomerId — уникальный идентификатор клиента
	* Surname — фамилия
	* CreditScore — кредитный рейтинг
	* Geography — страна проживания
	* Gender — пол
	* Age — возраст
	* Tenure — сколько лет человек является клиентом банка
	* Balance — баланс на счёте
	* NumOfProducts — количество продуктов банка, используемых клиентом
	* HasCrCard — наличие кредитной карты
	* IsActiveMember — активность клиента
	* EstimatedSalary — предполагаемая зарплата
## Целевой признак
	* Exited — факт ухода клиента













