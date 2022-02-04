# 31. Составить список простых множителей натурального числа N

# N = 64863214581876858567 # не справляется, огромный простой множитель
# N = 64863214581876858565 # не справляется, огромный простой множитель
# N = 64863214581876858564 # не справляется, огромный простой множитель
N = 64_863_214_581_876_858_564

def factors(N):
    factors = []
    factor = 2
    while factor * factor <= N:
        if N % factor == 0:
            factors.append(factor)
            N //= factor
        else:
            if factor == 3: 
                factor += 2
            else: 
                factor += 1
    factors.append(N)
    return factors

print(factors(N))            
    