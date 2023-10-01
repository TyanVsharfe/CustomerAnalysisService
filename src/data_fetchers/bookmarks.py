import aiohttp
import asyncio
import json


async def fetch_all_bookmarks(bookmark_id=8334341):
    url = 'https://api.dlsky.site/api/v1/bookmarks/all'

    params = {
        'bookmark_id': bookmark_id,
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                # В переменной data есть весь JSON-ответ как словарь Python
                print(data)
            else:
                print(f"Ошибка при выполнении запроса: {response.status}")


async def fetch_bookmark(bookmark_id=872687341):
    url = 'https://api.dlsky.site/api/v1/bookmarks/'

    params = {
        'bookmark_id': bookmark_id,
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                # В переменной data есть весь JSON-ответ как словарь Python
                print(data)
            else:
                print(f"Ошибка при выполнении запроса: {response.status}")