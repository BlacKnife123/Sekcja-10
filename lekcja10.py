def count(*numbers):

    sum = 0
    
    for i in numbers:
        sum = sum + i

    return sum


print(count(2,4,1,2,4,5,10))