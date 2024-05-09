from typing import Never

def dangerous_code() -> Never:
    raise ValueError('bad bad')

try:
    dangerous_code()
except ValueError as e:
    print(f'bad bad: !"{e}"')
    
finally:
    print('finally: pp')
    