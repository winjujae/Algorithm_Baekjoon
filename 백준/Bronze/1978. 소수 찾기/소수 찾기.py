# 1978번_소수 찾기
n = int(input())
lst = list(map(int,input().split()))
cnt = 0
for i in lst :
    if i == 1 :
        continue
    elif i == 2 :
        cnt += 1
        continue
    for j in range(2,i) :
        if i % j == 0 :
            err = 1
            break
        else :
            err = 0
    if err == 0 :
        cnt += 1
        
print(cnt)        