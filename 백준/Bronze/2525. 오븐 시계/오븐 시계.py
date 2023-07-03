a, b = map(int, input().split())
c = int(input())
b += c
if b >= 60 :
    count = b // 60
    a += count
    b = b % 60
    if a >= 24 :
        counta = a % 24
    else :
        counta = a
    print(counta, b)
    
elif b < 60 :
    print(a, b)