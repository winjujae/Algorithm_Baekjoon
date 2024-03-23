#1436번 영화감독 숌
lst = int(input())
cnt = 0
result = 666
# 666을 while으로 필요 input만큼 요구하는 값으로 회전시켜 답을 도출함
while(True) :
    if '666' in str(result):
        cnt += 1
    if cnt == lst :
        break
    result += 1
print(result)