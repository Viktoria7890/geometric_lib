import math
'модуль math предоставляет обширный фурнционал для проведения вычислений с вещественными числами (числами с плавующий точкой)'

def area(r):
    return math.pi * 2 * r * r
    'Принимает число, которое является радиусом круга r'
    'возвращает площадь круга,вычисляя ее по формуле: π*r^2'
def perimeter(r):
    return 2 * math.pi * r
    'Принимает число, которое является радиусом круга r'
    'возвращает площадь круга,вычисляя ее по формуле: π*r'
#
# r=4
# print(area(r))
# print(perimeter(r))
