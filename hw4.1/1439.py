#Лучшее из придуманного

N, M = map(int, input().split())
deleted = [N + 1]
s = []

for _ in range(M):
    c, n = input().split()
    n = int(n)

    if c == "D":
        deleted = [x-1 if x > n else x for x in deleted]
        deleted.append(n)
    else:
        s.append(n + sum(1 for e in deleted if e <= n))

print(*s, end='\n', sep='\n')