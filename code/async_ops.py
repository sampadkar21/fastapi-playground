import asyncio
import time

def printing(name):
    i = 3
    while i > 0:
        print(f"{name}: {i}")
        time.sleep(1)
        i -= 1

start = time.perf_counter()

printing("A")
printing("B")

print(f"Time = {time.perf_counter() - start:.2f}s")
        
async def asyn_printing(name):
    i = 3
    while i > 0:
        print(f"{name}: {i}")
        await asyncio.sleep(1)
        i -= 1

async def main():
    await asyncio.gather(
        asyn_printing("A"),
        asyn_printing("B")
    )

start = time.perf_counter()

asyncio.run(main())

print(f"Time = {time.perf_counter() - start:.2f}s")