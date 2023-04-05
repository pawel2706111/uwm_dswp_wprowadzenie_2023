# Wprowadzenie do języka Python
# Paweł Majorowski
# 155090
# Grupa 2
# lab 06
#
# Zadanie 1
import csv
import datetime
print('Zadanie 1')

zamowienia = ''

with open('zamowienia.csv', encoding='ANSI') as file_reader:
    zamowienia = csv.DictReader(file_reader, delimiter=';')
    zamowienia = list(zamowienia)

zamowienia_polska = []
zamowienia_niemcy = []

for i in range(0, len(zamowienia)):
    zamowienia[i]['Utarg'] = zamowienia[i]['Utarg'].replace('\x88', '')
    zamowienia[i]['Utarg'] = zamowienia[i]['Utarg'].replace('z', '')
    zamowienia[i]['Utarg'] = zamowienia[i]['Utarg'].replace(' ', '')
    zamowienia[i]['Utarg'] = zamowienia[i]['Utarg'].replace(',', '')
    data = zamowienia[i]['Data zamowienia']
    data = datetime.datetime.strptime(data, '%d.%m.%Y')
    data = data.strftime('%Y.%m.%d')
    zamowienia[i]['Data zamowienia'] = data
    if(zamowienia[i]['Kraj'] == 'Polska'):
        zamowienia_polska.append(zamowienia[i])
    else:
        zamowienia_niemcy.append(zamowienia[i])

with open('zamowienia_polska.csv', 'w', encoding='ANSI', newline='') as file_reader:
    kolumny = list(zamowienia_polska[0].keys())
    writer = csv.DictWriter(file_reader, fieldnames=kolumny)
    writer.writeheader()
    for i in zamowienia_polska:
        writer.writerow(i)

with open('zamowienia_niemcy.csv', 'w', encoding='ANSI', newline='') as file_reader:
    kolumny = list(zamowienia_niemcy[0].keys())
    writer = csv.DictWriter(file_reader, fieldnames=kolumny)
    writer.writeheader()
    for i in zamowienia_niemcy:
        writer.writerow(i)

print('Utworzono pliki "zamowienia_polska.csv" oraz "zamowienia_niemcy.csv"')

# Zadanie 2
print('\nZadanie 2')

def zadanie_2(lista_plikow, plik_wynikowy):
    plik_wynikowy = open(plik_wynikowy, 'w')
    for plik in lista_plikow:
        with open(plik, 'r') as f:
            plik_wynikowy.write(f.read())
            plik_wynikowy.write('\n')
    plik_wynikowy.close()

lista_plikow = ['zadanie_2_a.txt', 'zadanie_2_b.txt', 'zadanie_2_c.txt']
plik_wynikowy = 'zadanie_2_output.txt'
zadanie_2(lista_plikow, plik_wynikowy)

# Zadanie 3
import random
print('\nZadanie 3')

def zadanie_3(lista_numeryczna, n, najwieksze):
    liczby = []
    for i in lista_numeryczna:
        if(type(i) == int or type(i) == float):
            liczby.append(i)
    if(len(liczby) <= n):
        return liczby
    liczby.sort()
    if(najwieksze):
        return liczby[0:n]
    else:
        return liczby[-n:]

lista_numeryczna = [random.randint(0, 100) for i in range(0, 20)]
print(lista_numeryczna)
print('Największe 5 liczb to:', zadanie_3(lista_numeryczna, 5, True))
print('Najmniejsze 5 liczb to:', zadanie_3(lista_numeryczna, 5, False))

# Zadanie 4
print('\nZadanie 4')

def zadanie_4(mieszana):
    slownik = {}
    for element in mieszana:
        typ = element.__class__.__name__
        if(typ in slownik.keys()):
            slownik[typ].append(element)
        else:
            slownik[typ] = [element]
    return slownik

mieszana = [1, 2.3, 'Zbyszek', 5, 'Marian', 3.0]
print(zadanie_4(mieszana))

# Zadanie 5
print('\nZadanie 5')

def zadanie_5(nazwiska):
    nazwiska.sort()
    indeks = None
    for i in range(0, len(nazwiska)):
        if(nazwiska[i].upper() >= 'N'):
            indeks = i
            break
    with open('A-M_nazwiska.txt', 'w', encoding='utf-8') as file_reader:
        for nazwisko in nazwiska[:indeks]:
            file_reader.write(nazwisko+'\n')
    with open('N-Ż_nazwiska.txt', 'w', encoding='utf-8') as file_reader:
            for nazwisko in nazwiska[indeks:]:
                file_reader.write(nazwisko+'\n')
    print('Utworzono pliki "A-M_nazwiska.txt" oraz "N-Ż_nazwiska.txt"')

nazwiska = ['Adamska', 'Włodarczyk', 'Włodarczyk', 'Czerwiński', 'Kołodziej', 'Szewczyk', 'Duda', 'Brzeziński', 'Wiśniewski', 'Stępień', 'Krawczyk', 'Baranowski', 'Szymański', 'Maciejewski', 'Czarnecki', 'Zawadzki', 'Kucharski', 'Kubiak', 'Zawadzki', 'Tomaszewski', 'Pietrzak', 'Zalewski', 'Michalak', 'Walczak', 'Marciniak', 'Mazur', 'Mazur', 'Szymczak', 'Dąbrowski', 'Kalinowski', 'Nowak']
zadanie_5(nazwiska)

# Zadanie 6
print('\nZadanie 6')

def zadanie_6(napis):
    napis = napis.split(' ')
    napis = [i[::-1] for i in napis]
    napis = ' '.join(napis)
    print(napis)

napis = 'Ala ma kota'
zadanie_6(napis)

# Zadanie 7
import random
print('\nZadanie 7')

def zadanie_7(gracze):
    figury = [str(i) for i in range(2, 11)]
    figury.extend(['Walet', 'Dama', 'Król', 'As'])
    kolory = ['pik', 'kier', 'trefl', 'karo']
    talia_kart = [figura+' '+kolor for figura in figury for kolor in kolory]
    # tasowanie tali
    random.shuffle(talia_kart)
    # rozdanie kart
    reka_kazdego_gracza = {}
    for i in range(0, len(gracze)):
        reka_kazdego_gracza[gracze[i]] = talia_kart[i:5*len(gracze)+i:5]
    for i in reka_kazdego_gracza:
        print(i, reka_kazdego_gracza[i])

gracze = ['James Bond', 'Le Chiffre', 'Danny Ocean', 'Cincinnati Kid']
zadanie_7(gracze)

# Zadanie 8
from unidecode import unidecode
print('\nZadanie 8')

def zadanie_8(sciezka_input, sciezka_output, domena):
    lista_imion = []
    with open(sciezka_input, 'r', encoding='utf-8') as file_reader: 
        for linia in file_reader:
            lista_imion.append(linia.replace('\n', ''))
    lista_email = []
    for imie in lista_imion:
        email = imie.replace(' ', '.')
        email = unidecode(email)
        email = email.lower()
        email = email + domena
        lista_email.append(email)
    with open(sciezka_output, 'w', encoding='utf-8') as file_reader:
        for i in range(0, len(lista_imion)):
            linia = lista_imion[i] + ' ' + lista_email[i] + '\n'
            file_reader.write(linia)
    
zadanie_8('zadanie_8_input.txt', 'zadanie_8_output.txt', '@student.uwm.edu.pl')

# Zadanie 9
import random
print('\nZadanie 9')

hasla = []

with open('zadanie_9_input.txt', 'r', encoding='utf-8') as file_rearder:
    for i in file_rearder:
        hasla.append(i.replace('\n', ''))

haslo = hasla[random.randint(0, len(hasla)-1)]

ukryte_haslo = haslo.split(' ')
for i in range(0, len(ukryte_haslo)):
    ukryte_haslo[i] = '_' * len(ukryte_haslo[i])
ukryte_haslo = ' '.join(ukryte_haslo)

litery = set(haslo.lower())
litery.remove(' ')

slownik = {}
for litera in litery:
    indeksy = []
    for indeks in range(0, len(haslo)):
        if(haslo[indeks].lower() == litera):
            indeksy.append(indeks)
    slownik[litera] = indeksy

ukryte_haslo = list(ukryte_haslo)

print('Aby było łatwiej testować program hasło to: \"'+haslo+'\"\n')

czy_dalej_haslo_jest_zasloniete = True
while(czy_dalej_haslo_jest_zasloniete):
    print(''.join(ukryte_haslo))
    litera = input('Podaj literę: ')
    if(len(litera) == 1):
        if(litera in slownik):
            for i in slownik[litera]:
                ukryte_haslo[i] = haslo[i]
        else:
            print('Podana litera nie znajduje się w haśle')
    if(len(litera) > 1):
        if(litera.lower() == haslo.lower()):
            czy_dalej_haslo_jest_zasloniete = False
        else:
            print('Niestety! To nie jest to hasło. Próbuj dalej')
    print()
    if(''.join(ukryte_haslo).find('_') == -1):
        czy_dalej_haslo_jest_zasloniete = False

print('Gratulację! odgadłeś całe hasło')