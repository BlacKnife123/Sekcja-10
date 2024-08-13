import time

def function_performance(func, how_many_times = 1, *arg):
    sum = 0

    for i in range(0,how_many_times+1):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum = sum+(end-start)

    return sum


setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]
def is_element_in(what_value,container):
    if what_value in container:
        return True
    else:
        return False
    
print(function_performance(is_element_in, 5000000, 450 ,setContainer))

"""ARGUMENTY POZYCYJNE(NIENAZWANE) PRZED ARGUMENTAMI NAZWANYMI"""
"""*arg - POWSTAJE ARGUMENT KTRÓEMU MOŻNA PRZYPISAĆ WIELE ZMIENNYCH ALE NIE NAZWANYCH (KROTKA)"""
"""**arg - POWSTAJE ARGUMENT KTÓREMU MOŻEMY PRZYPISAĆ WIELE ZMIENNYCH Z NAZWAMI (SŁOWNIK) NP.
    print(function_performance(is_element_in, 5000000, WHAT_VALUE=450 ,CONTAINER=setContainer))"""

