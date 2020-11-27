# https://atcoder.jp/contests/dp/tasks/dp_a
n = int(input())
h = list(map(int, input().split()))

memo_cost = [1000000000 for i in range(n)]


def find_cost(num):
    if num == 0:
        memo_cost[0] = 0
        return

    if num == 1:
        memo_cost[1] = abs(h[1] - h[0])
        return

    cost1 = memo_cost[num - 1] + abs((h[num] - h[num - 1]))
    cost2 = memo_cost[num - 2] + abs((h[num] - h[num - 2]))

    memo_cost[num] = min(cost1, cost2)
    return


for i in range(n):
    find_cost(i)

print(memo_cost[n-1])
