n = int(input())
fac = 1
cnt = 0
for i in range(n,0,-1):
    fac *= i
fac = str(fac)
for i in range(len(fac),0,-1) :
    if fac[i-1] == "0" :
        cnt += 1
    else :
        print(cnt)
        break