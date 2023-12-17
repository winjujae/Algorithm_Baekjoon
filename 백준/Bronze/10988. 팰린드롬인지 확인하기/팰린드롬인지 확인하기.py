n = input()
lst1 = []
cnt = 0
for i in n :
  lst1.append(i)
for i in range(len(n)) :
  if lst1[i] == lst1[len(n)-1-i] :
    cnt += 1
if cnt == len(n) :
  print("1")
else :
  print("0")
