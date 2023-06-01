# Wprowadzenie do języka Python
# Paweł Majorowski
# 155090
# Grupa 2
# lab 11
# Zadanie 1
import re
print('Zadanie 1')

def zadanie_1():
    strings = ''
    with open('strings.txt', 'r', encoding='utf-8') as plik:
        strings = plik.read()
    # wszystkie liczby
    wszystkie_liczby = r'\d+'
    # wszystkie liczby co najmniej 3 cyfrowe
    liczby_co_najmniej_3_cyfrowe= 3*'\d'+'+'
    # wszystkie adresy IPv4
    ipv4 = r'\d+.\d+.\d+.\d'
    # wszystkie wyrazy rozpoczynające się od wielkiej litery
    wyrazy_od_wielkiej_litery = r'[A-Z]\w+'
    # wszystkie linie z pliku, które mają co najmniej 4 wyrazy
    linie_co_maja_4_lub_wiecej_wyrazow = r'.+\s.+\s.+\s.+\n'
    # wszystkie adresy url
    adresy_url = r'[https://|http://].+[/]'
    print('wszystkie liczby:')
    wzor = re.compile(wszystkie_liczby)
    print(re.findall(wzor, strings))
    print('wszystkie liczby co najmniej 3 cyfrowe:')
    wzor = re.compile(liczby_co_najmniej_3_cyfrowe)
    print(re.findall(wzor, strings))
    print('wszystkie adresy IPv4:')
    wzor = re.compile(ipv4)
    print(re.findall(wzor, strings))
    print('wszystkie wyrazy rozpoczynające się od wielkiej litery:')
    wzor = re.compile(wyrazy_od_wielkiej_litery)
    print(re.findall(wzor, strings))
    print('wszystkie linie z pliku, które mają co najmniej 4 wyrazy:')
    wzor = re.compile(linie_co_maja_4_lub_wiecej_wyrazow)
    print(re.findall(wzor, strings))
    print('wszystkie adresy url:')
    wzor = re.compile(adresy_url)
    print(re.findall(wzor, strings))

zadanie_1()

# Zadanie 2
import datetime
print('\nZadanie 2')

# Zapisz do pliku csv datę w formacie RRRR-MM-DD HH:mm:ss,
# adres ip w formacie z kropkami,
# usługę/użytkownika bez PID (to wartość numeryczna wewnątrz [])
# i komunikat z cytowaniem (quoting dla csv).

def zadanie_2():
    auth = open('auth.log', 'r')
    csv = open('zadanie_2.csv', 'w')
    data_wzor = '[A-Z][a-z]{2} +\d+ +'+2*'\d+:'+'\d+'
    ip_wzor = 'ip' + 4*'-\d+'
    usluga_bez_pid_wzor = ''
    for linia in auth:
        data = re.findall(data_wzor, linia)
        data = '2023 ' + data[0]
        data = datetime.datetime.strptime(data, '%Y %b %d %H:%M:%S')
        data = data.strftime('%Y-%m-%d %H:%M:%S')
        ip = re.findall(ip_wzor, linia)[0]
        ip = ip[3:].replace('-', '.')
        usluga = re.findall(usluga_bez_pid_wzor, linia)[0]
        komunikat = 'test'
        linia_do_csv = data+';'
        linia_do_csv += ip+';'
        linia_do_csv += usluga+';'
        linia_do_csv += '"""'+ komunikat + '"""\n'
        csv.write(linia_do_csv)
    csv.close()
    auth.close()

zadanie_2()

# Zadanie 3
import pickle
print('\nZadanie 3')

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
        if(not isinstance(inny_obiekt, Point)):
            return False
        if(self.x != inny_obiekt.x):
            return False
        if(self.y != inny_obiekt.y):
            raise False
        return True
    
def zadanie_3():
    punkt = Point(2, 3)
    with open('zad_3', 'wb') as plik:
        pickle.dump(punkt, plik)
    with open('zad_3', 'rb') as plik:
        punkt_z_pliku = pickle.load(plik)
    print('Punkt:', punkt)
    print('Punkt po wczytaniu z pliku:', punkt_z_pliku)
    print('Czy oba obiekty są sobie równe? - ', end='')
    if(punkt == punkt_z_pliku):
        print('tak')
    else:
        print('nie')
    
zadanie_3()

# Zadanie 4
print('\nZadanie 4')

def zadanie_4():
    lista_obiektów = []
    for i in range(0, 6):
        lista_obiektów.append(Point(i, i))
    print('Lista obiektów przed zapisem do pliku: ')
    print(lista_obiektów)
    with open('zad_3', 'wb') as plik:
        pickle.dump(lista_obiektów, plik)
    with open('zad_3', 'rb') as plik:
        lista_obiektów_z_pliku = pickle.load(plik)
    print('Lista obiektów po odczytaniu z pliku: ')
    print(lista_obiektów_z_pliku)


zadanie_4()