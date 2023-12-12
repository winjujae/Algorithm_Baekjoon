str = input()
result_str = ''
for char in str :
  if char.islower() :
    result_str += char.upper()
  else :
    result_str += char.lower()
print(result_str)

#2
print(input().swapcase())
