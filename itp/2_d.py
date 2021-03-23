w, h, x, y, r = map(lambda x: int(x), input().split(" "))

result = False

if x-r < 0:
    result = False
elif y-r < 0:
    result = False
elif x+r > w:
    result = False
elif y+r > h:
    result = False
else:
    result = True

if result:
    print("Yes")
else:
    print("No")



