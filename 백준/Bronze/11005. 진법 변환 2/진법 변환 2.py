n, b = map(int,input().split())
lst = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 60466175 36
# ZZZZZ
x = []
for idx, i in enumerate(lst) :
    if idx+1 == b :
        while(n // b > 0) :
            x.append(n % b)
            n = n // b
        x.append(n % b)
# print(x)
str = ""
for j in x[::-1] :
    str += lst[j]
print(str)