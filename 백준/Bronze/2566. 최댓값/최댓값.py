map_array = [list(map(int, input().split())) for _ in range(9)]
lst = []
max_row,max_col = 0, 0
for idx, i in enumerate(map_array) :
    lst.append(max(map_array[idx]))
for idx, i in enumerate(lst) :
    if i == max(lst) :
        max_row = idx
for idx, i in enumerate(map_array[max_row]) :
    if i == max(map_array[max_row]) :
        max_col = idx
print(map_array[max_row][max_col])
print(max_row+1 , max_col+1)