"""copy - płytka kopia

def evil_function(toBeDestroyedList):
    print(id(toBeDestroyedList))
    toBeDestroyedList.clear()


myList = [1,4,2,1,52,3]

print(id(myList))
evil_function(myList.copy)
"""

"""
copy.deepcompy(element) - głęboka kopia
import copy


def evil_function(toBeDestroyedList):
    print(id(toBeDestroyedList))
    toBeDestroyedList.clear()


myList = [[1,4],[2,1],[52,3]]

evil_function(copy.deepcopy(myList))

a = 4
b = 4
"""