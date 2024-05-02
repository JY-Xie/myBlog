import asyncio
import aiohttp

async def make_request(session):
    url = 'http://192.168.1.126:8888/'
    async with session.get(url) as response:
        return await response.text()

async def send_requests():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(100000):
            task = asyncio.ensure_future(make_request(session))
            tasks.append(task)
        await asyncio.gather(*tasks)

async def main():
    while True:
        await send_requests()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
