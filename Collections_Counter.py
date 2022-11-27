from collections import Counter

n = int(input())
s = input().split()
s = dict(Counter(s))
c = int(input())
m = 0
for i in range(c):
    x = input().split()
    if x[0] in s:
        if s[x[0]] >= 1:
            m += int(x[1])
            s[x[0]] -= 1
print(m)
