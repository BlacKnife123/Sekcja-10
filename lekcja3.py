"""
Napisz program, który policzy sumę wszystkich liczb od 1 do podanej liczby

Dla Np. 5

1+2+3+4+5
zwróci
15

"""

def sumuj_do(liczba):
    suma = 0

    for liczba in range(1,liczba+1):
        suma = suma + liczba

    return suma

def sumuj_do2(liczba):
    return sum([liczba for liczba in range(1,liczba+1)])

def sumuj_do3(liczba):
    return sum({liczba for liczba in range(1,liczba+1)})

def sumuj_do4(liczba):
    return sum((liczba for liczba in range(1,liczba+1)))

def sumuj_do5(liczba):
    return (1 + liczba) / 2 * liczba


liczba = int(input("Do jakiej liczby chcesz zsumować: "))

print("Wynik to:", sumuj_do(liczba))
print("Wynik to:", sumuj_do2(liczba))
print("Wynik to:", sumuj_do3(liczba))
print("Wynik to:", sumuj_do4(liczba))
print("Wynik to:", sumuj_do5(liczba))




