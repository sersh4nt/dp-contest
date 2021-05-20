test = 13

n = 99999
a = [99999] * n

with open(f'tests/{test}', 'w') as f:
    f.write(f'{n}\n')
    for t in a:
        f.write(f'{t} ')

with open(f'tests/{test}a', 'w') as f:
    f.write(str(9999800001))