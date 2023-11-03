
k, n = map(int, input().split())

a = list(map(int, input().split()))

res = 0 #число машин в пробке

for i in range(n):
    if res + a[i] > k:
        res += a[i] - k

    else:
        res = 0

print(res)
