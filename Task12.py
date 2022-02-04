# 12. Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3k + 1 
# k - предыдущий элемент OR k - номер индекса ?

N = 10

def dict_by_rule(N):
    d_result = {}
    for i in range(0,N):
        if i == 0 :
            d_result[i] = 1
        else:
            d_result[i] = d_result[i-1]*3 + 1
    return d_result

print(dict_by_rule(N))


list_ = list(enumerate([(3*x+1) for x in range(0,N)]))
print(list_)