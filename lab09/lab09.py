# Wprowadzenie do języka Python
# Paweł Majorowski
# 155090
# Grupa 2
# lab 09
class Point:
    x:int
    y:int

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'
    
    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __mul__(self, skalar):
        return Point(self.x * skalar, self.y * skalar)
    
    def __eq__(self, inny_obiekt):
        if(type(inny_obiekt) != type(self)):
            return False
        if(self.x != inny_obiekt.x):
            return False
        if(self.y != inny_obiekt.y):
            raise False
        return True

print('Zadanie 1:')

print('Wywołanie konstruktora bez podania wartości inicjalizujących')
punkt = Point()
print('punkt.x:', punkt.x)
print('punkt.y:', punkt.y)
print('Wywołanie konstruktora z podaniem wartości inicjalizujących')
punkt = Point(5, 4)
print('punkt.x:', punkt.x)
print('punkt.y:', punkt.y)

print('\nZadanie 2:')
print('punkt:', punkt)

print('\nZadanie 3:')
skalar = 5
punkt = Point(3, 4)
print('punkt:', punkt)
print('skara:', skalar)
print('punkt * skalar: ', punkt * skalar)

print('\nZadanie 4:')
from itertools import combinations
punkty = {}
punkty['punkt_1'] = Point(3, 4)
punkty['punkt_2'] = Point(4, 3)
punkty['punkt_3'] = Point(3, 4)
punkty['punkt_4'] = 'Point(3, 4)'
pary_punktow = list(combinations(list(punkty.keys()), 2))
for para in pary_punktow:
    p1 = para[0]
    p2 = para[1]
    print('Punkt', p1.split('_')[-1], end=' ')
    if(punkty[p1] == punkty[p2]):
        print('jest', end=' ')
    else:
        print('NIE jest', end=' ')
    print('równy punktowi', p2.split('_')[-1])

print('\nZadanie 5:')

class Polygon():
    points:list[Point]

    def __init__(self):
        self.points = []

    def add_point(self, point: Point):
        self.points.append(point)

    def __str__(self):
        return 'Polygon' + str(self.points)
    
    def __getitem__(self, items):
        try:
            return self.points[items]
        except TypeError: 
            print(f"Indeks musi mieć wartość typu int lub slice, a nie {type(items)}")
            return None

kwadrat = Polygon()
kwadrat.add_point(Point(2, 2))
kwadrat.add_point(Point(-2, 2))
kwadrat.add_point(Point(-2, -2))
kwadrat.add_point(Point(2, -2))

print('\nZadanie 6:')
print(kwadrat)

print('\nZadanie 7:')
print('kwadrat[0]:', kwadrat[0])
print('kwadrat[1::2]:', kwadrat[1::2])
print('kwadrat["xd"]: ', end='')
kwadrat["xd"]