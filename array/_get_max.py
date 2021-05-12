def get_max(target: [int]) -> int:
    max_n = target[0]
    for i in target:
        if i > max_n:
            max_n = i
    return max_n

print(get_max([1, 3, 4]))
print(get_max([-1, 3, 4]))
print(get_max([-1, -111, -4]))
