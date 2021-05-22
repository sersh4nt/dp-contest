import random

test = 7

q = 200
sred = 1000
spread = 5

strs = [str(q)]
anss = []

maxn = 200000

for i in range(q):
    if q == 1:
        n = 200000
    else:
        n = min(random.randint(sred - spread, sred + spread), maxn)
        maxn -= n
    t1 = ''.join((random.choice('123456') for i in range(n)))
    t2 = ''.join((random.choice('123456') for i in range(n)))
    strs.append(str(n))
    strs.append(t1)
    strs.append(t2)

    s = [''] * 2
    s[0] = t1
    s[1] = t2
    p = 0
    for i in range(n):
        if s[p][i] > '2':
            p = 1 - p
            if s[p][i] <= '2':
                p = 0
                break
    anss.append('YES' if p else 'NO')

with open(f'tests/{test}', 'w') as f:
    for s in strs:
        f.write(f'{s}\n')

with open(f'tests/{test}a', 'w') as f:
    for s in anss:
        f.write(f'{s}\n')