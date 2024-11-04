# 1110 : 더하기 사이클
x = int(input())
orig = x

def func(x) :
    integ = 0
    if x < 10 :
        x_temp = x * 11
    while True :
        integ += 1
        x_1 = x // 10
        x_2 = x % 10
        x_3 = (x_2 * 10) + ((x_1 + x_2) % 10)

        if  x_3 == orig :
            return integ
        x = x_3
        
print(func(x))