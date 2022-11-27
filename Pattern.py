a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n = int(input())
a = a[:n][::-1]
l = []
for i in range(len(a)):
    s = a[: i + 1]
    s = s + s[-2::-1]
    l.append("-".join(s))
x = list(range(0, n * 2 - 1, 2))[::-1]

for i in range(n):
    print("-" * x[i], l[i], "-" * x[i], sep="")
for i in range(n - 2, -1, -1):
    print("-" * x[i], l[i], "-" * x[i], sep="")
