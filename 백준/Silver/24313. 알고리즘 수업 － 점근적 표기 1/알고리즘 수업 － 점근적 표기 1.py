#24313번 알고리즘 수업-점근적 표기1
a1, a0 = map(int,input().split())
c = int(input())
n = int(input())
if a1*n + a0 <= c*n and a1 <= c :
    print(1)
else :
    print(0)