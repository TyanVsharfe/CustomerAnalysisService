import json
import websockets


# TODO Шаблон, сделать для всего анализа
async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f">>> {name}")

        greeting = await websocket.recv()
        print(f"<<< {greeting}")


# TODO Дописать шаблон
async def run_search_products():
    async with websockets.connect('ws://сервер/websocket/путь') as websocket:
        # Запрос в формате JSON
        request_data = {
            "method": "run_search_products",
            "args": ["Чайник Т-1000"]
        }

        # Отправьте запрос на сервер
        await websocket.send(json.dumps(request_data))

        # Получите ответ от сервера
        response = await websocket.recv()
        print(f"Ответ от сервера: {response}")


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
