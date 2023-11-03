n = int(input())

ranges = {
    (0, 5): 'few',
    (5, 10): 'several',
    (10, 20): 'pack',
    (20, 50): 'lots',
    (50, 100): 'horde',
    (100, 250): 'throng',
    (250, 500): 'swarm',
    (500, 1000): 'zounds',
    (1000, 2001): 'legion'
}

for key, value in ranges.items():
    if key[0] <= n < key[1]:
        print(value)
        break