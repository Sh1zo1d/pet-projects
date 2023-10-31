![image](https://github.com/Sh1zo1d/projects/assets/102797488/707f816f-555f-4909-bfaf-4e6e58596496)


# StackOverflow Database Analysis

## Project Description
The project involves analyzing the StackOverflow database and extracting valuable information about questions, answers, comments, and user ratings for the year 2008.

## Skills and Tools
* matplotlib
* pandas
* sqlalchemy
* seaborn

## General Conclusion:

The tasks were accomplished using the SQLAlchemy library, and the data yielded the following conclusions.

* Task 1: Analysis of the total number of publications per month
  * The maximum number of publications is 452,928,568, which occurred in September 2008.
  * The minimum is 669,895, posted in July 2008.
  * Key findings:
    * There was a sharp increase in publications from July to September.
    * A decline was observed from October to December.

* Task 2: Analysis of displaying user names
  * There are 254 users with 19 non-unique names.
  * 57 unique display names.
  
* Task 3: Number of publications in 2008 by month for users registered in September 2008.
  * Anomalies were identified - 32 publications in August 2008.

* Task 6: On average, how many days did users interact with the site in the first week of December 2008.
  * On average, users were active for 2 days in the first week of December 2008.

* Task 8: Cohort Analysis
  * Anomalies: For the first cohort, values change rapidly and jump, whereas the usual retention decreases exponentially or linearly.

* Task 9: The percentage change in the number of posts each month from September 1 to December 31, 2008.
  * From September to December 2008, a stable decrease in the number of publications by month was observed:
  * September - 70,371
  * October - 60,102
  * November - 46,975
  * December - 44,592




























<!--
# Описание проекта "Анализ_базы_данных_StackOverflow":

## Проект состоит из двух частей: в первой части я буду решать несколько задач в SQL-тренажере, а во второй части — напишу SQL-запросы в Jupyter Notebook с помощью библиотеки SQLAlchemy. Важно отметить, что задачи во второй части будут проверены вручную.

# Цель проекта:
Целью проекта является анализ данных из базы StackOverflow и получение полезной информации о вопросах, ответах, комментариях и оценках пользователей за 2008 год.

# Структура данных:
База данных содержит информацию о постах за 2008 год, а также информацию о более поздних оценках, которые эти посты получили. Пользователи сервиса задают вопросы, отвечают на посты, оставляют комментарии и ставят оценки другим ответам.

# Задачи проекта:

* Решение задач в SQL-тренажере для закрепления навыков SQL-запросов.
* Написание SQL-запросов в Jupyter Notebook с помощью библиотеки SQLAlchemy.
* Анализ данных и получение полезной информации о вопросах, ответах, комментариях и оценках за 2008 год.
