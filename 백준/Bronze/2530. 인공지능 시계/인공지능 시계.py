a, b, c = map(int,input().split())
d = int(input())

if c + d >= 60 :
    new_c = (c + d) % 60
    new_b = b + (c + d)//60
    if new_b >= 60 :
        new_b1 = new_b % 60
        new_a = a + new_b // 60
        if new_a//24 >= 1 :
            new_a1 = new_a % 24
        else :
            new_a1 = new_a
    else :
        new_b1 = new_b
        new_a1 = a
else :
    new_c = c + d
    new_b1 = b
    new_a1 = a
print(new_a1, new_b1, new_c)