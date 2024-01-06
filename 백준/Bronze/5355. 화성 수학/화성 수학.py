for i in range(int(input())):
    lst = list(input().split())
    ans = float(lst[0])
    
    for j in lst[1:]:
        if j == "@":
            ans *= 3
        elif j == "%":
            ans += 5
        elif j == "#":
            ans -= 7

    print(f'{ans:.2f}')
