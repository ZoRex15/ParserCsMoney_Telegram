import requests
import json
from anti_useragent import UserAgent


def start():

    headers = {
        'authority': 'cs.money',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        # 'cookie': 'group_id=f9e995ac-0f31-44ea-a241-c80fecd5adcb; region=Grodnenskaya; cc_service2={%22services%22:[%22necessary%22%2C%22gtm%22%2C%22ym%22%2C%22amplitude%22%2C%22gleam%22%2C%22esputnik%22%2C%22hotjar%22%2C%22userSesDatToAnalytic%22%2C%22userSesDatToMarketing%22%2C%22cardVisualSize%22]%2C%22acceptanceDate%22:1708344776018%2C%22revision%22:0}; _hjSessionUser_2848248=eyJpZCI6IjhlNDBjY2NhLWNmNTgtNTgwMC1iYzg2LTNlYjI0ZDIyOGFmZCIsImNyZWF0ZWQiOjE3MDgzNDQ3NzYzNTksImV4aXN0aW5nIjp0cnVlfQ==; _hjHasCachedUserAttributes=true; _gcl_au=1.1.955044900.1708344776; sc=7BF80433-7EEB-1D61-7E01-1FFD451C2518; _ga=GA1.1.869995080.1708344777; _scid=5c90199b-2bef-4526-b315-08e241307c22; _ym_uid=1708344777789041453; _ym_d=1708344777; _fbp=fb.1.1708344777162.2080337635; _ym_isad=2; ouid=2254924839_1734003192; _sctr=1%7C1708290000000; isAnalyticEventsLimit=true; cf_clearance=eV6ailSGljaK.v9OmdbDJBl208R2Q2W9RAudfvqDqjg-1708347887-1.0-Ac4j2Qto4xGJSJuJKekPOcT+S+2GJQffRx2A5iDGXT8q1S8xQqhATkfW59BnveXbCScHNwhXXEVOLgLD8HRAxIU=; new_language=en; _scid_r=5c90199b-2bef-4526-b315-08e241307c22; _ga_CFRN8YJV66=GS1.1.1708344776.1.1.1708348794.0.0.0; _uetsid=37761750cf2011eebf91d5c28222e44e; _uetvid=37765ae0cf2011eeaa4163b82a292c36; amplitude_id_c14fa5162b6e034d1c3b12854f3a26f5cs.money=eyJkZXZpY2VJZCI6ImFmNDcyMDJkLTBjYmYtNDkzMi04NDRiLWVhNjM2ZjI4M2Y3M1IiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTcwODM0Nzg4NzczOCwibGFzdEV2ZW50VGltZSI6MTcwODM0ODgyMzg5MSwiZXZlbnRJZCI6MTUsImlkZW50aWZ5SWQiOjEyLCJzZXF1ZW5jZU51bWJlciI6Mjd9; _ga_HY7CCPCD7H=GS1.1.1708344776.1.1.1708363385.59.0.0',
        'referer': 'https://cs.money/market/buy/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'traceparent': '00-defb64f2f2668451890e84ce2dbdb249-1ef171e13c3556f6-01',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'x-client-app': 'web_mobile',
    }

    params = {
        'limit': '60',
        'name': 'mac-10',
        'order': 'desc',
        'sort': 'discount',
    }

    response = requests.get('https://cs.money/1.0/market/sell-orders', params=params,headers=headers)
    print(response,response.json())










if __name__ == '__main__':
    start()
