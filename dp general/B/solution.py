n = int(input())
h1 = list(map(int, input().split()))
h2 = list(map(int, input().split()))
t = h1[-1]
b = h2[-1]

for i in range(n - 2, -1, -1):
    ct = h1[i] + b
    cb = h2[i] + t
    t = max(ct, t)
    b = max(cb, b)
print(max(t, b))