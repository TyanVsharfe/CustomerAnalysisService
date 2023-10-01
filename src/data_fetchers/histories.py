import aiohttp
import asyncio
import json

from config import API_KEY


async def fetch_all_history(user_id):
    url = 'https://api.dlsky.site/api/v1/history/all'

    headers = {'Telegram-User-Id': str(user_id),
               'X-API-Key': API_KEY}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                # В переменной data с есть весь JSON-ответ как словарь Python
                print(data)
            else:
                print(f"Ошибка при выполнении запроса: {response.status}")


async def send_history(title="historyOne",  history_url="https://history/2567"):
    url = 'https://api.dlsky.site/api/v1/history/'

    payload = {
        'title': title,
        'url': history_url
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


async def delete_all_history(user_id):
    url = 'https://api.dlsky.site/api/v1/history/all'

    headers = {'Telegram-User-Id': str(user_id),
               'X-API-Key': API_KEY}

    async with aiohttp.ClientSession() as session:
        async with session.delete(url, headers=headers, ssl=False) as response:
            if response.status == 204:
                print("История успешно выполнен.")
            else:
                print(f"Ошибка при удалении истории пользователя: {response.status}")
