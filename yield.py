from typing import Generator
def generate_numbers(limit: int) -> Generator:
    for i in range(0, limit):
        yield i

numbers: Generator = generate_numbers(limit=10)
print(next(numbers))
print(list(numbers))
