import numpy as np

test = 20

n = 100000
a = np.random.randint(0, 1000000000, n, dtype=np.int64)
b = np.random.randint(0, 1000000000, n, dtype=np.int64)

mxa, mxb = 0, 0
for x, y in zip(a, b):
    mxa, mxb = max(mxa, mxb + x), max(mxb, mxa + y)
ans = (max(mxa, mxb))

with open(f'tests/{test}', 'w') as f:
    f.write(f'{n}\n')
    for t in a:
        f.write(f'{t} ')
    f.write('\n')
    for t in b:
        f.write(f'{t} ')

with open(f'tests/{test}a', 'w') as f:
    f.write(str(ans))