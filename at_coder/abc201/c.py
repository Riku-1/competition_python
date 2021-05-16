s = input("")

total = 0
for i in range(10**4):
    i_zero = str(i).zfill(4)

    is_able_to_exist = True
    for j in range(10):
        if s[j] == "o" and not str(j) in i_zero:
            is_able_to_exist = False
        if s[j] == "x" and str(j) in i_zero:
            is_able_to_exist = False

    if is_able_to_exist:
        total += 1

print(total)
