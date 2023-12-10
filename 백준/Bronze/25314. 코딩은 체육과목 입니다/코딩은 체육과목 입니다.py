a = int(input())
if a%4 != 0 :
  print("long " * ((a//4)+1) + "int")
else :
  print("long " * (a//4) + "int")