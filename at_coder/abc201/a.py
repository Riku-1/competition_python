abc = input().split(" ")
abc = list(map(lambda x: int(x), abc))
abc.sort()

if abc[2] - abc[1] == abc[1] - abc[0]:
    print("Yes")
else:
    print("No")

