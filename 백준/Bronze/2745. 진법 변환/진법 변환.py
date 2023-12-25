lst = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = input().split()
answer = 0
for idx, num in enumerate(n[::-1]) :
    answer += int(b) ** idx * lst.index(num)
print(answer)

#2
#n, b = input().split()
#print(int(n, int(b)))