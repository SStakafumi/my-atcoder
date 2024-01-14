n, x = map(int, input().split())
s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

i = x//n
a = x%n

if x%n == 0:
    print(s[i-1])
else:
    print(s[i])
