# 13. Пользователь задаёт две строки. Определить количество количество вхождений одной строки в другой.

string1 = 'количество'
string2 = 'Определить количество количество вхождений одной строки в другой'


def str1_in_str2(string1, string2):
    return string2.count(string1)

print(str1_in_str2(string1, string2))

string2 = 'Определить количество количество количество количество вхождений одной строки в другой'
print(str1_in_str2(string1, string2))

string2 = 'Определить вхождений одной строки в другой'
print(str1_in_str2(string1, string2))