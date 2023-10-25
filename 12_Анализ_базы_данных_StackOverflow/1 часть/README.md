![image](https://github.com/Sh1zo1d/projects/assets/102797488/9bfd5a80-179b-45b5-89e0-992ca5c12840)


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
# Описание данных
## Таблица badges

Хранит информацию о значках, которые присуждаются за разные достижения. Например, пользователь, правильно ответивший на большое количество вопросов про PostgreSQL, может получить значок postgresql. 

* id	Идентификатор значка, первичный ключ таблицы
* name	Название значка
* user_id	Идентификатор пользователя, которому присвоили значок, внешний ключ, отсылающий к таблице users
* creation_date	Дата присвоения значка

## Таблица post_types
Содержит информацию о типе постов. Их может быть два:

* Question — пост с вопросом;
* Answer — пост с ответом.

* id	Идентификатор поста, первичный ключ таблицы
* type	Тип поста

## Таблица posts
Содержит информацию о постах.

* id	Идентификатор поста, первичный ключ таблицы
* title	Заголовок поста
* creation_date	Дата создания поста
* favorites_count	Число, которое показывает, сколько раз пост добавили в «Закладки»
* last_activity_date	Дата последнего действия в посте, например комментария
* last_edit_date	Дата последнего изменения поста
* user_id	Идентификатор пользователя, который создал пост, внешний ключ к таблице users
* parent_id	Если пост написали в ответ на другую публикацию, в это поле попадёт идентификатор поста с вопросом
* post_type_id	Идентификатор типа поста, внешний ключ к таблице post_types
* score	Количество очков, которое набрал пост
* views_count	Количество просмотров



## Таблица users
Содержит информацию о пользователях.

* id	Идентификатор пользователя, первичный ключ таблицы
* creation_date	Дата регистрации пользователя
* display_name	Имя пользователя
* last_access_date	Дата последнего входа
* location	Местоположение
* reputation	Очки репутации, которые получают за хорошие вопросы и полезные ответы
* views	Число просмотров профиля пользователя

## Таблица vote_types

Содержит информацию о типах голосов. Голос — это метка, которую пользователи ставят посту. Типов бывает несколько: 

* UpMod — такую отметку получают посты с вопросами или ответами, которые пользователи посчитали уместными и полезными.
* DownMod — такую отметку получают посты, которые показались пользователям наименее полезными.
* Close — такую метку ставят опытные пользователи сервиса, если заданный вопрос нужно доработать или он вообще не подходит для платформы.
* Offensive — такую метку могут поставить, если пользователь ответил на вопрос в грубой и оскорбительной манере, например, указав на неопытность автора поста.
* Spam — такую метку ставят в случае, если пост пользователя выглядит откровенной рекламой.

* id	Идентификатор типа голоса, первичный ключ
* name	Название метки
## Таблица votes
Содержит информацию о голосах за посты. 

* id	Идентификатор голоса, первичный ключ
* post_id	Идентификатор поста, внешний ключ к таблице posts
* user_id	Идентификатор пользователя, который поставил посту голос, внешний ключ к таблице users
* bounty_amount	Сумма вознаграждения, которое назначают, чтобы привлечь внимание к посту
* vote_type_id	Идентификатор типа голоса, внешний ключ к таблице vote_types
* creation_date	Дата назначения голоса
