# 18. Реализовать алгоритм перемешивания списка.

import random

def shuffle_list(list_):
    len_ = len(list_)
    for i in range(0, len_-1):
        suf = random.randint(i, len_-1)
        list_[i], list_[suf] = list_[suf], list_[i]
    return list_

list_ = [0,1,2,3,4,5,6]

print(shuffle_list(list_))    
