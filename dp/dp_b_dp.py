# https://atcoder.jp/contests/dp/tasks/dp_b
n, k = map(int, input().split())
h = list(map(int, input().split()))

dp = [1000000000 for i in range(n)]
dp[0] = 0


def foo(num):
    if num == 0:
        return

    for i in range(k):
        if num - i < 0:
            return

        dp[num] = min(
            (dp[num - i - 1] + abs(h[num] - h[num - i - 1])),
            dp[num]
        )


for i in range(n):
    foo(i)

print(dp[n-1])
