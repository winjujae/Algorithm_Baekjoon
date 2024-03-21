#1343번 폴리오미노
lst_input = input()
lst_input = lst_input.replace('XXXX','AAAA')
lst_input = lst_input.replace('XX','BB')
if lst_input.count('X') >= 1 :
    print(-1)
else :
    print(lst_input)