n = int(input())

s = []
t = []
for _ in range(n):
    st = input().split(" ")
    s.append(st[0])
    t.append(int(st[1]))

_max = sorted(t)[n-2]

max_index = t.index(_max)
print(s[max_index])
