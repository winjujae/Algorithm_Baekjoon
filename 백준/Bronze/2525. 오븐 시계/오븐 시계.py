a, b = map(int, input().split())
c = int(input())
b += c
if b >= 60 :
    count = b // 60
    a += count
    b = b % 60
    if a >= 24 :
        counta = a % 24
    else :
        counta = a
    print(counta, b)
    
elif b < 60 :
    print(a, b)

#2
a, b = map(int,input().split())
c = int(input())
if (b+c) // 60 >= 1 :
  a += (b+c) // 60
  if a >= 24 :
    a = a % 24
  print(a, (b+c) - 60*((b+c)//60))
else :
  print(a, b+c)
