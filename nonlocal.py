def fun() -> None:
    item: str = 'can'

    def inner_fun() -> None:
        nonlocal item
        item = 'apple'
        print(item)

    inner_fun()
fun()
    