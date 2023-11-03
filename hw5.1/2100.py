n = int(input())
guests = 2

for i in range(n):
    s = input()
    guests += 1 + s.count('+one')

guests += 1 if guests == 13 else 0
print(guests*100)