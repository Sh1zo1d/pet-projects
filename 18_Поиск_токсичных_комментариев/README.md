# Поиск_токсичных_комментариев

## Описание проекта
Нужно создать модель, которая будет помогать определять тональност текста, а именно правки и комментарии для товаров в интернет магазине 

## Навыки и инструменты
* pandas
* warnings
* train_test_split
* cross_val_score
* cross_val_predict
* numpy
* optuna
* re
* collections.Counter
* accuracy_score
* recall_score
* fbeta_score
* roc_auc_score
* make_scorer
* f1_score
* precision_score
* classification_report
* balanced_accuracy_score
* LogisticRegression
* RandomForestClassifier
* torch
* nltk.corpus.stopwords
* nltk.tokenize.word_tokenize
* CountVectorizer
* math
* compute_class_weight
* shuffle
* CatBoostClassifier
* GridSearchCV
* matplotlib.pyplot
* TfidfVectorizer
* WordNetLemmatizer
* spacy
* tqdm
* wordnet
* DecisionTreeClassifier
* Pipeline
* enable_halving_search_cv
* HalvingGridSearchCV
* RandomOverSampler
* RandomUnderSampler
* RocCurveDisplay
* ConfusionMatrixDisplay

## Общий вывод

Лучшая модель:

* LogisticRegression(C=4, class_weight='balanced', max_iter=12, random_state=7, solver='sag')

* Классическая модель без каких-либо противодействий дизбалансу дает f1 = 0.77.

* Лучшая F1-мера на тестовой выборке:

* F1-score для тестовой выборки: 0.77

* Модель с statify, весами и дала максимально 0.769
