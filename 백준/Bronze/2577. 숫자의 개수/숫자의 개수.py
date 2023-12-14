a = int(input())
b = int(input())
c = int(input())
str1 = str(a*b*c)
for i in range(10) :
  cnt = 0
  for j in range(len(str1)) :
    if str(i) == str1[j] :
      cnt += 1
  print(cnt)

#2
a = int(input())
b = int(input())
c = int(input())
str1 = str(a * b * c)

for i in range(10):
    cnt = str1.count(str(i))
    print(cnt)
