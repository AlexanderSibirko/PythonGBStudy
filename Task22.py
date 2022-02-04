# 22. Найти сумму чисел списка стоящих на нечетной позиции

def sum_odd(list_):
    sum = 0
    for i in range(0, len(list_), 2):
        sum += list_[i]
    return sum

list_ = [0,1,2,3,4,5,6,7,8,9]
print(sum_odd(list_))

list_ = [15]
print(sum_odd(list_))

list_ = [5,5,5]
print(sum_odd(list_))

list_ = []
print(sum_odd(list_))