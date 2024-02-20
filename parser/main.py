import requests
import json
from anti_useragent import UserAgent
import time
import concurrent.futures
from data import data_,col_potokov
from loguru import logger
from service import RebbitMQ

c = 0
logger.add('debug.log',format="{time} {level} {message}",level='DEBUG',rotation='100 MB',compression='zip')

def start(tupl: tuple):
    name,price = tupl[0],float(tupl[1])
    global c

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'X-Client-App': 'web',
        'traceparent': '00-c518993e8e67dd15a917fe97067735f7-c6fd71b0dd9858d5-01',
        'Alt-Used': 'cs.money',
        'Connection': 'keep-alive',
        'Referer': 'https://cs.money/market/buy/',
        # 'Cookie': 'region=Grodnenskaya; cc_service2={%22services%22:[%22necessary%22%2C%22gtm%22%2C%22ym%22%2C%22amplitude%22%2C%22gleam%22%2C%22esputnik%22%2C%22hotjar%22%2C%22userSesDatToAnalytic%22%2C%22userSesDatToMarketing%22%2C%22cardVisualSize%22]%2C%22acceptanceDate%22:1708281882726%2C%22revision%22:0}; group_id=d42c470d-7dea-4e74-add3-104d15440d4e; sc=5130948A-2EFB-54FC-AF9F-339C47DB13B2; _gcl_au=1.1.42814056.1708281883; _ga_HY7CCPCD7H=GS1.1.1708406151.3.1.1708406732.60.0.0; _ga=GA1.1.894398092.1708281884; cf_clearance=OjXPtZSxmcGvvvs8cWv8uYImO58e4vboOBKBS61wm8s-1708406149-1.0-AWKlDIMlvQn6DzCzb16wKSkLtbewwWeLGbhJI4Qa5VUoOrlrBGlq4aoP+Lp6CbhjhZLZ5bft4KOcj2uokBbXRL4=; _ga_CFRN8YJV66=GS1.1.1708406151.3.0.1708406151.0.0.0; ouid=60299031_1734003192; _ym_uid=1708281886412497733; _ym_d=1708281886; _scid=eafb7b8f-21ae-4a77-99ec-d91424da7f0a; amplitude_id_c14fa5162b6e034d1c3b12854f3a26f5cs.money=eyJkZXZpY2VJZCI6IjMwYzc3N2U0LTBmZGMtNDVhMi1hYzM5LTQ1ZDhjOTc3MWU5MVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTcwODQwNjE0NzUwNywibGFzdEV2ZW50VGltZSI6MTcwODQwNjczMjYwMiwiZXZlbnRJZCI6MjksImlkZW50aWZ5SWQiOjM3LCJzZXF1ZW5jZU51bWJlciI6NjZ9; _hjSessionUser_2848248=eyJpZCI6IjU1N2EwYmJhLTAzYWItNWJlMy1hNTg2LTNhMTY4NjhiOWZhNyIsImNyZWF0ZWQiOjE3MDgyODE4ODY0ODAsImV4aXN0aW5nIjp0cnVlfQ==; _sctr=1%7C1708203600000; new_language=en; _hjHasCachedUserAttributes=true; _ym_isad=1; onboarding__skin_quick_view=false; isAnalyticEventsLimit=true; _hjSession_2848248=eyJpZCI6IjdlOWU1ODQ1LTZjYTQtNGFhNS05NTI1LWZkY2I5NmU5MDViNiIsImMiOjE3MDg0MDYxNDc3MzUsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _scid_r=eafb7b8f-21ae-4a77-99ec-d91424da7f0a; _uetsid=c962ac70ce8d11eeb5d901acd8280a1f; _uetvid=ae42a8205d4f11ee829917d87d31b452; _ym_visorc=b',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
    }
    offset = 0
    batch_size = 60
    while True:
        try:
            params = {
                'limit': '60',
                'name': '',
                'offset': '0',
                'order': 'desc',
                'sort': 'discount',
            }
            params['name'] = name
            hash = []
            response = requests.get('https://cs.money/1.0/market/sell-orders', params=params,headers=headers)
            if response.status_code == 200:
                c += 1
                items = response.json().get('items')
                for item in items:
                    hash.append((item.get('pricing').get('computed'),item.get('asset').get("images").get('steam')))
                lowest_item = min(hash,key=lambda x: x[0])
                logger.info(f'Количество запросов {c}')
                logger.debug(f'Market: {lowest_item[0]}, Json: {lowest_item[1]}')
                if lowest_item[0] <= price:
                    logger.info(f'Нашли скин с низкой ценой! {name}')
                    RebbitMQ.send_message(
                        photo_url=lowest_item[1],
                        name=name,
                        price=lowest_item[0],
                        price_difference=round(price-lowest_item[0],2)
                    )
                    break

            else:
                logger.warning(f'Статус код {response.status_code}')
                break
        except Exception as ex:
            time.sleep(1)
            logger.error(f'Ошибка в парсере {ex} Статус код: {response.status_code}')












if __name__ == '__main__':
    list_ = data_  # сюда вставляешь то что прогоняешь через фор смотри где больше ссылок собрано
    CONNECTIONS = col_potokov  # колличетсво потоков
    out = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
        future_to_url = {executor.submit(start,tupl): tupl for tupl in list_}
        done, _ = concurrent.futures.wait(future_to_url, return_when=concurrent.futures.ALL_COMPLETED)
        for future in done:
            try:
                data = future.result()
            except Exception as exc:
                data = str(type(exc))
            finally:
                print('многопоток завершается')
                out.append(data)
