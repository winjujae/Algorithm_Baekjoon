# 2747 : 피보나치 수
n = int(input())
def fibo(x) :
    if x == 0 :
        return 0
    elif x == 1 :
        return 1
    
    a, b = 0, 1
    for _ in range(2, x + 1):
        a, b = b, a + b
    return b

print(fibo(n))