# Wprowadzenie do języka Python
# Paweł Majorowski
# 155090
# Grupa 2
# lab 05
#
# Zadanie 1
print('\nZadanie 1')

A = [1/x for x in range(1,11)]
B = [2**i for i in range(0, 11)]
C = [x for x in B if x % 4 == 0]

print('A:', A)
print('B:', B)
print('C:', C)

# Zadanie 2
import random
print('\nZadanie 2')

macierz = [[random.randint(0,9) for x in range(0, 4)] for y in range(0, 4)]
przekatna = [macierz[i][i] for i in range(0,4)]

print('macierz:')
for i in range(0,4):
    print(macierz[i])
print('przekątna:')
print(przekatna)

# Zadanie 3
print('\nZadanie 3')

zdanie = 'Ala ma kota.'
lista_slow = zdanie.split(' ')
generator_krotki = ((slowo, [ord(znak) for znak in slowo]) for slowo in lista_slow)
for i in generator_krotki:
    print(i)

# Zadanie 4
print('\nZadanie 4')
import math


def row_kwadratowe(a: float, b: float, c: float) -> float:
    delta = b**2 - 4 * a * c
    if (delta < 0):
        # brak pierwiastków
        return -1
    elif (delta == 0):
        # jeden pierwiastek
        x = (-b) / (2 * a)
        return x
    else:
        # równanie ma dwa pierwiastki
        x1 = (- b - math.sqrt(delta)) / (2 * a)
        x2 = (- b + math.sqrt(delta)) / (2 * a)
        return x1, x2

print(row_kwadratowe(6,1,3))
print(row_kwadratowe(1,2,1))
print(row_kwadratowe(1,4,1))

# Zadanie 5
print('\nZadanie 5')

def zad_5(n: int) -> list():
    wyniki = [0 for liczba_oczek in range(0, 6)]
    for rzut in range(0, n):
        wynik_rzutu = random.randint(1, 6)
        wyniki[wynik_rzutu-1] += 1
    lista_krotek = [(f'oczka: {i}', f'rzutów: {wyniki[i-1]}') for i in range(1, 7)]
    return lista_krotek

n = int(input('Podaj n: '))
print(zad_5(n))

# Zadanie 6
print('\nZadanie 6')

def zad_6(* napisy):
    if(len(napisy) == 0):
        return []
    else:
        lista = [i for i in napisy]
        lista.sort()
        return lista

print(zad_6('ala', 'ma', 'kota', 'kot', 'lubi', 'mleko'))

# Zadanie 7
print('\nZadanie 7')

def zad_7(**slownik):
    if(len(slownik) == 0):
        return 0
    else:
        suma = 0
        for i in slownik:
            suma += slownik[i]
        return suma

print('zad_7(a = 42, b = 12, c = 54, d = 41, e = 213, f = 31) = ', end='')
print(zad_7(a = 42, b = 12, c = 54, d = 41, e = 213, f = 31))