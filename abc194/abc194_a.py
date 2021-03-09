a, b = map(lambda x: int(x), input().split(" "))


def foo(x, y):
    s = x + y
    if s >= 15 and y >= 8:
        return 1

    if s >= 10 and y >= 3:
        return 2

    if s >= 3:
        return 3
    return 4


print(foo(a, b))