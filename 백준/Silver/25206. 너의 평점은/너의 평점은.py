sub_grad_rate = {"A+" : 4.5, "A0" : 4.0, "B+" : 3.5, "B0" : 3.0,
                "C+" : 2.5, "C0" : 2.0,
                "D+" : 1.5, "D0" : 1.0, "F" : 0.0, "P" : 0.0}
lst_rate, lst_grad = [], []
total = []
for i in range(20) :
    sub_name, sub_rate, sub_grad = input().split()
    if sub_grad == "P" :
        continue
    lst_rate.append(float(sub_rate))
    lst_grad.append(sub_grad)
    total.append(float(sub_rate) * sub_grad_rate[sub_grad])
print(sum(total) / sum(lst_rate))