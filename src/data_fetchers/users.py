import aiohttp
import asyncio
import json

from config import API_KEY


# TODO ХУЙ ПРОССЫШ КАКОГО ВИДА ОТВЕТ И ЧЕ ЕМУ ПЕРЕДАВАТЬ
async def fetch_accept_terms(user_id):
    url = 'https://api.dlsky.site/api/v1/users/accept-terms'

    headers = {'Telegram-User-Id': str(user_id),
               'X-API-Key': API_KEY}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.text()
                json_data = json.loads(data)
                print(f"Все ок")
                return True
            else:
                print(f"Говно запрос: {response.status}")
                return False


async def fetch_user(user_id):
    url = 'https://api.dlsky.site/api/v1/users/'

    params = {
        'user_id': user_id,
    }

    headers = {'Telegram-User-Id': str(user_id),
               'X-API-Key': API_KEY}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params, ssl=False) as response:
            if response.status == 200:
                data = await response.text()
                json_data = json.loads(data)
                if 'message' in json_data:  # message меняем на название поля ну и ваще я ебу че там надо, имя тип
                    # еще чет, доделать надо
                    extracted_string = json_data['message']
                    print(f"Извлеченная строка: {extracted_string}")
                    print(json_data)
                else:
                    print("Указанный ключ не найден в JSON-ответе.")
            else:
                print(f"Говно запрос: {response.status}")


async def fetch_user_by_username(user_id, username):
    url = 'https://api.dlsky.site/api/v1/users/search'

    params = {
        'q': username,
    }

    headers = {'Telegram-User-Id': str(user_id),
               'X-API-Key': API_KEY}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params, ssl=False) as response:
            if response.status == 200:
                data = await response.text()
                json_data = json.loads(data)
                print(json_data)

                user_info = [json_data[0]['username'], json_data[0]['role'], json_data[0]['tokens'], json_data[0]['id']]
                # for item in json_data:
                #     extracted_data = {
                #         item['tokens'],
                #         item['username'],
                #         item['role']
                #     }
                #    user_info.append(extracted_data)

                print(user_info)

                # # Создаем пустой список для массива
                # my_array = []
                #
                # # Добавляем элементы из исходной структуры данных в массив
                # for item in user_info:
                #     my_array.append(list(item))
                #
                # # my_array теперь содержит элементы в виде массива
                # print(my_array)

                return user_info
                # if 'message' in json_data:  # message меняем на название поля ну и ваще я ебу че там надо, имя тип
                #     # еще чет, доделать надо
                #     extracted_string = json_data['message']
                #     print(f"Извлеченная строка: {extracted_string}")
                #     print(json_data)
                # else:
                #     print("Указанный ключ не найден в JSON-ответе.")
            else:
                print(f"Говно запрос: {response.status}")


async def fetch_user_tokens(user_id):
    url = 'https://api.dlsky.site/api/v1/users/'

    params = {
        'user_id': user_id,
    }

    headers = {'Telegram-User-Id': str(user_id),
               'X-API-Key': API_KEY}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params, ssl=False) as response:
            if response.status == 200:
                data = await response.text()
                json_data = json.loads(data)
                if 'tokens' in json_data:  # message меняем на название поля ну и ваще я ебу че там надо, имя тип
                    # еще чет, доделать надо
                    print(f"Извлеченная строка: {json_data['tokens']}")
                    return json_data['tokens']
                else:
                    print("Указанный ключ не найден в JSON-ответе.")
            else:
                print(f"Говно запрос: {response.status}")
