# Wprowadzenie do języka Python
# Paweł Majorowski
# 155090
# Grupa 2
# lab 02
#
# zadanie 4

# dodawanie pod kreską


liczba_1 = '234'
liczba_2 = '135'
kreska = '+ ' + '-' * len(liczba_1)

nowy_format = '{:>'+str(len(kreska))+'}'
print(nowy_format.format(liczba_1))
print(nowy_format.format(liczba_2))
print(kreska)
print(nowy_format.format(str(int(liczba_1)+int(liczba_2))))
