a, b, c = map(lambda x: int(x), input().split(" "))

result = 0
for v in range(a, b + 1):
    if c % v == 0:
        result += 1

print(result)