a1,b1,c1,d1 = map(int,input().split())
a2,b2,c2,d2 = map(int,input().split())
if a1+b1+c1+d1 < a2+b2+c2+d2 :
    print(a2+b2+c2+d2)
else :
    print(a1+b1+c1+d1)