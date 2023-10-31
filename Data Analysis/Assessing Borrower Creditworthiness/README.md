# Bank analysis for preparing a classification system

## Project Description
It is necessary to conduct an analysis of real Yandex.Music data using the Pandas library to compare the behavior and preferences of users from two capitals - Moscow and St. Petersburg.

## Skills and Tools

* Python
* Numpy

## General Conclusion
* As a result of the analysis, the main factors influencing the timely repayment of the loan were identified. Clients who are in unstable relationships (unmarried / in a civil marriage) and have a certain number of children (1, 2, 4), as well as those with income less than 30,000 or in the range of 50,001 - 200,000, and a loan purpose for car operations or education, have a higher probability of loan payment delays.

* On the other hand, widows/widowers without children, with income in the range of 30,001 - 50,000, and a loan purpose for real estate operations, have the lowest probability of loan default.

* These results can help the bank optimize its loan approval processes, taking into account the factors mentioned and making more informed decisions.





<!--
# Цель проекта: 

Разобраться, как семейное положение и количество детей клиента влияют на своевременное погашение кредита. Заказчиком проекта является кредитный отдел банка.

# Задачи проекта:

* Провести анализ данных о платежеспособности клиентов банка.
* Изучить зависимость между семейным положением, количеством детей и возвратом кредита в срок.
* Определить, какие категории клиентов имеют лучшие показатели возврата кредита, а также выявить группы с наибольшим риском невозврата.
* Подготовить выводы и рекомендации на основе проведенного анализа.
* Важность проекта: Результаты исследования будут использованы при разработке системы классификации кредитного риска. Эта система позволит оценить способность потенциальных заёмщиков вернуть кредит в банк. Таким образом, анализ поможет банку оптимизировать процесс выдачи кредитов и снизить риски невозврата.

# Ожидаемый результат: 
Выявление статистически значимых зависимостей между платежеспособностью клиентов и их семейным положением, а также количеством детей. Подготовка рекомендаций по улучшению системы классификации кредитного риска и оптимизации процесса принятия решений о выдаче кредитов.


# Описание данных:
* children — количество детей в семье
* days_employed — общий трудовой стаж в днях
* dob_years — возраст клиента в годах
* education — уровень образования клиента
* education_id — идентификатор уровня образования
* family_status — семейное положение
* family_status_id — идентификатор семейного положения
* gender — пол клиента
* income_type — тип занятости
* debt — имел ли задолженность по возврату кредитов
* total_income — ежемесячный доход
* purpose — цель получения кредита

# Цели:
1) Есть ли зависимость между количеством детей и возвратом кредита в срок?
2) Есть ли зависимость между семейным положением и возвратом кредита в срок?
3) Есть ли зависимость между уровнем дохода и возвратом кредита в срок?
4) Как разные цели кредита влияют на его возврат в срок?

