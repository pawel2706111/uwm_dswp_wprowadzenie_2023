# Wprowadzenie do języka Python
# Paweł Majorowski
# 155090
# Grupa 2

# zadanie 1
print('zadanie 1')
int_1 = 10
int_2 = int('47', base=8)
print('\tint 1:', int_1)
print('\tint 2:', int_2)

float_1 = 0.2 + 0.1
float_2 = float('0.357')
print('\tfloat 1:', float_1)
print('\tfloat 2:', float_2)

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
print('\nzadanie 3')