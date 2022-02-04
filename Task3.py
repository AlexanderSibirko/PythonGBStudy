# 3. Вывести на экран числа от -N до N

# for i in range(-N,N+1):
#     print(i)
    
# def N_list(N):
#     Num_list = []
#     for i in range(-N,N+1):
#         Num_list.append(i)
#     return Num_list

# numbers = N_list(N)

N = 10
numbers = [i for i in range(-N,N+1)]
print(numbers)

