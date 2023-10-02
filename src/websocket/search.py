import websockets
from websockets.exceptions import ConnectionClosedOK

import config


# TODO Дописать шаблон
async def run_search_products(search_input, telegram_user_id):
    async with websockets.connect(f'ws://dlsky.site:49407/api/v1/analysis/ws/search?'
                                  f'search_input={search_input}',
                                  extra_headers={"X-API-Key": config.API_KEY,
                                                 "Telegram-User-Id": telegram_user_id},
                                  max_size=50000000
                                  ) as websocket:
        try:
            msg: str = await websocket.recv()
            """
            Сообщение формата - найденные продукты:
            [
                {
                    "fullname": "str",
                    "image_url": "HttpUrl",
                    "name_id": "str"
                }
            ]
            """
            return msg

        except ConnectionClosedOK as ex:
            print(f"Ошибка: {ex.code} - {ex.reason}")
            return None


# TODO Юзаем его после run_search_produtcs
async def run_pipeline_analysis(product_name_id: str, telegram_user_id: int):
    async with websockets.connect(f'ws://dlsky.site:49407/api/v1/analysis/ws/pipeline_analysis?'
                                  f'product_name_id={product_name_id}',
                                  extra_headers={"X-API-Key": config.API_KEY,
                                                 "Telegram-User-Id": telegram_user_id},
                                  max_size=50000000
                                  ) as websocket:
        try:
            msg_pipeline_id: str = await websocket.recv()
            pipeline_id: str = msg_pipeline_id.split(": ")[1]
            msg_report_id: str = await websocket.recv()
            report_id: str = msg_report_id.split(": ")[1]
            msg_pipeline: str = await websocket.recv()
            """
            msg_pipeline - сообщение формата:
            [
                {
                    "analysis_task_id": "UUID4",
                    "analysis_title": "str",
                    "analysis_type": "AnalysisType",
                    "visualization_html_task_id": "UUID4",
                    "visualization_html_title": "str",
                    "visualization_image_task_id": "UUID4",
                    "visualization_image_title": "str"
                }
            ]
            """
            return pipeline_id, report_id, msg_pipeline  # tuple
        except ConnectionClosedOK as ex:
            print(f"Ошибка: {ex.code} - {ex.reason}")
            return None


# TODO Юзаем его после run_pipeline_anylisis
async def get_task_result(task_id: str, result_type: str, telegram_user_id: int):
    # result_type = text или bytes
    async with websockets.connect(f'ws://dlsky.site:49407/api/v1/analysis/ws/task_result?'
                                  f'task_id={task_id}&'
                                  f'result_type={result_type}',
                                  extra_headers={"X-API-Key": config.API_KEY,
                                                 "Telegram-User-Id": telegram_user_id},
                                  max_size=50000000
                                  ) as websocket:

        try:
            result = await websocket.recv()
            return result
        except ConnectionClosedOK as ex:
            print(f"Ошибка: {ex.code} - {ex.reason}")
            return None


async def save_report(pipeline_id: str, report_id: str, telegram_user_id: int):
    # result_type = text или bytes
    async with websockets.connect(f'ws://dlsky.site:49407/api/v1/analysis/ws/save_report?'
                                  f'pipeline_id={pipeline_id}&'
                                  f'report_id={report_id}',
                                  extra_headers={"X-API-Key": config.API_KEY,
                                                 "Telegram-User-Id": telegram_user_id},
                                  max_size=50000000
                                  ) as websocket:

        try:
            msg: str = await websocket.recv()
            s = msg.split(": ")[1]
            return s == "success}"
        except ConnectionClosedOK as ex:
            print(f"Ошибка: {ex.code} - {ex.reason}")
            return None
