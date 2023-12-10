a = int(input())
if a%4 != 0 :
  print("long " * ((a//4)+1) + "int")
else :
  print("long " * (a//4) + "int")

#2
n = int(input())
k = n // 4
str = ''
for _ in range(1,k+1):
    str += "long "
print(str + 'int')
