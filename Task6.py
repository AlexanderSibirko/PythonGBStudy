# 6. Дано число обозначающее день недели. Вывести его название и указать является ли он выходным.

weekdays_namе_and_type = (('понедельник','рабочий'), ('вторник','рабочий'), ('среда','рабочий'), ('четверг','рабочий'), ('пятинца','рабочий'), ('суббота','выходной') , ('воскресение','выходной'))

def weekday_name(day_number_value):
    return (weekdays_namе_and_type[day_number_value-1])

for i in range(1,8):
    print(f'{i} = {weekday_name(i)}')

# list_ = [weekday_name(x) for x in range(1,8)]
# print(weekday_name(x) for x in range(1,8))
# print(list_)