import json
import websockets

from config import API_KEY


# TODO Дописать шаблон
async def run_search_products(search_input, user_id):

    headers = {'Telegram-User-Id': str(user_id),
               'X-API-Key': API_KEY}

    async with websockets.connect(f'ws://api.dlsky.site/api/v1/analysis/ws/search?search_input{search_input}',
                                  extra_headers=headers, max_size=5000000) as websocket:

        # Получите ответ от сервера
        response = await websocket.recv()
        print(f"Ответ от сервера: {response}")
        return response


# TODO Юзаем его после run_search_produtcs
async def run_pipeline_analysis():
    async with websockets.connect('ws://сервер/websocket/путь') as websocket:
        # Запрос в формате JSON
        request_data = {
            "method": "run_pipeline_analysis",
            "args": [""]
        }

        await websocket.send(json.dumps(request_data))

        # Получите ответ от сервера
        response = await websocket.recv()
        print(f"Ответ от сервера: {response}")


# TODO Юзаем его после run_pipeline_anylisis
async def get_task_result():
    async with websockets.connect('ws://сервер/websocket/путь') as websocket:
        # Запрос в формате JSON
        request_data = {
            "method": "get_task_result",
            "args": [""]
        }

        await websocket.send(json.dumps(request_data))

        # Ответ от сервера
        response = await websocket.recv()
        print(f"Ответ от сервера: {response}")
