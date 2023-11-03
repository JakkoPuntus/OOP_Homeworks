n, x = map(int, input().split())

obstacles = list(map(int, input().split()))

positive_obstacles = [i for i in obstacles if i > 0]
negative_obstacles = [i for i in obstacles if i < 0]


if any(i>x for i in negative_obstacles) or any(i<x for i in positive_obstacles):
    print('Impossible')

elif x < 0:
    print(2 * min(positive_obstacles) + abs(x), abs(x))
elif x > 0:
    print(x, max(negative_obstacles) * -2 + x)