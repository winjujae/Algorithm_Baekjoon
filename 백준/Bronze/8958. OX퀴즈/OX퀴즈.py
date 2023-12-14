n = int(input())
for i in range(n):
  str=input()
  cnt = 0
  lst = []
  for j in range(len(str)) :
    if str[j] == "O" :
      cnt += 1
      lst.append(cnt)
    else :
      cnt = 0
      lst.append(cnt)
  print(sum(lst))
    