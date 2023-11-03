l, h, w = map(int, input().split())

G = 9.81

h /= 100
l /= 100
w /= 60


if (h <= l/2):
    print('butter')
else:
    h -= l/2
    t = ((2*h) / G)**0.5

    a = (w * t)
    a -= int(a)
    
    if a < 0.25 or a > 0.75:
        print('butter')
    else:
        print('bread')
