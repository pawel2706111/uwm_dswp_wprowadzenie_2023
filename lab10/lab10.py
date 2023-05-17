# Wprowadzenie do języka Python
# Paweł Majorowski
# 155090
# Grupa 2
# lab 10
# Zadanie 1
print('\nZadanie 1')
import os

def zadanie_1(lista_sciezek):
    for sciezka in lista_sciezek:
        if(os.path.exists(sciezka)):
            print(f'Folder "{sciezka}" istnieje')
        else:
            print(f'Folder "{sciezka}" NIE istnieje')
            try:
                os.makedirs(sciezka)
                print(f'Utworzono folder "{sciezka}"')
            except OSError as e:
                print(f'Nie udało się utworzyć folderu "{sciezka}" z powodu błędu: {e}')

zadanie_1(['data_for_lab_10', 'jakis_folder', 'D:/aaa_zupelnie_nowy_folder'])

# Zadanie 2
print('\nZadanie 2')

def zadanie_2(sciezka_do_folderu):
    wynik = open('wynik.txt', 'w')
    sciezka, nazwy_folderow, nazwy_plikow = next(os.walk(sciezka_do_folderu, topdown=False))
    sciezka_do_pliku = sciezka + '\\' + nazwy_plikow[0]
    with open(sciezka_do_pliku, 'r') as plik:
        naglowek = plik.readline()
        wynik.write(naglowek)
    for sciezka, nazwy_folderow, nazwy_plikow in os.walk(sciezka_do_folderu):
        for nazwa_pliku in nazwy_plikow:
            sciezka_do_pliku = sciezka + '\\' + nazwa_pliku
            with open(sciezka_do_pliku, 'r') as plik:
                plik.readline()
                tekst = plik.readlines()
                wynik.writelines(tekst)
    wynik.close()

zadanie_2('data_for_lab_10')

# Zadanie 3
from datetime import datetime
from zoneinfo import ZoneInfo

print('\nZadanie 3')

def zadanie_3():
    format = '%H:%M:%S'
    czas = input('Podaj czas w formacie "HH:MM:SS": ')
    czas = datetime.strptime(czas, format).replace(tzinfo=ZoneInfo('Poland'))
    czas = datetime.now().replace(hour=czas.hour, minute=czas.minute, second=czas.second, microsecond=0)
    print('Tokio -', czas.astimezone(ZoneInfo('Asia/Tokyo')).strftime(format))
    print('Waszyngton -', czas.astimezone(ZoneInfo('Etc/GMT+4')).strftime(format))
    print('Sydney -', czas.astimezone(ZoneInfo('Australia/Sydney')).strftime(format))
    print('Londyn -', czas.astimezone(ZoneInfo('Europe/London')).strftime(format))

zadanie_3()

# Zadanie 4
from dateutil import relativedelta
print('\nZadanie 4')

def zadanie_4(data_urodzenia):
    dzis = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    nastepne_urodziny = datetime(dzis.year, data_urodzenia.month, data_urodzenia.day)
    if(nastepne_urodziny <= dzis):
        nastepne_urodziny = nastepne_urodziny.replace(year=dzis.year+1)
    Z = relativedelta.relativedelta(dzis, data_urodzenia)
    X = Z.years
    Y = Z.months
    Z = Z.days
    N = (nastepne_urodziny - dzis).days
    print(f'Dzisiaj masz {X} lat, {Y} miesięcy i {Z} dni. Do twoich kolejnych urodzin pozostało {N} dni.')

zadanie_4(datetime(2000, 6, 27))

# Zadanie 5
print('\nZadanie 5')

def zadanie_5(nazwa_pliku_zrodlowego, nazwa_pliku_docelowego, indeks_kolumny, format_zrodlowy, format_docelowy):
    plik_zrodlowy = open(nazwa_pliku_zrodlowego, 'r')
    plik_docelowy = open(nazwa_pliku_docelowego, 'w')
    plik_docelowy.write(plik_zrodlowy.readline())
    for linia in plik_zrodlowy:
        linia = linia.split(',')
        data = datetime.strptime(linia[indeks_kolumny], format_zrodlowy)
        linia[indeks_kolumny] = data.strftime(format_docelowy)
        plik_docelowy.write(','.join(linia))
    plik_zrodlowy.close()
    plik_docelowy.close()
    print(f'Utworzono plik "{nazwa_pliku_docelowego}"')

zadanie_5('wynik.txt', 'zad_5.txt', 2, '%Y%m%d', '%Y-%m-%d')