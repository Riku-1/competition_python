data_set = []
while True:
    x, y = map(lambda v: int(v), input().split(" "))
    if x == 0 and y == 0:
        break
    data_set.append((x, y))

for i in data_set:
    rev = sorted(i)
    print(rev[0], rev[1])
