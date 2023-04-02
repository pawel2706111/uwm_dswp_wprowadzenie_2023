# Wprowadzenie do języka Python
# Paweł Majorowski
# 155090
# Grupa 2
# lab 06
#
# Zadanie 1
print('Zadanie 1')

# Zadanie 2
print('\nZadanie 2')

# Zadanie 3
print('\nZadanie 3')

# Zadanie 4
print('\nZadanie 4')

mieszana = [1, 2.3, 'Zbyszek', 5, 'Marian', 3.0]
slownik = {}
for element in mieszana:
    typ = element.__class__.__name__
    if(typ in slownik.keys()):
        slownik[typ].append(element)
    else:
        slownik[typ] = [element]

print(slownik)

# Zadanie 5
print('\nZadanie 5')

nazwiska = ['Adamska', 'Włodarczyk', 'Włodarczyk', 'Czerwiński', 'Kołodziej', 'Szewczyk', 'Duda', 'Brzeziński', 'Wiśniewski', 'Stępień', 'Krawczyk', 'Baranowski', 'Szymański', 'Maciejewski', 'Czarnecki', 'Zawadzki', 'Kucharski', 'Kubiak', 'Zawadzki', 'Tomaszewski', 'Pietrzak', 'Zalewski', 'Michalak', 'Walczak', 'Marciniak', 'Mazur', 'Mazur', 'Szymczak', 'Dąbrowski', 'Kalinowski', 'Nowak']
nazwiska.sort()
indeks = None
for i in range(0, len(nazwiska)):
    if(nazwiska[i].upper() >= 'N'):
        print(nazwiska[i].upper() >= 'N')
        indeks = i
        break

with open('A-M_nazwiska.txt', 'w', encoding='utf-8') as file_reader:
    for nazwisko in nazwiska[:indeks]:
        file_reader.write(nazwisko+'\n')

with open('N-Ż_nazwiska.txt', 'w', encoding='utf-8') as file_reader:
        for nazwisko in nazwiska[indeks:]:
            file_reader.write(nazwisko+'\n')

# Zadanie 6
print('\nZadanie 6')

napis = 'Ala ma kota'
napis = napis.split(' ')

napis = [i[::-1] for i in napis]
napis = ' '.join(napis)
print(napis)

# Zadanie 7
import random
print('\nZadanie 7')

figury = [str(i) for i in range(2, 11)]
figury.extend(['Walet', 'Dama', 'Król', 'As'])
kolory = ['pik', 'kier', 'trefl', 'karo']
talia_kart = [figura+' '+kolor for figura in figury for kolor in kolory]
gracze = ['James Bond', 'Le Chiffre', 'Felix Leiter', 'Danny Ocean', 'Cincinnati Kid']

# tasowanie tali
random.shuffle(talia_kart)

# rozdanie kart
reka_kazdego_gracza = {}
for i in range(0, len(gracze)):
    reka_kazdego_gracza[gracze[i]] = talia_kart[i:5*len(gracze)+i:5]

for i in reka_kazdego_gracza:
    print(i, reka_kazdego_gracza[i])

# Zadanie 8
from unidecode import unidecode
print('\nZadanie 8')


def generuj_adresy_email(sciezka_input, sciezka_output, domena):
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
    
generuj_adresy_email('zadanie_8_input.txt', 'zadanie_8_output.txt', '@student.uwm.edu.pl')

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