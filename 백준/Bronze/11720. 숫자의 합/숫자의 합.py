n = int(input())
char = str(input())
k = [char[i] for i in range(len(char))]
a = 0
for i in range(len(k)):
    a += int(k[i])
print(a)