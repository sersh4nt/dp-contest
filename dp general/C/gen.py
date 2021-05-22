import random

test = 22

n = 100000
ar = []
for i in range(n):
    ar.append(random.randint(0, 100000))

a = [0] * 100001
for i in ar:
    a[i] += 1

dp = [0] * 100001
dp[1] = a[1]
for i in range(2, 100001):
    dp[i] = max(a[i] * i + dp[i - 2], dp[i - 1])
ans = dp[-1]

with open(f'tests/{test}', 'w') as f:
    f.write(f'{n}\n')
    for t in ar:
        f.write(f'{t} ')

with open(f'tests/{test}a', 'w') as f:
    f.write(str(ans))