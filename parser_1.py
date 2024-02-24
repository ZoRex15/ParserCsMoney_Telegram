import requests

from anti_useragent import UserAgent

from parser_settings.data import data_ as info
from loguru import logger
from service.rebbit import RebbitMQ
from database.requests import Database


logger.add('debug.log', format="{time} {level} {message}", level='DEBUG', rotation='100 MB', compression='zip')
ua = UserAgent()

def start(min_price: int | float = 0,max_price: int | float = 0):
    headers = {
        'authority': 'cs.money',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'region=Grodnenskaya; group_id=b62119c5-797f-47f9-8963-0208f5187fd0; cc_service2={%22services%22:[%22necessary%22%2C%22gtm%22%2C%22ym%22%2C%22amplitude%22%2C%22gleam%22%2C%22esputnik%22%2C%22hotjar%22%2C%22userSesDatToAnalytic%22%2C%22userSesDatToMarketing%22%2C%22cardVisualSize%22]%2C%22acceptanceDate%22:1708534353971%2C%22revision%22:0}; _gcl_au=1.1.996797232.1708534356; _hjSessionUser_2848248=eyJpZCI6IjhiMWMyM2MzLTc2M2MtNTA1Zi1hOGEyLWE2ZmU1YTNhMjczNiIsImNyZWF0ZWQiOjE3MDg1MzQzNTU5MTUsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.1.1085143897.1708534356; sc=F16E4144-E979-C8BD-CC14-75FAB188DB32; ouid=3272362712_3726229750; _ym_uid=1708534357629095503; _ym_d=1708534357; _scid=822a2d8f-f0db-4905-a830-d1f2f0de2057; _fbp=fb.1.1708534357459.944632933; _sctr=1%7C1708462800000; _ga_HY7CCPCD7H=deleted; cf_clearance=y4VJWtJt0uDF5N4sfYHww08xnLs9PcnpTGAIc2A2.QM-1708707736-1.0-AU43frJim5qxoqY/5q9iz9JLOjp2a4p6Ah26E1HNjvNeGv5dtmWEb+0k2eEW7BpI8YXHgt66aU35Xhzzhb3zUbg=; _gcl_aw=GCL.1708707739.Cj0KCQiAoeGuBhCBARIsAGfKY7xZ2otSJHClGIlOsJXK4VXemBeJYXeuX65kNVon0dQqnxv0UBoh0MgaApeXEALw_wcB; _hjSession_2848248=eyJpZCI6ImUxZWQ0OWFjLTBmNmMtNDIwMi1iZGIzLTJlZTVlZTViZTczOCIsImMiOjE3MDg3MDc3MzkyMDAsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _hjHasCachedUserAttributes=true; _ym_isad=2; _ym_visorc=b; isAnalyticEventsLimit=true; new_language=en; _scid_r=822a2d8f-f0db-4905-a830-d1f2f0de2057; _ga_HY7CCPCD7H=GS1.1.1708707739.2.1.1708707791.8.0.0; _ga_CFRN8YJV66=GS1.1.1708707739.2.1.1708707791.0.0.0; _uetsid=4de90a60d26d11eebc8e554ab0604254; _uetvid=9e1a3600d0d911ee9cd2979f53a72729; amplitude_id_c14fa5162b6e034d1c3b12854f3a26f5cs.money=eyJkZXZpY2VJZCI6IjBkZDU2YTE3LTczMmMtNDE1NC05YzRkLWZmNGFmOTU1NTYzMlIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTcwODcwNzczODcwNSwibGFzdEV2ZW50VGltZSI6MTcwODcwNzgwMjUzOCwiZXZlbnRJZCI6MjUsImlkZW50aWZ5SWQiOjIxLCJzZXF1ZW5jZU51bWJlciI6NDZ9',
        'referer': 'https://cs.money/market/buy/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-56e16fe32fb63048cf5a68a520698048-f354c577f0c71e2e-01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'x-client-app': 'web_mobile',
    }
    while True:
        try:
            c = 0
            col_skinov = 0
            params = {
                'limit': '60',
                'maxPrice': '',
                'minPrice': '',
                'order': 'desc',
                'sort': 'discount',
            }
            params['maxPrice'] = max_price
            params['minPrice'] = min_price
            hash = []
            for i in range(0, 5000, 60):
                params['offset'] = i
                headers['user-agent'] = ua.random
                #proxi = next(proxy)
                #proxy_ye = dict(http=f'socks5://{proxi}',
                #               https=f'socks5://{proxi}')
                response = requests.get('https://cs.money/1.0/market/sell-orders', params=params,headers=headers)
                if response.status_code == 200:
                    c += 1
                    logger.info(f'Количество запросов {c}')
                    items = response.json().get('items')
                    for item in items:
                        hash.append((item.get('pricing').get('computed'),
                                     item.get('asset').get("images").get('steam'),
                                     item.get('asset').get('names').get('full')))
                else:
                    logger.warning(f'Статус код {response.status_code}')
                    break

            for item_ in hash:
                price,img,name = item_
                price_json = info.get(name,999_999_999)
                if float(price_json) >= float(price):
                    logger.debug(f'''Нашли скин с низкой ценой! {name}. Market price: {price}, Json price: {price_json}''')
                    col_skinov += 1
                    RebbitMQ.send_message(
                        photo_url=img,
                        name=name,
                        price=price,
                        url=f'https://cs.money/market/buy/?limit=60&search={name}&order=asc&sort=price')
            logger.debug(f'Количество скинов которые отправили {col_skinov}')
        except Exception as ex:
            logger.error(f'Ошибка в парсере {ex} Статус код: {response.status_code}')

if __name__ == '__main__':
    user = Database.get_user_data()
    start(min_price=user.min_price,
          max_price=user.max_price)
