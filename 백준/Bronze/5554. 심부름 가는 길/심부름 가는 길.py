#5554번 심부름 가는 길
lst = []
for i in range(4) :
    lst.append(int(input()))
a = sum(lst) // 60
b = sum(lst) % 60
print(a)
print(b)