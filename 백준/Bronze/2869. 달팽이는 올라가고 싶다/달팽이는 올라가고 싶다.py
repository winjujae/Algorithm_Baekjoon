a, b, v = map(int,input().split())

if (v-b)%(a-b) == 0 :
    k = (v-b)//(a-b)
else :
    k = (v-b)//(a-b)+1
print(k)