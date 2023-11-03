n, k, t = map(int, input().split())

res = 0

while n > k:
    n *= 1 - t/100
    res += 1

print(res)
