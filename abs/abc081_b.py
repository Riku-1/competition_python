n = int(input())
a = list(map(int, input().split()))

total = 0

def divide(alist, total):
    while True:
        if any(f % 2 != 0 for f in alist):
            return total

        alist = list(map(lambda x: x/2, alist))
        total += 1

print(divide(a, total))
