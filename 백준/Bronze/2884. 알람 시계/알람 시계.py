h, m = map(int,input().split())
if (m - 45 ) < 0:
  m = 60 + (m - 45)
  h = h-1
  if h == -1 :
    h = 23
  print(h, m)
else :
  print(h, m-45)