"""

    obiekt to zmienna, która ma więcej możliwości,
    można wywołać na nim "Funkcje"
    może mieć więcej niż 1 wartość

    obiekty immutable: bool, int, float, tuple, str

    immutable - niezmienne
    mutable - zmienny

    = - zmiana miejsca wskazywania na nowy adres, na inny obiekt
"""

a = 4

listSamole = [1,4,512,24]
listSamole2 = listSamole

listSamole2.append(465) #Mutable

a = 4

b = a

b = 7

c = 5

def add(c,amount = 1):
    print(id(c))
    c = c + amount
    print(id(c))

add(c)


def append_element_to_list(listka, element):
    print(id(listka))
    listka.append(element)
    print(id(listka))

print(id(listSamole))
append_element_to_list(listSamole,5)
