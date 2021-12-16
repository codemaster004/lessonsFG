################################
#   Python For Kids :) Start   #
################################

# jesli chcemy cos pokazac w koncoli (czarne pudelko takie) przywamy print() i cos co pokazyjemy w srodku
print('Hello World')


###############
#   Zmienne   #
###############

### Na poczatek te latwe

i_am_text = 'Jestem stringiem'  # Zmienna typu String (jakies text)
i_am_integer = 3  # Zmienna typu Int (liczba)
i_am_boolean = False  # Zmienna typu Bool (prawda / klamstwo)

print(i_am_text)  # Output: Jestem stringiem
print(i_am_integer)  # Output: 3
print(i_am_boolean)  # Output: False


### Teraz te trudniejsze

#             0        1        2
my_list = ['filip', 'gocha', 'franek']  # lita czyli przetrymujemy wiecej jak jedna zmienna

# w ten sposob mozemy zobaczyc wszytkie elementy
print(my_list)  # Output: ['filip', 'gocha', 'franek']

# pokazujemy element z numerem 1
print(my_list[1])  # Output: gocha
# Czemu? Bo listy numeruje sie od 0

print(my_list[2])  # Output: franek
my_list[2] = 'nie franek'  # tutaj zmieniamy wartosc 'franek' na 'nie franek'
print(my_list[2])  # Output: nie franek

# slownicz czyli taka jakby lista ale zamiast liczby urzywamy stringow jako klucz
slownik_user = {
    'haslo': '!23QweAsd',
    'username': 'filip123'
}

# zeby dostac sie do wartosci ze slownika urzywamy nazwy nazwy zmiennej a potem [] - nawiasow kwadratowych. tak samo jak przy listach
print(slownik_user['haslo'])

# Petla for wykonuje podany kod podana ilosc razy
# for - slowo klucz
# _ - nazwa zmiennej przetrymujacej ktory raz petla soe odbywa
# in range(N) - mowi ze petla wykona sie N razy
for _ in range(5):
    print('Gocha nie pamieta')  # kod ktory mamy wyprintowac

# to samo tylko tym razem 3 razy
for i in range(3):
    # i za kazdym razem piezemy po kolei kazdy element z listy
    print(my_list[i])
