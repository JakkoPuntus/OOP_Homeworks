PI = 3.14

n, r = map(float, input().split())
n = int(n)

res = 0
x_tmp, y_tmp = [float(x) for x in input().split()]
x0, y0 = x_tmp, y_tmp

for i in range(n-1):
    x, y = [float(x) for x in input().split()]
    res += ((x-x_tmp)**2 + (y-y_tmp)**2)**0.5
    x_tmp, y_tmp = x, y


res += ((x0-x_tmp)**2 + (y0-y_tmp)**2)**0.5
res += 2*PI*r

print(round(res, 2))