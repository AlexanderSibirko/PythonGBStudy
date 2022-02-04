# 15. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

def number_list (N):
    l_result = []
    for i in range(1, N+1):
        if i == 1:
            l_result.append(1)
        else:
            l_result.append(l_result[i-1-1]*i)
    return l_result


print(number_list(4))
print(number_list(5))
print(number_list(6))