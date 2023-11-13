n,m = map(int, input().split())
l = []
for i in range(n):
    l.append(input())


l = l[m%n:] + l[:m%n]

print(''.join(l[0:10]))