data_list = []

while True:
    data = tuple(map(lambda x: int(x), input().split(" ")))
    if data[0] == 0 and data[1] == 0:
        break
    data_list.append(data)

for data in data_list:
    for i in range(data[0]):
        print("#" * data[1])
    print("")

