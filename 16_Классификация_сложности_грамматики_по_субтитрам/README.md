# Классификация_сложности_грамматики_по_субтитрам

## Описание проекта
В этом проекте нужно построить алгоритм, который будет определять сложность материала по шкале CERF. Я использовал не только бинарную классификацию, но и регрессию. Точность на регресии показала наилучший результат 0.7 уровня ошибки в среднем.

## Навыки и инструменты
* pandas
* numpy
* optuna
* nltk
* sklearn
* train_test_split
* os
* PyPDF2
* tika.parser
* re
* pysrt
* fuzzywuzzy.fuzz
* fuzzywuzzy.process
* nltk.corpus.stopwords
* nltk.tokenize.sent_tokenize
* warnings
* word_tokenize
* pos_tag
* LinearRegression
* LogisticRegression
* mean_absolute_error
* mean_squared_error
* r2_score
* accuracy_score
* recall_score
* fbeta_score
* roc_auc_score
* plot_roc_curve
* f1_score
* precision_score
* plot_confusion_matrix
* classification_report
* RandomForestRegressor
* RandomForestClassifier
* CountVectorizer
* ngrams
* spacy

## Общий вывод
Лучшие модели:
* RandomForestClassifier = F1- 0.6
* LinearRegression = MAE = 0.71
