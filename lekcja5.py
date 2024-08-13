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

def function_performance(func, arg):
    start = time.perf_counter()
    func(arg)
    end = time.perf_counter()
    return end - start

liczba = int(input("Do jakiej liczby chcesz zsumować: "))

print(function_performance(sumuj_do, 10))
print(function_performance(sumuj_do2,liczba))
print(function_performance(sumuj_do3,liczba))
print(function_performance(sumuj_do4,liczba))
print(function_performance(sumuj_do5,liczba))
