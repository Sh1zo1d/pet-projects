# Star Surface Temperature Prediction

## Project Description
The project involves using a neural network to predict the surface temperature of detected stars.

## Skills and Tools
* pandas
* torch
* numpy
* sklearn.model_selection.train_test_split
* matplotlib.pyplot
* ProfileReport
* warnings
* collections.Counter
* re
* scipy.stats
* fuzzywuzzy.fuzz
* fuzzywuzzy.process
* OneHotEncoder
* StandardScaler
* sklearn.cluster.KMeans
* sklearn.compose.ColumnTransformer
* Pipeline
* torch.nn
* math.ceil
* torch.optim.Adam
* sklearn.metrics.mean_squared_error
* sklearn.compose.make_column_transformer

## General Conclusion

The lowest RMSE is approximately 4064.127, which I achieved with the following:
* nn.Softplus() in even layers
* LeakyReLU() in odd layers and at the output
* Dropout regularization (p=0.5) after each hidden layer
* Using He initialization with parameters (mode='fan_in', nonlinearity='relu')
* Using standard deviation with mean=0.5, std=1
* 3 hidden layers with 12, 8, and 4 neurons, respectively.

Compared to the baseline model, the quality increased by 39%.

I consider this to be a reasonably good result relative to the baseline model.















<!--

# Описание проекта "Определение_температуры_на_поверхности_звезд":


* Я начал работу над самостоятельным проектом, связанным с астрономией и машинным обучением. Задача от обсерватории - разработать нейросеть, которая сможет предсказывать температуру на поверхности обнаруженных звёзд.

* Обычно для определения температуры звезд учёные используют различные методы, такие как закон смещения Вина, закон Стефана-Больцмана и спектральный анализ. Но обсерватория хочет попробовать подход с машинным обучением, чтобы получить более точные и удобные результаты.

* В базе обсерватории уже есть характеристики 240 звёзд, которые были изучены ранее. Эти характеристики включают относительную светимость, относительный радиус, абсолютную звёздную величину, звёздный цвет и тип звезды.


# Цель проекта:
* Моя цель - разработать модель машинного обучения, которая сможет предсказывать температуру звезд на основе указанных характеристик.


# Характеристики
* Относительная светимость L/Lo — светимость звезды относительно Солнца.
* Относительный радиус R/Ro — радиус звезды относительно радиуса Солнца.
* Абсолютная звёздная величина Mv — физическая величина, характеризующая блеск звезды.
* Звёздный цвет (white, red, blue, yellow, yellow-orange и др.) — цвет звезды, который определяют на основе спектрального анализа.
* Тип звезды.
Тип звезды-Номер,соответствующий типу
* Коричневый карлик-0
* Красный карлик-1
* Белый карлик-2
 *Звёзды главной последовательности-3
* Сверхгигант-4
* Гипергигант-5

* Абсолютная температура T(K) — температура на поверхности звезды в Кельвинах.


















