import aiohttp
import asyncio
import json


async def fetch_all_history():
    url = 'https://api.dlsky.site/api/v1/history/all'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                # В переменной data с есть весь JSON-ответ как словарь Python
                print(data)
            else:
                print(f"Ошибка при выполнении запроса: {response.status}")


async def fetch_history():
    url = 'https://api.dlsky.site/api/v1/history/'

    payload = {
        # Тело POST-запроса, надо или нет хз
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            if response.status == 200:
                data = await response.json()
                if 'title' in data and 'url' in data:
                    title = data['title']
                    url = data['url']
                    print(f"Title: {title}")
                    print(f"URL: {url}")
                else:
                    print("Нету полей 'title' или 'url'.")
            else:
                print(f"Ошибка при выполнении POST-запроса: {response.status}")


async def delete_data():
    url = 'https://api.dlsky.site/api/v1/history/all'

    async with aiohttp.ClientSession() as session:
        async with session.delete(url) as response:
            if response.status == 204:
                print("История успешно выполнен.")
            else:
                print(f"Ошибка при удалении истории пользователя: {response.status}")
