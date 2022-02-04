# 24. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным 
# значением дробной части элементов. Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list_ = [1.1, 1.2, 3.1, 5, 10.01]

new_list = [round(x % 1,8) for x in list_ if x%1 > 0]

min_in_list = lambda x: min(x)
max_in_list = lambda x: max(x)
sub = lambda x,y: x-y

print(list_)
print(new_list)
print(sub(max_in_list(new_list), min_in_list(new_list)))