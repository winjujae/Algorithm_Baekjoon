#10987번 모음의개수
lst = 'aeiou'
lst_input = input()
cnt = 0
for i in lst :
    cnt += lst_input.count(i)
print(cnt)