# 16. Задать список из n чисел последовательности (1+1/n)^n и вывести на экран их сумму 

# Функция которая стремиться к 'е'

import math

def specific_list(n):
    l_result = []
    for i in range(1, n+1):
        l_result.append((1+1/i)**i)
    return l_result

def sum_list(list_):
    return sum(list_)

print(specific_list(50))

print(sum_list(specific_list(50)))

f = lambda x: ((1+1/x)**x)
list_ = [f(x) for x in range(1,51)]
print(list_)
print(sum(list_))
        
