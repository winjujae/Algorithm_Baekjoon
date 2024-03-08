#1100번 하얀 칸
lst_array = [input() for _ in range(8)]
#print(lst_array)
cnt = 0
for i in range(len(lst_array)) :
    if i % 2 == 0 :
        for j in lst_array[i][::2] :
            if j == 'F' :
                cnt += 1
    else :
        for j in lst_array[i][1::2] :
            if j == 'F' :
                cnt += 1
print(cnt)