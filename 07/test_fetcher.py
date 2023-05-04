import asyncio
import tempfile

import pytest

from fetcher import fetch_all

@pytest.fixture()
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture()
def urls():
    return ['http://httpbin.org/headers',
            'https://jsonplaceholder.typicode.com/posts/1']


@pytest.fixture()
def urls_file():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write('http://httpbin.org/headers\n'
                'https://jsonplaceholder.typicode.com/posts/1\n')
        yield f.name


@pytest.mark.asyncio
async def test_fetch_all(urls):
    results = await fetch_all(urls, 2)
    assert len(results) == len(urls)


@pytest.mark.asyncio
async def test_fetch_all_from_file(urls_file):
    with open(urls_file) as f:
        urls = [line.strip() for line in f.readlines()]

    results = await fetch_all(urls, 2)
    assert len(results) == len(urls)
