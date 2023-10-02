import json
from io import IOBase

import websockets
from websockets.exceptions import ConnectionClosedOK
from aiogram.types import InputFile

import config


# TODO run_visualise_analysis_value_category
async def run_visualise_analysis_value_category(json_data: str,
                                                telegram_user_id: int,
                                                title: str,
                                                title_object_count: str,
                                                title_analysis_value: str):
    async with websockets.connect(f'ws://dlsky.site:49407/api/v1/analysis/ws/visualise_analysis_value_category?'
                                  f'vis_type=image&'
                                  f'title={title}&'
                                  f'title_object_count={title_object_count}&'
                                  f'title_analysis_value={title_analysis_value}',
                                  extra_headers={"X-API-Key": config.API_KEY,
                                                 "Telegram-User-Id": telegram_user_id},
                                  max_size=50000000
                                  ) as websocket:
        try:
            await websocket.send(json_data)
            image = await websocket.recv()
            # Не уверен, что нужно так писать, нужен объект, который будем отдавать в telegram
            return InputFile(IOBase(image), filename=f"{title}.png")

        except ConnectionClosedOK as ex:
            print(f"Ошибка: {ex.code} - {ex.reason}")
            return None


# TODO  run_visualise_analysis_value_region
async def run_visualise_analysis_value_region(json_data: str,
                                              telegram_user_id: int,
                                              title: str,
                                              title_object_count: str,
                                              title_analysis_value: str):
    async with websockets.connect(f'ws://dlsky.site:49407/api/v1/analysis/ws/visualise_analysis_value_region?'
                                  f'vis_type=image&'
                                  f'title={title}&'
                                  f'title_object_count={title_object_count}&'
                                  f'title_analysis_value={title_analysis_value}',
                                  extra_headers={"X-API-Key": config.API_KEY,
                                                 "Telegram-User-Id": telegram_user_id},
                                  max_size=50000000
                                  ) as websocket:
        try:
            await websocket.send(json_data)
            image = await websocket.recv()
            # Не уверен, что нужно так писать, нужен объект, который будем отдавать в telegram
            return InputFile(IOBase(image), filename=f"{title}.png")

        except ConnectionClosedOK as ex:
            print(f"Ошибка: {ex.code} - {ex.reason}")
            return None


# TODO  run_visualise_histogram
async def run_visualise_histogram(json_data: str,
                                  telegram_user_id: int,
                                  title: str,
                                  title_object_count: str,
                                  title_analysis_value: str):
    async with websockets.connect(f'ws://dlsky.site:49407/api/v1/analysis/ws/visualise_histogram?'
                                  f'vis_type=image&'
                                  f'title={title}&'
                                  f'title_object_count={title_object_count}&'
                                  f'title_analysis_value={title_analysis_value}',
                                  extra_headers={"X-API-Key": config.API_KEY,
                                                 "Telegram-User-Id": telegram_user_id},
                                  max_size=50000000
                                  ) as websocket:
        try:
            await websocket.send(json_data)
            image = await websocket.recv()
            # Не уверен, что нужно так писать, нужен объект, который будем отдавать в telegram
            return InputFile(IOBase(image), filename=f"{title}.png")

        except ConnectionClosedOK as ex:
            print(f"Ошибка: {ex.code} - {ex.reason}")
            return None


# TODO  run_visualise_quantity_category
async def run_visualise_histogram(json_data: str,
                                  telegram_user_id: int,
                                  title: str,
                                  title_object_count: str):
    async with websockets.connect(f'ws://dlsky.site:49407/api/v1/analysis/ws/visualise_quantity_category?'
                                  f'vis_type=image&'
                                  f'title={title}&'
                                  f'title_object_count={title_object_count}',
                                  extra_headers={"X-API-Key": config.API_KEY,
                                                 "Telegram-User-Id": telegram_user_id},
                                  max_size=50000000
                                  ) as websocket:
        try:
            await websocket.send(json_data)
            image = await websocket.recv()
            # Не уверен, что нужно так писать, нужен объект, который будем отдавать в telegram
            return InputFile(IOBase(image), filename=f"{title}.png")

        except ConnectionClosedOK as ex:
            print(f"Ошибка: {ex.code} - {ex.reason}")
            return None
