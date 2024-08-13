"""
Napisz program, który policzy sumę wszystkich liczb od 1 do podanej liczby

Dla Np. 5

1+2+3+4+5
zwróci
15

"""

import time

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

def finish_timer(start):
    end = time.perf_counter()
    return end-start


liczba = int(input("Do jakiej liczby chcesz zsumować: "))

start = time.perf_counter()
print("Wynik to:", sumuj_do(liczba))
print(finish_timer(start))

start = time.perf_counter()
print("Wynik to:", sumuj_do2(liczba))
print(finish_timer(start))

start = time.perf_counter()
print("Wynik to:", sumuj_do3(liczba))
print(finish_timer(start))

start = time.perf_counter()
print("Wynik to:", sumuj_do4(liczba))
print(finish_timer(start))

start = time.perf_counter()
print("Wynik to:", sumuj_do5(liczba))
print(finish_timer(start))




