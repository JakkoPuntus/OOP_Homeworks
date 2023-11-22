def bubble_sort(l: list) -> list:
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


k = int(input())

l = [int(x) for x in input().split()]
s = sum(l)
l = bubble_sort(l)
c = 0
d = 0
for i in l:
    c += i//2 + 1
    d += 1
    if d > k//2:
        break

print(c)