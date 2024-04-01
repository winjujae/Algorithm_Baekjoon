#11050번 이항 계수 1
a,b = map(int,input().split())
lst = list(range(1,a+1))
up = 1
down = 1
for i in lst[::-1][:b] :
    up *= i
for j in range(1,b+1) :
    down *= j
print(up // down)