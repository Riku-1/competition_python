n = int(input())
a = list(map(lambda x: int(x), input().split(" ")))


nlist = list(range(1, n+1))
a.sort()

if a == nlist:
    print("Yes")
else:
    print("No")
