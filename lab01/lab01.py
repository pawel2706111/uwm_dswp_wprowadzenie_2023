# Wprowadzenie do języka Python
# Paweł Majorowski
# 155090
# Grupa 2

# zadanie 1
print('zadanie 1')
int_1 = 10
int_2 = int('47', base=8)
print('int 1:', int_1)
print('int 2:', int_2)

float_1 = 0.2 + 0.1
float_2 = float('0.357')
print('float 1:', float_1)
print('float 2:', float_2)

# zadanie 2
print('\nzadanie 2')

# int.bit_count()
import random

print('Wykorzystanie int.bit_count()')
print('dec - bin - liczba jedynek')
for i in range(0, 3):
    liczba = random.randint(0, 255)
    print(liczba, bin(liczba), liczba.bit_count(), sep=' - ')

# float.is_integer()
print('\nWykorzystanie float.is_integer()')
floaty = [5.56, 4.7, 3.0]
for i in floaty:
    print('Liczba', i, end=' ')
    if(i.is_integer()):
        print('jest liczbą całkowitą')
    else:
        print('NIE jest liczbą całkowitą')

# zadanie 3

liczba = 0b100010
print('\nzadanie 3')
print(liczba, '-', bin(liczba))
print('najmłodszy bit liczby', int(liczba), 'to', liczba & 1)
print('najstarszy bit liczby', int(liczba), 'to', liczba >> (liczba.bit_length()-1))
print('2 ** 5 =', (1 << 5))
print(' p | q | p ^ q')
print(' 0 | 0 |  ', 0 ^ 0)
print(' 0 | 1 |  ', 0 ^ 1)
print(' 1 | 0 |  ', 1 ^ 0)
print(' 1 | 1 |  ', 1 ^ 1)