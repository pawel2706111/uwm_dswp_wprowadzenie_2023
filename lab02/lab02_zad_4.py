# Wprowadzenie do języka Python
# Paweł Majorowski
# 155090
# Grupa 2
# lab 02
#
# zadanie 4

# Wycięcie z napisu pierwszych pięciu liter
print('wycięcie z napisu abcdefg trzech pierwszych liter:')
print(f'{"abcdefg":.3}')

# Znak liczby (domyślnie znak + nie jest wyświetlany, tylko - jest wyświetlany)
print('\nwyświetlanie znaku liczby:')
liczba = 5
print(f'{liczba:+d}')
print(f'{-liczba:+d}')

# wyrównanie do środka
print('\nwyrówanie do środka:')
print('+' + '-' * 18 + '+')
print(f'+{"nazwa kolumny":^18}+')
print('+' + '-' * 18 + '+')

# formatowanie daty
from datetime import datetime

print('\nformatowanie daty:')
print(f'teraz: {datetime.now():%d %m %y %H:%M}')

# użycie słownika

auto = {'marka': 'Mercedes',
        'model': 'SLS'}

print('\nUżycie słownika:')
print(f'{auto["marka"]} {auto["model"]}')