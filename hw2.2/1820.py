n, k = map(int, input().split())

if k > n: # если n<k то жарить нужно 2 минуты всегда
    print(2)
else:
    result = n * 2.0 / k
    result = int(result) if result - int(result) <= 0 else int(result) + 1 #округление вверх

    print(result)
