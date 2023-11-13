S = int(input())

start = int((1 + (1+8*S)**0.5) / 2)

for N in range(start, 0, -1):
    A = S / N - (N - 1) / 2

    if A.is_integer() and A>0:
        print(int(A), N, start)
        break


