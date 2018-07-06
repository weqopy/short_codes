import asyncio
import random


async def MyCoroutine(id):
    process_time = random.randint(1, 5)
    await asyncio.sleep(process_time)
    print(f" 协程：{id}，执行完毕。用时：{process_time} 秒。")


async def main():
    tasks = [asyncio.ensure_future(MyCoroutine(i)) for i in range(20)]
    await asyncio.gather(*tasks)


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
