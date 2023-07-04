n, m = map(int,input().split())
total = [i for i in range(n+1)]
for i in range(m) :
    start, end = map(int,input().split())
    total[start:end+1] = reversed(total[start:end+1])
total.remove(total[0])
print(*total) # *는 리스트의 각 요소를 개별인자로 반환