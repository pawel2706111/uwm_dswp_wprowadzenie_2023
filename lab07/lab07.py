# Wprowadzenie do języka Python
# Paweł Majorowski
# 155090
# Grupa 2
# lab 07
#
# Zadanie 1
print('\nZadanie 1:')

def extract_numbers(vals: list[any]) -> list[int | float]:
    return list(filter(lambda x: isinstance(x, (int, float)), vals))

print('Lista przed filtrowaniem:')
vals = [1, 2.5, 'xdas', 3.5, 'asdas', 2]
print(vals)
print('Lista po filtrowaniu:')
print(extract_numbers(vals))

# Zadanie 2
print('\nZadanie 2:')
wyrazy = input('Podaj wyrazy oddzielając je spacją: ')
wyrazy = wyrazy.split(' ')
print('Lista wyrazów przed posortowaniem:')
print(wyrazy)
print('Lista wyrazów po posortowaniu:')
wyrazy = sorted(wyrazy, key = lambda x: len(x), reverse=True)
print(wyrazy)

# Zadanie 3
print('\nZadanie 3:')

def zadanie_3(lista, reversed=False):
    inty = list(filter(lambda x: isinstance(x, int), lista))
    stringi = list(filter(lambda x: isinstance(x, str), lista))
    inty = sorted(inty)
    stringi = sorted(stringi)
    if(reversed):
        return stringi + inty
    else:
        return inty + stringi
    
lista = [3, 'abc', 5, 1, 'bcd']

print('lista nieposortowana:')
print(lista)
print('Lista posortowana dla domyślnej wartości atrybutu reversed:')
print(zadanie_3(lista))
print('Lista posortowana dla atrybutu reversed o wartości True:')
print(zadanie_3(lista, True))

# Zadanie 4
print('\nZadanie 4:')
import csv
import datetime

zamowienia = ''

with open('zamowienia.csv', encoding='ANSI') as file_reader:
    zamowienia = csv.DictReader(file_reader, delimiter=';')
    zamowienia = list(zamowienia)

def utarg(slownik):
    slownik['Utarg'] = slownik['Utarg'].replace('\x88', '')
    slownik['Utarg'] = slownik['Utarg'].replace('z', '')
    slownik['Utarg'] = slownik['Utarg'].replace(' ', '')
    slownik['Utarg'] = slownik['Utarg'].replace(',', '')
    return slownik

def data(slownik):
    data = slownik['Data zamowienia']
    data = datetime.datetime.strptime(data, '%d.%m.%Y')
    data = data.strftime('%Y.%m.%d')
    slownik['Data zamowienia'] = data
    return slownik

zamowienia = list(map(utarg, zamowienia))
zamowienia = list(map(data, zamowienia))

zamowienia_polska = []
zamowienia_niemcy = []

zamowienia_polska = list(filter(lambda x: x['Kraj'] == 'Polska', zamowienia))
zamowienia_niemcy = list(filter(lambda x: x['Kraj'] == 'Niemcy', zamowienia))

with open('zamowienia_polska.csv', 'w', encoding='ANSI', newline='') as file_reader:
    kolumny = list(zamowienia_polska[0].keys())
    writer = csv.DictWriter(file_reader, fieldnames=kolumny)
    writer.writeheader()
    writer.writerows(zamowienia_polska)

with open('zamowienia_niemcy.csv', 'w', encoding='ANSI', newline='') as file_reader:
    kolumny = list(zamowienia_niemcy[0].keys())
    writer = csv.DictWriter(file_reader, fieldnames=kolumny)
    writer.writeheader()
    writer.writerows(zamowienia_niemcy)

print('Utworzono pliki "zamowienia_polska.csv" oraz "zamowienia_niemcy.csv"')

# Zadanie 5
print('\nZadanie 5:')

# abs - najmniejsza wartość bezwzględna

def zadanie_5(slownik, funkcja):
    if (funkcja != abs):
        return sorted(slownik.items(), key = lambda x: funkcja(x[1]))
    else:
        return sorted(slownik.items(), key = lambda x: min(map(abs, x[1])))

slownik = {'Marek': [-10, 40],
           'Mateusz': [13, 16],
           'Łukasz': [25, 35],
           'Jan': [20, 30]}

print('Słownik przed posortowaniem:')
print(slownik)
print('Słownik po posortowaniu według min:')
print(zadanie_5(slownik, min))
print('Słownik po posortowaniu według max:')
print(zadanie_5(slownik, max))
print('Słownik po posortowaniu według sum:')
print(zadanie_5(slownik, sum))
print('Słownik po posortowaniu według abs:')
print(zadanie_5(slownik, abs))

print('\nStatystki dla sprawdzenia poprawności działania zadania 5:\n')
print(' '*5, end='')
for i in slownik.keys():
    print(f'|{i:^20}', end='')
print('|')
print(' '*5, end='')
for i in slownik.keys():
    print('+'+'-'*20, end='')
print('+')
print('min  ', end='')
for i in slownik.values():
    print(f'|{min(i):^20}', end='')
print('|')
print('max  ', end='')
for i in slownik.values():
    print(f'|{max(i):^20}', end='')
print('|')
print('sum  ', end='')
for i in slownik.values():
    print(f'|{sum(i):^20}', end='')
print('|')
print('abs  ', end='')
for i in slownik.values():
    print(f'|{min(map(abs, i)):^20}', end='')
print('|')
print(' '*5, end='')
for i in slownik.keys():
    print('+'+'-'*20, end='')
print('+')