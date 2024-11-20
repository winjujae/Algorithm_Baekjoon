# 27433 : 팩토리얼
def func(x):
    if x < 2:
        return 1
    else:
        return x * func(x-1)

print(func(int(input())))