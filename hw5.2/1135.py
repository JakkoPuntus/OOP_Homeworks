n = int(input())
s = ''
while len(s) < n:
    s = s + input()

c = 0
left = 0

for i in range(n):
    if s[i] == '<':
        c += len(s[:i]) - left
        left += 1

print(c)
