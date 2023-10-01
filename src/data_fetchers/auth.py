import aiohttp


# TODO ДОПИСАТЬ ХУЙ ЗНАЕТ ЧТО ТУТ ПОЛУЧАТЬ
async def user_login(user_id=872687341):
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


# TODO ТУТ ТОЖЕ САМОЕ ЧЕ КАВО КУДА ГДЕ ТОКЕНЫ ВАХУИ
async def user_signup(user_id = 872687341):
    url = 'https://api.dlsky.site/api/v1/signup'

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

