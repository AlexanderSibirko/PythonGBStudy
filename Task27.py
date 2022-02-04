# 27. Строка содержит набор чисел. Показать большее и меньшее число

numbers_string = '22,42, 53 336, 324   234  , 236'

def min_max_in_numbers_string(numbers_string):
    list_ = numbers_string.replace(',',' ').split()
    print(list_) ### Debugg remove on prod
    for i in range(0, len(list_)):
         list_[i] = int(list_[i])
    print(list_) ### Debugg remove on prod
    return min(list_), max(list_)

min_, max_ = min_max_in_numbers_string(numbers_string)

print(f'Минимальное: {min_}, Максимальное: {max_}')
