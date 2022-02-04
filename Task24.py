# 24. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным 
# значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_ = [1.1, 1.2, 3.1, 5, 10.01]

def new_list (list_):
    fractions_list = []
    for i in list_:
        fractions_list.append(str(i).split(sep='.'))
    return fractions_list

num = '10.002'
print(num)
num =float(num)
print(num)

a = 1.2
a = 1.2 - 1.0
print(a)

print(list_)
print(new_list(list_))