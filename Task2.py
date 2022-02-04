from GeneralMods import MyMethods as MM

# 2. Найти максимальной из пяти чисел


print('Enter 5 numbers:')
numbers_list = [MM.input_int_number() for i in range(0,5)]
# print(numbers_list)
print(max(numbers_list))

# for i in range(0,5):
#     numbers_list.append(MM.input_int_number())


# print(numbers_list)

# def max_number(values_array):
#     return max(values_array)
       

# values_set = {1,646,345,23,24}
# values_tuple = (35,24,634,324,3436)

# print(max_number(values_set))
# print(max_number(values_tuple))