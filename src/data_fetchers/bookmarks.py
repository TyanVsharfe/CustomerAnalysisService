import aiohttp
import asyncio
import json

from config import API_KEY


async def fetch_all_bookmarks(user_id):
    url = 'https://api.dlsky.site/api/v1/bookmarks/all'

    headers = {'Telegram-User-Id': str(user_id),
               'X-API-Key': API_KEY}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, ssl=False) as response:
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
        async with session.get(url, params=params, ssl=False) as response:
            if response.status == 200:
                data = await response.json()
                # В переменной data есть весь JSON-ответ как словарь Python
                print(data)
            else:
                print(f"Ошибка при выполнении запроса: {response.status}")