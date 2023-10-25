# Toxic Comment Classification

## Project Description
The aim of this project is to create a model that helps determine the sentiment of text, specifically edits and comments for products in an online store.

## Skills and Tools
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

## General Conclusion
Best model:

* LogisticRegression(C=4, class_weight='balanced', max_iter=12, random_state=7, solver='sag')

* A classic model without any balance improvements yields an F1 score of 0.77.

* The best F1 score on the test set:

* F1-score for the test set: 0.77

* The model with stratification and weights achieved a maximum of 0.769.
