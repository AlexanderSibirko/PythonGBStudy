# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

def if_its_true(predicats):
    for i in range(0, len(predicats[0])):
        for j in range(0, len(predicats)):
            x = predicats[j][i]
            y = predicats[j][i]
            z = predicats[j][i]
        if (~(x | y | z) == ~x & ~y & ~z):
            continue
        else:
            return False
    return True

def create_predicats(predicats_amount):
    result = []
    for j in range(1,predicats_amount+1):
        curBool = True
        k = 1
        predicat = []
        for i in range(0, 2 ** predicats_amount):
            if (k > 2 ** (predicats_amount - j )):
                curBool = not curBool
                k = 1
            k += 1
            predicat.append(curBool)
        result.append(tuple(predicat))
    return tuple(result)
            
preds = create_predicats(3)
print(preds)
print(if_its_true((preds)))