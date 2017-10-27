def suma(x):
    begin_suma = 0
    for i in x:
        begin_suma += i
    return begin_suma

def multiply(x):
    begin_multiply = 1
    for i in x:
        begin_multiply *= i
    return begin_multiply

print suma([1,2,3,4])
print multiply([1,2,3,4])
