import aiohttp
import asyncio


async def ban_user(user_id=872687341):
    url = 'https://api.dlsky.site/api/v1/admin/ban'

    payload = {
        'user_id': user_id
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload) as response:
            if response.status == 200:
                print(f"Пользователь с ID {user_id} забанен.")
            else:
                print(f"Ошибка при выполнении POST-запроса: {response.status}")


async def change_user_role(user_id=872687341, role="user"):
    url = 'https://api.dlsky.site/api/v1/admin/role'

    payload = {
        'user_id': user_id,
        'role': role
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=payload) as response:
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
        async with session.post(url, data=payload) as response:
            if response.status == 200:
                print(f"Пользователь с ID {user_id} получил '{tokens}' токенов.")
            else:
                print(f"Ошибка при выполнении POST-запроса: {response.status}")


async def fetch_user_activity(user_id=872687341):
    url = 'https://api.dlsky.site/api/v1/admin/activity'

    params = {
        'user_id': user_id,
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                print(f"Данные активности пользователя с ID {user_id}: {data}")
            else:
                print(f"Ошибка при выполнении GET-запроса: {response.status}")


async def fetch_all_user_activity():
    url = 'https://api.dlsky.site/api/v1/admin/activity/all'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                # В переменной data есть весь JSON-ответ как словарь Python
                print(data)
            else:
                print(f"Ошибка при выполнении запроса: {response.status}")


async def fetch_new_users_stats():
    url = 'https://api.dlsky.site/api/v1/admin/stats'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                # В переменной data есть весь JSON-ответ как словарь Python
                print(data)
            else:
                print(f"Ошибка при выполнении запроса: {response.status}")
