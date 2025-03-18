import asyncio
import random
import time

async def task(i):
    await asyncio.sleep(random.randint(2,5))
    print(f"task {i} completed")


async def main():
    task_count = 5

    tasks = [task(i) for i in range(task_count)]

    await asyncio.gather(*tasks)


asyncio.run(main())   