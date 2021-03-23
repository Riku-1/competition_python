inp = list(map(lambda x: int(x), input().split(" ")))

for i, v in enumerate(sorted(inp)):
    if i == len(inp)-1:
        print(v)
    else:
        print(v, end=" ")
