import time

connect: bool = True
i: int = 1

while connect:
    if i == 3:
        connect = False

    print(f'connect for:{i}s')
    time.sleep(1)
    i += 1

print('lost...')
