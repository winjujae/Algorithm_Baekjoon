a = int(input())
b = int(input())
c = int(input())
str1 = str(a * b * c)

for i in range(10):
    cnt = str1.count(str(i))
    print(cnt)