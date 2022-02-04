# 10. Найти расстояние между двумя точками пространства
import math

def get_range(dot1, dot2):
    sum = 0
    for i in range(0, len(dot1)):
        sum += (dot1[i]-dot2[i])**2
    return math.sqrt(sum)

dot1 = [10,10,10]
dot2 = [0,0,0]
print(get_range(dot1, dot2))

dot1 = [-10,-10,-10]
dot2 = [0,0,0]
print(get_range(dot1, dot2))

dot1 = [-10,-5,0]
dot2 = [0,5,10]
print(get_range(dot1, dot2))

dot1 = [10,10]
dot2 = [0,0]
print(get_range(dot1, dot2))

# есть готовая функция dist !
print(math.dist(dot1, dot2))