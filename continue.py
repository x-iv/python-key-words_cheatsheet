names: list[str] = ['tom', 'bob', 'james']

for name in names:
    if name == 'bob':
        print('we do not say bob')
        continue

    print(f'hello, {name}!')
