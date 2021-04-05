data_set = []
while True:
    x = int(input())
    if x == 0:
        break
    data_set.append(x)

for i, v in enumerate(data_set):
    print(f"Case {i+1}: {v}")