# 20. Определить, присутствует ли в заданном списке строк, некоторое число 
number = 3

def look_for_number(n, list_):
    looking_str = str(n)
    for str_ in list_:
        if looking_str in str(str_):
            return True
        
list_a = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
print(look_for_number(number, list_a))

list_a = ["qwe", "asd", 3, "qwe", "ertqwe"]
print(look_for_number(number, list_a))

list_a = ["qwe", "asd", 0, "qwe", "ertqwe", 3, "ertre"]
print(look_for_number(number, list_a))

list_a = ["qwe", "asd", "qwe", "ertqwe", "f3ewr", "ertre"]
print(look_for_number(number, list_a))