name: str='bob'

def change() -> None:
    global name

    name = 'james'

change()
print(name)
