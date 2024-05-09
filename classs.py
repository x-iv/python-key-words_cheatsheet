class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def work(self) -> None:
        print(f'{self.name} is working')
        