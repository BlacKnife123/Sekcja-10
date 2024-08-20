numbers1 = [1,3,5,7,8,9]
numbers2 = [1,3,5,7,9]
numbers3 = [2,4,6,8]

def any_even(lista):
   return any([nr % 2 == 0 for nr in lista])

def all_even(lista):
   return all([nr % 2 == 0 for nr in lista])


print(any_even(numbers1))
print(any_even(numbers2))


if(any_even(numbers1)):
   print("W tej liście jest parzysta")
else:
   print("Nie")

if(any_even(numbers2)):
   print("W tej liście jest parzysta")
else:
   print("Nie")

john = {'name':'John Doe',
        'age': 30,
        'skills':['Python','JavaScript','C++']}

jane = {'name':'Jane Doe',
        'age': 30,
        'skills':['Python','Java']}


#any -jakikolwiek - funkcja any SPRAWDZA, czy JAKAKOLWIEK wartosc to True

