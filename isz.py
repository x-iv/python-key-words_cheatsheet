class fruit:
    ...

apple: fruit = fruit()
other_app = apple

print(apple is other_app)

banana: fruit = fruit()
print(input() is banana)
#compares memorry

print(f'{id(apple)}')
print(f'{id(other_app)}')
print(f'{id(banana)}')
