#2441번 별찍기4
n = int(input())
lst = '*' * n
print(lst)
for i in range(n-1) :
    lst = lst[:i] + lst[i].replace('*',' ') + lst[i+1:]
    print(lst)