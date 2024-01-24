#14215번 세 막대
lst = list(map(int,input().split()))
lst.sort()
while(lst[2] >= lst[1] + lst[0]) :
    lst[2] -= 1
print(lst[2] + lst[1] + lst[0])