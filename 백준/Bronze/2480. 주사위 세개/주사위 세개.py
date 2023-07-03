a, b, c = map(int, input().split())

if a == b and b == c :
    pz = 10000 + a * 1000
elif a == b or b == c :
    pz = 1000 + b * 100
elif a == c :
    pz = 1000 + a * 100
else :
    pz = max(a,b,c) * 100
print(pz)