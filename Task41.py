
def op_sum(a,b):
    return a+b
def op_sub(a,b):
    return a-b
def op_mult(a,b):
    return a*b
def op_div(a,b):
    return a/b
def op_pow(a,b):
    return a**b

sum_ = op_sum
sub_ = op_sub
mult_ = op_mult
div_ = op_div
pow_ = op_pow

def calc(op,a,b,):
    return op(a,b)


ops = {"+": sum_,"-": div_,"*":mult_,"/":div_,"^":pow_}

math_str = "5.0 + 5 * 1 - 9.0 / 3.0 ^ 2 + -2 ^ 2 ^ 2 + ( 8.3 - 5.3 )"

# собираем все подряд пока не упремся в "-" унарный минус, "(" оскртывающую скобку, ")" закрывающую скобку, действия "^*/+-"
# 1. превращаем в постфиксную запись
def create_postfix_list(string_):
    curitem = '' # собираем сюда все пока не упремся в "спец. символ", таким образом получаем число
    calc_stack = [] # стак для проведения вычисления => собираем сюда элементы в очерёдности посфиксной записи
    ops_stack = [] # стак операций, заполняется и выталкивает из себя операции по спец. правилам

    for i in string_: # бежим по каждому символу
        if i not in "+-*/^()": # если не встретили "спец. символ"
            curitem += i # прицепляем всё в текущее значение
        else: #если встретили "спец. символ"
            if len(curitem): # то что скопили в текущем значении выталкиваем в постфиксную запись
                calc_stack.append(curitem) 
                curitem = ''
            else: # встретили два "спец. символа" подряд

    # curitem = ""
    # result = []
    # stack = []

    # for i in string_:
    #     if i in "+-*/^()":
    #         if curitem:
    #             result.append(float(curitem))
    #             curitem = ""
    #             if i == "+" or i == "-":
    #                 while len(stack)>0 and stack[len(stack)-1] in "+-*/^":
    #                     result.append(stack.pop())
    #                 else:
    #                     stack.append(i)
    #             elif i == "*" or i == "/":
    #                 while  len(stack)>0 and stack[len(stack)-1] in "*/^":
    #                     result.append(stack.pop())
    #                 else:
    #                     stack.append(i)
    #             elif i == "^":
    #                 while  len(stack)>0 and stack[len(stack)-1] in "^":
    #                     result.append(stack.pop())
    #                 else:
    #                     stack.append(i)
    #             elif i == "(":
    #                 pass
    #             elif i == ")":
    #                 pass
    #             else:
    #                 pass

    #         else:    
    #             stack.append(i)
            
    #     else:
    #         curitem += i
    # result.append(curitem)
    # while len(stack)>0:
    #     result.append(stack.pop())

    # return result

postfix = create_postfix_list(math_str)
print(postfix)
# # 5 3.2 2.2 5 10 5 2 3 3




# 2. вычисляем постфиксную запись
