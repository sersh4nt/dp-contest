import random

test = 25

n = 500000
leng = None

strs = [str(n)]
anss = []

for i in range(n):
    if not leng:
        le = random.randint(1, 2)
    else:
        # abcdefghijklmopqrstvuwxyz
        le = leng
    stri = 'id'.join((random.choice('abcdefghijklmopqrstvuwxyz') for j in range(3)))
    strs.append(stri)

l = strs[1:]
dp = []
for i in range(26):
    dp.append([-999999999] * 26)
ans = 0
for i in range(26):
    dp[i][i] = 0
    for j in range(n):
        first = ord(l[j][0]) - 97
        ln = len(l[j])
        last = ord(l[j][ln - 1]) - 97
        dp[i][last] = max(dp[i][last], dp[i][first] + ln)
    ans = max(ans, dp[i][i])

anss.append(str(ans))

with open(f'tests/{test}', 'w') as f:
    for s in strs:
        f.write(f'{s}\n')

with open(f'tests/{test}a', 'w') as f:
    for s in anss:
        f.write(f'{s}\n')