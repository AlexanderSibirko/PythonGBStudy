from GeneralMods.MyMethods import *


# 1. По двум заданным числам определить является ли одно квадратом другого
print('Введите первое число:')
a = input_int_number()
print('Введите второе число:')
b = input_int_number()

print(a, b)

def AorB_isPow(a, b):
    return (a == b**2 or b == a**2)

print(AorB_isPow(a, b))



