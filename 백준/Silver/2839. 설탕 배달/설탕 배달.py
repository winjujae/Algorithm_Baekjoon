#2839번 설탕 배달(DP_효율적 화폐구성_바텀업)
n = int(input())
sub = [5,3]

d = [10001] * (n+1)
d[0] = 0
for i in range(2) :
    for j in range(sub[i], n+1) :
        if d[j-sub[i]] != 10001 :
            d[j] = min(d[j],d[j-sub[i]]+1)

if d[n] == 10001 :
    print(-1)
else :
    print(d[n])