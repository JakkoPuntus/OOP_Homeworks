n = int(input())
s = ''
while len(s) < n:
    s = s + input()

c = 0

for i in range(n):
    if s[i] == '<':
        c += s[0:i].count('>')

print(c)
