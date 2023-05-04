import argparse
import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def bound_fetch(sem, session, url):
    async with sem:
        return await fetch(session, url)


async def fetch_all(urls, limit):
    tasks = []
    sem = asyncio.Semaphore(limit)

    async with aiohttp.ClientSession() as session:
        for url in urls:
            task = asyncio.ensure_future(bound_fetch(sem, session, url))
            tasks.append(task)

        results = await asyncio.gather(*tasks)
        return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Fetcher script for asynchronous URL requests')
    parser.add_argument('limit', type=int, help='Limit for number of allowed requests')
    parser.add_argument('urlsfile', type=str, help='Path to file with URLs')

    args = parser.parse_args()

    with open(args.urlsfile) as f:
        urls = [line.strip() for line in f.readlines()]

    loop = asyncio.get_event_loop()
    results = loop.run_until_complete(fetch_all(urls, args.limit))
    print(results)
