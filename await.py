import asyncio
from asyncio import Future

async def my_task(no: int) -> dict:
    print('starting task...')
    await asyncio.sleep(2)
    return {'task':no}

async def main() -> None:
    tasks: Future = asyncio.gather(my_task(1),
                                   my_task(2),
                                   my_task(3))
    results: list[dict] = await tasks
    print(results)