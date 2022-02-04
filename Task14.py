# 14. Подсчитать сумму цифр в вещественном числе.
# Формально у вещественного числа может быть бесконечно цифр ? =)

import math

def calc_digits(number):
    sum = 0
    while number % 1 > 0:
        number *= 10
        print(number)
    while number > 0:
        sum += number % 10
        number //= 10
    return int(sum)

def calc_digits2(number):
    sum = 0
    for i in str(number):
        if i.isdigit():
            sum += int(i)
    return int(sum)

number = math.sqrt(2)
print(number)
print(calc_digits(number))
print(calc_digits2(number))

number = math.pi
print(number)
print(calc_digits(number))
print(calc_digits2(number))