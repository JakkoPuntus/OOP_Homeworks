n = int(input())

numbers = list(map(int, input().split()))
c = 1
tmp = numbers[0]
for i in range(1, n):
    if numbers[i] == tmp:
        c += 1
    else:
        print(c, tmp, end=' ')
        tmp = numbers[i]
        c = 1

print(c, tmp)
