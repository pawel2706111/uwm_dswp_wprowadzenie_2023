# Wprowadzenie do języka Python
# Paweł Majorowski
# 155090
# Grupa 2
# lab 04
#
# import potrzebnych bibliotek
import this
import sys
import random

# zadanie 1

print('\nZadanie 1')
liczba = int(input('Podaj liczbę całkowitą: '))
print(f'Liczba {liczba}:')
print(f'\t- ma postać {bin(liczba)} w systemie binarnym')
print(f'\t- ma postać {oct(liczba)} w systemie oktalnym')
print(f'\t -ma postać {hex(liczba)} w systemie heksadecymalnym')

# zadanie 2
print('\nZadanie 2')
i = input('Podaj jakąś wartość i: ')

try:
    int(i)
    print(f'Podana wartość jest rzutowalna na typ int')
except:
    print(f'Podana wartość NIE jest rzutowalna na typ int')

try:
    float(i)
    print(f'Podana wartość jest rzutowalna na typ float')
except:
    print(f'Podana wartość NIE jest rzutowalna na typ float')

# zadanie 3
print('\nZadanie 3')

sys.stdout.write('Podaj liczbę:\n')
liczba = sys.stdin.readline()
liczba = int(liczba)
cyfry = []
mnoznik = 1
for i in range(0, len(str(liczba))):
    cyfry.append(liczba % 10)
    liczba = liczba // 10
    mnoznik = mnoznik * 10
cyfry.reverse()
mnoznik = mnoznik // 10

sys.stdout.write('Podaną liczbę można zapisać jako: ')
sys.stdout.write(str(mnoznik)+' * '+str(cyfry[0]))
cyfry.remove(cyfry[0])
for cyfra in cyfry:
    mnoznik = mnoznik // 10
    if(cyfry != 0):
        sys.stdout.write(' + '+str(mnoznik)+' * '+str(cyfra))
sys.stdout.write('\n')

# zadanie 4
print('\nZadanie 4')

wiadomosc_do_zaszyfrowania = input("Podaj tekst do zaszyfrowania: ")

zaszyfrowana_wiadomosc = ''
for znak in wiadomosc_do_zaszyfrowania:
    try:
        zaszyfrowana_wiadomosc = zaszyfrowana_wiadomosc + this.d[znak]
    except:
        zaszyfrowana_wiadomosc = zaszyfrowana_wiadomosc + znak

print('Wiadomość przed zaszyfrowaniem:')
print(wiadomosc_do_zaszyfrowania)
print('Wiadomość po zaszyfrowaniu:')
print(zaszyfrowana_wiadomosc)

# zadanie 5
print('\nZadanie 5')
zdanie = input('Podaj zdanie: ')
zdanie = zdanie.split(" ")
zdanie.sort(key=len)
print('Wyrazy z podanego zdania posortowane według ich długości rosnąco:')
for i in zdanie:
    print('-', i)

# zadanie 6
print('\nZadanie 6')

kolumna_1 = ['Koleżanki i koledzy ',
             'Z drugiej strony ',
             'Podobnie ',
             'Nie zapominajmy jednak, że ',
             'W ten oto sposób ',
             'Praktyka dnia codziennego dowodzi, że ',
             'Wagi i znaczenia tych problemów nie trzeba szerzej uzasadniać, ponieważ ',
             'Różnorakie i bogate doświadczenia ',
             'Troska organizacji, a szczególnie ',
             'Wyższe założenia ideowe, a także ']

kolumna_2 = ['realizacja nakreślonych zadań programowych ',
             'zakres i miejsce szkolenia kadr ',
             'stały wzrost ilości i zakres naszej aktywności ',
             'aktualna struktura organizacji ',
             'nowy model działalności organizacyjnej ',
             'dalszy rozwój różnych form działalności ',
             'stałe zabezpieczenie informacyjno programowe naszej działalności ',
             'wzmacnianie i rozwijanie struktur ',
             'konsultacja z szerokim aktywem ',
             'rozpoczęcie powszechnej akcji kształtowania postaw ']

kolumna_3 = ['zmusza nas do przeanalizowania ',
             'spełnia istotną rolę w kształtowaniu ',
             'wymaga sprecyzowania i określenia ',
             'pomaga w przygotowaniu i realizacji ',
             'zabezpiecza udział szerokiej grupie w kształtowaniu ',
             'spełnia ważne zadania w wypracowaniu ',
             'umożliwia w większym stopniu tworzenie ',
             'powoduje docenianie wagi ',
             'przedstawia intersującą próbę sprawdzenia ',
             'pociąga za sobą proces wdrażania i unowocześniania ']

kolumna_4 = ['istniejących warunków administracyjno-finansowych. ',
             'dalszych kierunków rozwoju. ',
             'systemu powszechnego uczestnictwa. ',
             'postaw uczestników wobec zadań stawianych przez organizację. ',
             'nowych propozycji. ',
             'kierunków postępowego wychowania. ',
             'systemu szkolenia kadry odpowiadającego potrzebom. ',
             'odpowiednich waruknków aktywizacji. ',
             'modelu rozwoju. ',
             'form oddziaływania. ']

kolumny = [kolumna_1, kolumna_2, kolumna_3, kolumna_4]
indeks_ostatniego_zdania_w_kolumnie = len(kolumna_1) - 1

liczba_zdan = int(input('Podaj ile zdań ma wygenerować program: '))

for i in range(0, liczba_zdan+1):
    zdanie = ''
    for numer_kolumny in range(0, 4):
        losowe_zdanie = random.randint(0, indeks_ostatniego_zdania_w_kolumnie)
        zdanie = zdanie + kolumny[numer_kolumny][losowe_zdanie]
    print(i, zdanie, sep=' - ')