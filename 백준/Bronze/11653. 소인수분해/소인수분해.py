#11653번 소인수분해
n = int(input())
sub = []
for i in range(1,n+1):
    if n % i == 0 :
        sub.append(i)
#print(sub)
for j in sub[1:] :
    while(n % j == 0) :
        print(j)
        n = n//j