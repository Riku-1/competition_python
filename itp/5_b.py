h = []
w = []
while True:
    hi, wi = map(lambda x: int(x), input().split(" "))
    if hi == 0 and wi == 0:
        break
    h.append(hi)
    w.append(wi)


for i, v in enumerate(h):
    print("#" * w[i])

    for _ in range(h[i]-2):
        print("#" + "." * (w[i]-2) + "#")

    print("#" * w[i])
    print("")
