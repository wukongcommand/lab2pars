data = {}

with open('conf') as f:
    for line in f:
        line = line.strip('\n')
        if line.startswith('#') or line.startswith(';'):
            continue
        elif ' ' in line:
            key, value = line.split(' ', 1)
            data[key] = value
        else:
            data[line] = None


while True:
    line = input()
    if line.startswith('get param '):
        key = line[10:]
        try:
            print(key, ':', data[key] or '(данные отсутствуют)')
        except KeyError:
            print('Ключ отсутствует')

        print('Продолжить? (Да/Нет)')
        should_continue = input().lower()
        if should_continue == 'да':
            continue
        elif should_continue == 'нет':
            print('Осуществляется выход из программы')
            break
        else:
            print('(Да/Нет)')
