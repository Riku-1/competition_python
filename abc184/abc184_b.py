# https://atcoder.jp/contests/abc184/tasks/abc184_b

n, x = map(int, input().split())
s = input()

num = x
for i in range(0, n):
    if s[i] == "o":
        num = num + 1
    else:
        if num != 0:
            num = num - 1

print(num)



