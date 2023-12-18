n = int(input())
lst = []
for i in range(n) :
  str = input()
  lst.append(str)
lst = list(set(lst))
lst.sort(key=lambda x : (len(x),x))
for i in range(len(lst)) :
  print(lst[i])