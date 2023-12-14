a,b,c,d,e,f,g,h = map(int,input().split())
lst = [a,b,c,d,e,f,g,h]
asc = list(range(1,9))
desc = list(range(8,0,-1))
if lst == asc :
  print("ascending")
elif lst == desc :
  print("descending")
else :
  print("mixed")