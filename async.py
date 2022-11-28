import asyncio
import datetime
import random

"""
@asyncio.coroutine
def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        yield from asyncio.sleep(random.randint(0, 5))


loop = asyncio.get_event_loop()

asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))

loop.run_forever()
"""


async def display_date(num, loop):
    end_time = loop.time() + 30.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(10)


# loop = asyncio.get_event_loop()
#
# asyncio.ensure_future(display_date(1, loop))
# asyncio.ensure_future(display_date(2, loop))
#
# loop.run_forever()


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


# loop = asyncio.get_event_loop()
# loop.run_until_complete(factorial('A', 4))

# asyncio.run(factorial('A', 4))

async def main():
    # Запланировать дерево вызовов *конкурентно*:
    await asyncio.gather(
        factorial("A", 10),
        factorial("B", 15),
        factorial("C", 16),
    )

asyncio.run(main())
