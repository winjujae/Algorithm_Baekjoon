for _ in range(int(input())) :
    c = int(input())
    first, second, third, forth = 0,0,0,0
    if c // 25 > 0 :
        first = c//25
        c = c%25
    if c // 10 > 0 :
        second = c // 10
        c = c%10
    if c // 5 > 0 :
        third = c // 5
        c = c%5
    if c // 1 > 0 :
        forth = c
    print(first, second,third,forth)