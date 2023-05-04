# Wprowadzenie do języka Python
# Paweł Majorowski
# 155090
# Grupa 2
# lab 08
#
# Zadanie 1
from timeit import timeit

def zadanie_1():
    setup = 'from array import array\n'
    setup += 'import random\n'
    setup += 'lista_liczb = [random.randint(32, 126) for i in range(0, 100000)]\n'
    setup += 'lista_znakow = [chr(znak) for znak in lista_liczb]'

    tablica_int = '''tablica_int = array('i', lista_liczb)'''
    tablica_long = '''tablica_long = array('l', lista_liczb)'''
    tablica_char = '''tablica_char = array('u', lista_znakow)'''
    lista_liczb = '''lista = [i for i in lista_liczb]'''
    lista_znakow = '''lista = [i for i in lista_znakow]'''

    czas_int = timeit(tablica_int, setup, number=100)
    czas_long = timeit(tablica_long, setup, number=100)
    czas_char = timeit(tablica_char, setup, number=100)
    czas_lista_liczb = timeit(lista_liczb, setup, number=100)
    czas_lista_znakow = timeit(lista_znakow, setup, number=100)

    print('Czasy (w sekundach):')
    print('\t- Int:', czas_int)
    print('\t- Long:', czas_long)
    print('\t- Char:', czas_char)
    print('\t- Lista_liczb:', czas_lista_liczb)
    print('\t- Lista znaków:', czas_lista_znakow)

print('Zadanie 1')
zadanie_1()

# Zadanie 2
import datetime
from array import array
import random

def zadanie_2():
    czas = {'tablica': {'zapis': {'start': 0, 'end': 0},
                        'odczyt': {'start': 0, 'end': 0}},
            'lista': {'zapis': {'start': 0, 'end': 0},
                        'odczyt': {'start': 0, 'end': 0}}}
    # zapisanie tablicy do pliku oraz jej wczytanie
    lista = [random.random() for _ in range(1000000)]
    czas['tablica']['zapis']['start'] = datetime.datetime.now()
    tab_of_floats = array('f', lista)
    with open('floats_array.bin', 'wb') as file_arr:
        tab_of_floats.tofile(file_arr)
    czas['tablica']['zapis']['end'] = datetime.datetime.now()

    # wczytujemy ponownie dane do tablicy floatów
    czas['tablica']['odczyt']['start'] = datetime.datetime.now()
    tab_of_floats_loaded = array('f')
    file_arr  = open('floats_array.bin', 'rb')
    tab_of_floats_loaded.fromfile(file_arr, 1000000)
    file_arr.close()
    czas['tablica']['odczyt']['end'] = datetime.datetime.now()


    # i analogiczna operacja dla listy
    czas['lista']['zapis']['start'] = datetime.datetime.now()
    list_of_floats = [i for i in lista]
    with open('floats_list.txt', 'w') as file_arr:
        file_arr.writelines('\n'.join([str(x) for x in list_of_floats]))
    czas['lista']['zapis']['end'] = datetime.datetime.now()

    czas['lista']['odczyt']['start'] = datetime.datetime.now()
    with open('floats_list.txt', 'r') as file_list:
        list_of_floats_loaded = file_list.readlines()
    list_of_floats_loaded = [float(x.strip()) for x in list_of_floats_loaded]
    czas['lista']['odczyt']['end'] = datetime.datetime.now()

    for i in czas.keys():
        for j in czas[i].keys():
            czas[i][j]['czas wykonania'] = czas[i][j]['end'] - czas[i][j]['start']

    print('Czas wykonania:')
    print('\t- zapis tablicy flotów do pliku:', czas['tablica']['zapis']['czas wykonania'])
    print('\t- odczyt tablicy flotów z pliku:', czas['tablica']['odczyt']['czas wykonania'])
    print('\t- zapis listy flotów do pliku:  ', czas['lista']['zapis']['czas wykonania'])
    print('\t- odczyt listy flotów z pliku:  ', czas['lista']['odczyt']['czas wykonania'])

    zapis_ile_szybszy = czas['lista']['zapis']['czas wykonania'] / czas['tablica']['zapis']['czas wykonania']
    print(f'Zapis tablicy do pliku jest {zapis_ile_szybszy:.2f} raza szybszy od zapisu listy do pliku')
    odczyt_ile_szybszy = czas['lista']['odczyt']['czas wykonania'] / czas['tablica']['odczyt']['czas wykonania']
    print(f'Odczyt tablicy do pliku jest {odczyt_ile_szybszy:.2f} raza szybszy od odczytu listy do pliku')
    print('Wnioski: Używanie tablicy jest zdecydowanie szybsze od używania list')

print('\nZadanie 2')
zadanie_2()

# Zadanie 3

def zadanie_3():
    setup =  'from collections import deque, namedtuple, Counter\n'
    setup += 'kolejka = deque("Ala ma kota".split())\n'
    setup += 'lista = "Ala ma kota".split()'
    kolejka_append = 'kolejka.append("xd")'
    kolejka_appendleft = 'kolejka.appendleft("xd")'
    lista_append = 'lista.append("xd")'
    lista_insert_zero = 'lista.insert(0, "xd")'
    czas_kolejka_append = timeit(kolejka_append, setup, number=100000)
    czas_kolejka_appendleft = timeit(kolejka_appendleft, setup, number=100000)
    czas_lista_append = timeit(lista_append, setup, number=100000)
    czas_lista_insert_zero = timeit(lista_insert_zero, setup, number=100000)
    print(f'Czas wykonania append dla kolejki wyniósł {czas_kolejka_append} sekund')
    print(f'Czas wykonania appendleft dla kolejki wyniósł {czas_kolejka_appendleft} sekund')
    print(f'Czas wykonania append dla listy wyniósł {czas_lista_append} sekund')
    print(f'Czas wykonania insert(0) dla listy wyniósł {czas_lista_insert_zero} sekund')
    print(f'Append dla kolejki jest {czas_lista_append/czas_kolejka_append} raza szybszy, niż append dla listy')
    print(f'Appendleft dla kolejki jest {czas_lista_insert_zero/czas_kolejka_appendleft} raza szybszy, niż insert(0) dla listy')

print('\nZadanie 3')
zadanie_3()

# Zadanie 4
from collections import deque, namedtuple, Counter

def zadanie_4():
    with open('zamowienia.txt', 'r', encoding='ANSI', newline='') as plik:
        nazwy_kolumn = plik.readline()
        nazwy_kolumn = nazwy_kolumn.replace('\n', '')
        nazwy_kolumn = nazwy_kolumn.split(';')
        nazwy_kolumn = [nazwa.replace(' ', '_') for nazwa in nazwy_kolumn]
        Rekord = namedtuple('Rekord', nazwy_kolumn)
        rekordy = []
        for _ in range(0, 10):
            rekord = plik.readline().replace('\n', '')
            rekord = rekord.split(';')
            rekordy.append(Rekord._make(rekord))
    print('Pierwsze 10 rekordów:')
    for rekord in rekordy:
        print(rekord)

print('\nZadanie 4:')
zadanie_4()

# Zadanie 5

# funkcję, która z tablicy wartości liczbowych zwraca 10% najwyższych wartości
def max_10_procent(tablica):
    tablica = sorted(tablica)
    return tablica[-(len(tablica)//10):]

def zadanie_5():
    lista_liczb = [random.randint(0, 10000) for i in range(0, 200)]
    tablica = array('i', lista_liczb)
    print('Tablica liczb:')
    print(tablica)
    print('\n10% najwyższych wartości:')
    print(max_10_procent(tablica))

print('\nZadanie 5:')
zadanie_5()

# Zadanie 6

def create_kolo_fortuny(*args):
    counter = Counter(args)
    counter = counter.elements()
    return deque(counter)

def zadanie_6():
    args = range(1, 11)
    kolo_fortuny = create_kolo_fortuny(*args)
    print(kolo_fortuny)

print('\nZadanie 6:')
zadanie_6()

# Zadanie 7
import time

def spinit(kolo_fortuny):
    stop = kolo_fortuny[0]
    o_ile_obracac = random.randint(0, len(kolo_fortuny))
    czy_jeszcze_nie_zakrecono = True
    while(kolo_fortuny[0] != stop or czy_jeszcze_nie_zakrecono):
        czy_jeszcze_nie_zakrecono = False
        kolo_fortuny.rotate(o_ile_obracac)
        print(kolo_fortuny, end='')
        time.sleep(0.5)
        print('\r', end='')
    print(kolo_fortuny)

def zadanie_7():
    args = list(range(1, 10))
    random.shuffle(args)
    kolo_fortuny = create_kolo_fortuny(*args)
    print('Koło fortuny przed zakręceniem:')
    print(kolo_fortuny)
    print('Aktualny stan koła fortuny:')
    spinit(kolo_fortuny)

print('\nZadanie 7:')
zadanie_7()