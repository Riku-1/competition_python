a, b = map(lambda x: int(x), input().split(" "))

d = int(a/b)
r = a%b
f = a/b

print(d, r, "{:.9f}".format(f))