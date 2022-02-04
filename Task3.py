# 3. Вывести на экран числа от -N до N

N = 10

for i in range(-N,N+1):
    print(i)
    
def N_list(N):
    Num_list = []
    for i in range(-N,N+1):
        Num_list.append(i)
    return Num_list


numbers = N_list(N)
print(numbers)