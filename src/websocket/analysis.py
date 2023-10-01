import json
import websockets


# TODO run_visualise_analysis_value_category
async def run_visualise_analysis_value_category():
    async with websockets.connect('ws://сервер/websocket/путь') as websocket:
        # Запрос в формате JSON
        request_data = {
            "method": "run_visualise_analysis_value_category",
            "args": [""]
        }

        await websocket.send(json.dumps(request_data))

        # Ответ от сервера
        response = await websocket.recv()
        print(f"Ответ от сервера: {response}")


# TODO  run_visualise_analysis_value_region
async def run_visualise_analysis_value_region():
    async with websockets.connect('ws://сервер/websocket/путь') as websocket:
        # Запрос в формате JSON
        request_data = {
            "method": "run_visualise_analysis_value_region",
            "args": [""]
        }

        await websocket.send(json.dumps(request_data))

        # Ответ от сервера
        response = await websocket.recv()
        print(f"Ответ от сервера: {response}")


# TODO  run_visualise_histogram
async def run_visualise_histogram():
    async with websockets.connect('ws://сервер/websocket/путь') as websocket:
        # Запрос в формате JSON
        request_data = {
            "method": "run_visualise_analysis_value_region",
            "args": [""]
        }

        await websocket.send(json.dumps(request_data))

        # Ответ от сервера
        response = await websocket.recv()
        print(f"Ответ от сервера: {response}")


# TODO  run_visualise_quantity_category
async def run_visualise_quantity_category():
    async with websockets.connect('ws://сервер/websocket/путь') as websocket:
        # Запрос в формате JSON
        request_data = {
            "method": "run_visualise_quantity_category",
            "args": [""]
        }

        await websocket.send(json.dumps(request_data))

        # Ответ от сервера
        response = await websocket.recv()
        print(f"Ответ от сервера: {response}")