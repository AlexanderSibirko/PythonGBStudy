# 4. Показать первую цифру дробной части числа

def first_fraction_digit(number):
    if type(number) == int or type(number) == float:
        return int(number * 10 % 10)
    else:
        return 'Error: argument is not a number'
    # else:
    #     if number.isdecimal():
    #         return int(float(number) * 10 % 10)
    #     else:
    #         return 'Error 42: not number in argument'
  
first_digit = lambda a : int(a *10 % 10)

Number = 564.486
print(Number, first_fraction_digit(Number))
print(Number, first_digit(Number))


Number = 564.5
print(Number, first_fraction_digit(Number))
print(Number, first_digit(Number))

Number = 564.0
print(Number, first_fraction_digit(Number))
print(Number, first_digit(Number))

Number = 5600
print(Number, first_fraction_digit(Number))
print(Number, first_digit(Number))

# Number = '56'
# print(Number, first_fraction_digit(Number))

# Number = '56.4324'
# print(Number, first_fraction_digit(Number))

# Number = '56432,345'
# print(Number, first_fraction_digit(Number))

# Number = '564321a,3rw45'
# print(Number, first_fraction_digit(Number))

