# Wprowadzenie do języka Python
# Paweł Majorowski
# 155090
# Grupa 2
# lab 02
#
# zadanie 1
print('Zadanie 1:')
lista = list(range(1, 11))
print('Przed dzieleniem:')
print('oryginalna lista:', lista)

nowa_lista = lista[5:]
lista = lista[:5]

print('\nPo dzieleniu:')
print('oryginalna lista:', lista)
print('nowa lista:', nowa_lista)

# zadanie 2
print('\nZadanie 2:')
lista = [0] + lista + nowa_lista
print('lista:', lista)

# zadanie 3
print('\nZadanie 3:')
napis = input('Podaj tekst: ')
napis = napis.lower()
napis = list(set(napis))
napis.sort()
print('Ciąg unikalnych znaków z wczytanego zdania: ', end='')
print(napis)

# zadanie 4

slownik_pl = {1: 'Styczeń',
           2: 'Luty',
           3: 'Marzec',
           4: 'Kwiecień',
           5: 'Maj',
           6: 'Czerwiec',
           7: 'Lipiec',
           8: 'Sierpień',
           9: 'Wrzesień',
           10: 'Październik',
           11: 'Listopad',
           12: 'Grudzień'}

print('\nZadanie 4:')
print(slownik_pl)

# zadanie 5

print('\nZadanie 5:')

slownik_en = {1: 'January',
              2: 'February',
              3: 'March',
              4: 'April',
              5: 'May',
              6: 'June',
              7: 'July',
              8: 'August',
              9: 'September',
              10: 'October',
              11: 'November',
              12: 'December'}

slownik = {}
slownik['pl'] = slownik_pl
slownik['en'] = slownik_en

for i in range(1, 13):
    print(i, '-' , slownik['pl'][i], '-' , slownik['en'][i])

# Zadanie 6

print('\nZadanie 6:')

napis = 'Marianna'
slownik = dict.fromkeys(napis, 1)

print(slownik)

# Zadanie 7

print('\nZadanie 7:')

import string

napis = input('Podaj jakiś tekst:')
znaki_z_napisu = set(napis.lower())
litery = set(string.ascii_lowercase)
cyfry = set(string.digits)

ile_liter = len(znaki_z_napisu.intersection(litery)) / len(znaki_z_napisu)
ile_cyfr = len(znaki_z_napisu.intersection(cyfry)) / len(znaki_z_napisu)

print(f'Małe litery stanowią {ile_liter * 100:.2f}% podanego tekstu')
print(f'Cyfry litery stanowią {ile_cyfr * 100:.2f}% podanego tekstu')