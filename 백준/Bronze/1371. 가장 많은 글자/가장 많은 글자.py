#1371번 가장 많은 글자
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha_cnt = [0] * 26
import sys
while(True) :
    input_str = sys.stdin.read().strip()
    if not input_str :
        break
    cnt = []
    for idx, i in enumerate(alpha) :
        alpha_cnt[idx] += input_str.count(i)
# print(cnt)
# print(alpha_cnt)

ans = []
for idx, i in enumerate(alpha_cnt) :
    if i == max(alpha_cnt) :
        ans.append(alpha[idx])
print(''.join(ans))
# print(alpha[cnt.index(max(cnt))])