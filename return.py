from datetime import datetime

def get_time() -> str:
    now: datetime = datetime.now()
    return f'{now:%r}'
print(get_time)
