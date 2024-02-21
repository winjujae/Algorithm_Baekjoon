#2845번 파티가 끝나고 난 뒤(언패킹, 리스트 컴프리헨션)
l, p = map(int, input().split())
lst = list(int(x) - (l*p) for x in input().split())
print(*lst, sep=' ')