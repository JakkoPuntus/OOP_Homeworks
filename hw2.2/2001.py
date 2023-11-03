a = []
b = []

for i in range(3):
    tmp = [int(x) for x in input().split()]
    
    a.append(tmp[0])
    b.append(tmp[1])

print(a[0]-a[2], b[0]-b[1])
