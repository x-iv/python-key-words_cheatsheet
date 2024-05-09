from typing import Callable, Any

def print_results(func: Callable, elements:list[Any]):
          for elem in elements:
            print(func(elem))

print_results(lambda x: x * 2, elements=[1,2,2,4])
