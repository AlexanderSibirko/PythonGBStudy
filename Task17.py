# 17. Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

import random

Size = 10
def random_(min, max):
    return random.randint(min, max)

def create_list(N):
    list_ = []
    for i in range(0,N):
        list_.append(random_(-N,N))
    return list_

# creating file if not exist
f = open('file.txt','a')
f.close()

# writing in file 2 indexes
f = open('file.txt','w')
x = str(random_(0, Size-1))
print(x)
f.write(x + '\n')
f = open('file.txt','a')
x = str(random_(0, Size-1))
print(x)
f.write(x)
f.close()

def position_prod(list_):
    f = open('file.txt','r')
    result = list_[int(f.readline())] * list_[int(f.readline())]
    f.close
    return result

test_list = create_list(Size)
print(test_list)
print(position_prod(test_list))