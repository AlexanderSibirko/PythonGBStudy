#  11. Для натурального N создать список: 1, -3, 9, -27, 81 и т.д.

def list_by_rules(N):
    l_result = []
    for i in range(0, N):
        l_result.append((-3)**i)
    return l_result
        
print(list_by_rules(6))
        
    