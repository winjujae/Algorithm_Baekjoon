#n번방 1 7 19 37 61 91 127 169
#차이 6 12 18 24 30 36 42
n = int(input())
lst = [1,6]
cnt = 1
while(lst[0] < n) :
    lst[0] = lst[1] + lst[0]
    lst[1] += 6
    cnt += 1
print(cnt)