import aiohttp
import asyncio
import json


# TODO ХУЙ ПРОССЫШ КАКОГО ВИДА ОТВЕТ И ЧЕ ЕМУ ПЕРЕДАВАТЬ
async def fetch_accept_terms():
    url = 'https://api.dlsky.site/api/v1/users/accept-terms'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.text()
                json_data = json.loads(data)
                if 'message' in json_data:  # message меняем на название поля ну и ваще я ебу че там надо, имя тип
                    # еще чет, доделать надо
                    extracted_string = json_data['message']
                    print(f"Извлеченная строка: {extracted_string}")
                else:
                    print("Указанный ключ не найден в JSON-ответе.")
            else:
                print(f"Говно запрос: {response.status}")
