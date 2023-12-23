# 2941번 크로아티아 알파벳
n = input()
croa = ["c=","c-","dz=","d-","lj","nj","s=","z="]
cnt=0
for i in croa :
    if i in n :
        cnt += n.count(i)
        n = n.replace(i,' ')
n = n.replace(' ','')
cnt += len(n)
print(cnt)