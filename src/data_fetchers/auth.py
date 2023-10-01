import aiohttp

from config import API_KEY


async def user_login(user_id):
    url = 'https://api.dlsky.site/api/v1/login'

    params = {
        'user_id': user_id,
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            if response.status == 200:
                data = await response.json()
                # В переменной data есть весь JSON-ответ как словарь Python
                print(data)
            else:
                print(f"Ошибка при выполнении запроса: {response.status}")


# Авторизация первый раз (если второй и более пох сюда же скипаем 409 ошибку и норм)
async def user_signup(return_to, user_id, first_name, username, is_accept_terms, last_name="None", photo_url="None"):
    url = 'https://api.dlsky.site/api/v1/signup'
    headers = {'Telegram-User-Id': str(user_id),
               'X-API-Key': API_KEY}

    params = {
        'return_to': return_to,
        'id': user_id,
        'first_name': first_name,
        'last_name': last_name,
        'username': username,
        'photo_url': photo_url,
        'is_accept_terms': is_accept_terms
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params, ssl=False) as response:
            if response.status == 200:
                data = await response.json()
                # В переменной data есть весь JSON-ответ как словарь Python
                print(data)
            elif response.status == 409:
                return
            else:
                print(f"Ошибка при выполнении запроса: {response.status} {response.content}")


