n = int(input())
a = []
for i in range(n):
    a.append(input().split())

for i in range(2*n-1):
        if i < n:
            print(*[a[j][i-j] for j in range(i, -1, -1)], end=' ')
        else:
             print(*[a[j][i-j] for j in range(n-1, i-n,-1)], end=' ')

    


