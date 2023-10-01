import aiohttp
import asyncio

from config import API_KEY


async def ban_user(user_id):
    url = 'https://api.dlsky.site/api/v1/admin/ban'

    payload = {
        'user_id': user_id
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, ssl=False) as response:
            if response.status == 200:
                print(f"Пользователь с ID {user_id} забанен.")
            else:
                print(f"Ошибка при выполнении POST-запроса: {response.status}")


async def change_user_role(user_id, header_id, role):
    url = 'https://api.dlsky.site/api/v1/admin/role'

    payload = {
        'user_id': user_id,
        'role': role
    }

    headers = {'Telegram-User-Id': str(header_id),
               'X-API-Key': API_KEY}

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, ssl=False) as response:
            if response.status == 200:
                print(f"Пользователь с ID {user_id} получил роль '{role}'.")
            else:
                print(f"Ошибка при выполнении POST-запроса: {response.status}")


async def add_user_token(user_id=872687341, tokens=100):
    url = 'https://api.dlsky.site/api/v1/admin/token'

    payload = {
        'user_id': user_id,
        'tokens': tokens
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload, ssl=False) as response:
            if response.status == 200:
                print(f"Пользователь с ID {user_id} получил '{tokens}' токенов.")
            else:
                print(f"Ошибка при выполнении POST-запроса: {response.status}")


async def fetch_user_activity(user_id=872687341):
    url = 'https://api.dlsky.site/api/v1/admin/activity'

    params = {
        'user_id': user_id,
    }

    headers = {'Telegram-User-Id': str(user_id),
               'X-API-Key': API_KEY}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params, ssl=False) as response:
            if response.status == 200:
                data = await response.json()
                print(f"Данные активности пользователя с ID {user_id}: {data}")
            else:
                print(f"Ошибка при выполнении GET-запроса: {response.status}")


async def fetch_all_user_activity(user_id):
    url = 'https://api.dlsky.site/api/v1/admin/activity/all'

    headers = {'Telegram-User-Id': str(user_id),
               'X-API-Key': API_KEY}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, ssl=False) as response:
            if response.status == 200:
                data = await response.json()
                # В переменной data есть весь JSON-ответ как словарь Python
                print(data)
                return data
            else:
                print(f"Ошибка при выполнении запроса: {response.status}")


async def fetch_new_users_stats(user_id):
    url = 'https://api.dlsky.site/api/v1/admin/stats'

    headers = {'Telegram-User-Id': str(user_id),
               'X-API-Key': API_KEY}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, ssl=False) as response:
            if response.status == 200:
                data = await response.json()
                # В переменной data есть весь JSON-ответ как словарь Python
                print(data)
                return data
            else:
                print(f"Ошибка при выполнении запроса: {response.status}")
