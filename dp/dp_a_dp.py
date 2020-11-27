# https://atcoder.jp/contests/dp/tasks/dp_a
n = int(input())
h = list(map(int, input().split()))
h.reverse()

dp = [1000000000 for i in range(n)]

dp[0] = 0
dp[1] = abs(h[1] - h[0])


def get_dp():
    if n > 2:
        for i in range(2, n):
            dp[i] = min(
                (dp[i - 2] + abs((h[i] - h[i - 2]))), (dp[i - 1] + abs(h[i] - h[i - 1]))
            )

    return dp[n-1]


print(get_dp())
