# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

divider1 = 5
divider2 = 10
divider3 = 15
divider4 = 30

def Div1_AND_Div2ORDiv3_NOT_Div4(num, div1, div2, div3, div4):
    return (num % div1 == 0) and (num % div2 == 0 or num % div3 == 0) and not (num % div4 == 0)

for i in range(1,13):
    num = i*5
    print(num, Div1_AND_Div2ORDiv3_NOT_Div4(num, divider1, divider2, divider3, divider4))