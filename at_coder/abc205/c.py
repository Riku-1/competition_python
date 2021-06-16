a, b, c = map(lambda x: int(x), input().split(" "))

if c % 2 == 0:
    a = abs(a)
    b = abs(b)

if a == b:
    print("=")

elif a > b:
    print(">")

else:
    print("<")


