#19532번 수학은비대면강의입니다(완전 탐색)
#ax + by = c
#dx + ey = f
a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 1000) :
    for j in range(-999, 1000) :
        if (a*i) + (b*j) == c and (d*i) + (e*j) == f :
            print(i,j)
