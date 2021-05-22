mod = 7 + 10 ** 9
t, k = map(int, input().split())
x = [1] * 100001
for i in range(k, 100001):
    x[i] = (x[i - 1] + x[i - k]) % mod
for i in range(1, 100001):
    x[i] = (x[i] + x[i - 1]) % mod
for i in range(t):
    a, b = map(int, input().split())
    print((x[b] - x[a - 1]) % mod)
