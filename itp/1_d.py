inp = int(input())

h = int(inp/3600)
m = int((inp - h*3600)/60)
s = inp - h*3600 - m*60

print(f"{h}:{m}:{s}")