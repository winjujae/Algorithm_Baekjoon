from string import ascii_lowercase
k = list(ascii_lowercase)
s = input()
for i in range(len(k)):
    print(s.find(k[i]), end = " ")