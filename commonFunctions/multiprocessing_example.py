import asyncio


async def say_hello(name):
    print(f"hi, {name}")
    await asyncio.sleep(1)
    print(f"hi, {name}")


async def gather_jobs(names):
    jobs = (say_hello(name) for name in names)
    gathered = await asyncio.gather(*jobs)
    return gathered


if __name__ == '__main__':
    names = list("abcdefg")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(gather_jobs(names))