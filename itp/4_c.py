data_set = []
while True:
    n1, op, n2 = input().split(" ")
    if op == "?":
        break
    data_set.append((int(n1), op, int(n2)))

for i in data_set:
    if i[1] == "+":
        print(i[0] + i[2])
    elif i[1] == "-":
        print(i[0] - i[2])
    elif i[1] == "*":
        print(i[0] * i[2])
    else:
        print(int(i[0] / i[2]))
