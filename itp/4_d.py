n = int(input())
an = list(map(lambda x: int(x), input().split(" ")))

min_an = min(an)
max_an = max(an)
avg_an = sum(an)

print(str(min_an) + " " + str(max_an) + " " + str(avg_an))
