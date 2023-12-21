palin = 0
while (palin != "0") :
    palin = input()
    if palin == "0":
        break
    if palin[::] == palin[::-1] :
        print("yes")
    else :
        print("no")
    