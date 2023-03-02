# Wprowadzenie do języka Python
# Paweł Majorowski
# 155090
# Grupa 2
# zadanie 1

dane = input('Podaj linię danych: ')
separator_zrodlowy = input('Podaj separator źródłowy: ')
separator_docelowy = input('Podaj separator docelowy: ')

nowe_dane = dane.split(separator_zrodlowy)
nowe_dane = separator_docelowy.join(nowe_dane)
print('Wprowadzone dane po użyciu metod split i join:')
print(nowe_dane)

# można to zrobić prościej
# do zamiany jednego znaku na inny w stringu, najłatwiej jest użyć metody replace

nowe_dane = dane.replace(separator_zrodlowy, separator_docelowy)
print('Wprowadzone dane po użyciu metody replace:')
print(nowe_dane)

# zadanie 2
lipsum = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'
