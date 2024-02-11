#2506번 점수계산
input()
lst = list(map(int,input().split()))
k, ans = 0, 0
for i in lst :
    if i == 1 :
        k += 1
        ans += k
    else :
        k = 0
print(ans)