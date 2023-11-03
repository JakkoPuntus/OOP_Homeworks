N, M = map(int, input().split())
deleted = {}
s = ''

for _ in range(M):
    c, n = input().split()
    n = int(n)

    if c == "L":
        deleted_count = sum(1 for key in deleted if key <= n)
        s += str(n + deleted_count) + '\n'
    else:
        if n in deleted:
            deleted[n] += 1
        else:
            deleted[n] = 1

print(s)
