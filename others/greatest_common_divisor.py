# a > 0, b > 0

def get_greatest_common(a: int, b: int):
    commons = []

    i = 2
    while a >= i and b >= i:
        if a % i == 0 and b % i == 0:
            commons.append(i)
            a = a/i
            b = b/i
            i = 1

        i += 1

    multiples = 1

    for i in commons:
        multiples *= i

    return multiples

print(get_greatest_common(1, 4) == 1)  # a or b = 1
print(get_greatest_common(3, 4) == 1)  # no common
print(get_greatest_common(12, 12) == 12) # a = b
print(get_greatest_common(12, 18) == 6)

# TODO: Euclidean algorithm
