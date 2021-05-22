TASK = 'F'
FOLDER = 'dp general'

with open(f'{FOLDER}/{TASK}/{TASK}.txt', 'r') as f:
    lines = f.readlines()

test = []
ans = []
cnt = 1
i = 0
while i < len(lines):
    if lines[i] == '\n':
        pass
    elif 'Ввод' in lines[i]:
        i += 1
        while 'Вывод' not in lines[i]:
            if lines[i] != '\n':
                test.append(lines[i])
            i += 1
    elif 'Ответ' in lines[i]:
        i += 1
        while 'Протокол тестирования' not in lines[i]:
            if lines[i] != '\n':
                ans.append(lines[i])
            i += 1
        with open(f'{FOLDER}/{TASK}/tests/{cnt}', 'w') as f:
            for t in test:
                f.write(t)
        with open(f'{FOLDER}/{TASK}/tests/{cnt}a', 'w') as f:
            for t in ans:
                f.write(t)
        cnt += 1
        test.clear()
        ans.clear()
    i += 1
