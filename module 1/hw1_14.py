'''Программисты часто работают с геоданными. Поработаем и мы с ними. 
Нам необходимо написать программу, в которой мы рассчитаем расстояние между двумя точками на поверхности Земли.

Считать будем расстояние между двумя городами: Киевом и Лондоном
Координаты Киева в градусах:

Широта lat1 = 50.45
Долгота lon1 = 30.523
Координаты Лондона в градусах:

Широта lat2 = 51.5072
Долгота lon2 = -0.1275
Радиус Земли примем 6371.01 км. Расстояние в километрах между городами с учетом искривленности планеты можно найти по следующей формуле:

distance = 6371.01 · arccos(sin(lat1) · sin(lat2) + cos(lat1) · cos(lat2) · cos(lon1 - lon2))

Помните, что тригонометрические функции в Python оперируют радианами. И значит величины из градусов необходимо перевести в радианы, 
прежде чем вычислять расстояние между точками. Для этого в модуле math есть функция radians

<радианы> = math.radians(<градусы>)
Также:

arccos(x) — это math.acos(x)
sin(x) — это math.sin(x)
cos(x) — это math.cos(x)
Вычислите distance по указанной формуле с помощью предложенных методов модуля math.'''

import math

RADIUS = float(6371.01)

lat1 = math.radians(50.45)
lon1 = math.radians(30.523)

lat2 = math.radians(51.5072)
lon2 = math.radians(-0.1275)

distance = RADIUS * math.acos(math.sin(lat1) * math.sin(lat2) +
                              math.cos(lat1) * math.cos(lat2) * math.cos(lon1 - lon2))
