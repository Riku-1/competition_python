h = []
w = []

while True:
    a, b = map(lambda x: int(x), input().split(" "))
    if a == 0 and b == 0:
        break

    h.append(a)
    w.append(b)

for i in range(len(w)):
    for j in range(h[i]):
        output = ""
        for k in range(w[i]):
            if j%2 == 0 and k%2 == 0:
                output += "#"
            elif j%2 == 0 and k%2 != 0:
                output += "."
            elif j%2 != 0 and k%2 == 0:
                output += "."
            else:
                output += "#"

        print(output)
    print("")
