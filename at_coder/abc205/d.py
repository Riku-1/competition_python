n, q = map(lambda x: int(x), input().split(" "))
a = list(map(lambda x: int(x), input().split(" ")))

k = []
for _ in range(q):
    k.append(int(input()))

for ki in k:
    nokori = ki
    value = 0
    while True:
        if nokori == 0:
            print(value)
            break
        




