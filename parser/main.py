import requests
import json
from anti_useragent import UserAgent
import time




def start():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:122.0) Gecko/20100101 Firefox/122.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'X-Client-App': 'web',
        'traceparent': '00-2ae53341d261d7c20af6f5f8bb4ea3db-f6bb9dfa64254cf6-01',
        'Alt-Used': 'cs.money',
        'Connection': 'keep-alive',
        'Referer': 'https://cs.money/market/buy/',
        # 'Cookie': 'region=Grodnenskaya; cc_service2={%22services%22:[%22necessary%22%2C%22gtm%22%2C%22ym%22%2C%22amplitude%22%2C%22gleam%22%2C%22esputnik%22%2C%22hotjar%22%2C%22userSesDatToAnalytic%22%2C%22userSesDatToMarketing%22%2C%22cardVisualSize%22]%2C%22acceptanceDate%22:1708281882726%2C%22revision%22:0}; group_id=97bc3555-3efe-4876-91f9-2018937763a6; sc=5130948A-2EFB-54FC-AF9F-339C47DB13B2; _gcl_au=1.1.42814056.1708281883; _ga_HY7CCPCD7H=GS1.1.1708365886.2.1.1708365918.28.0.0; _ga=GA1.1.894398092.1708281884; cf_clearance=.w_Dxq1JPih7h9ch1Uvmg9ljHlssx9UwpQ6coDScLKo-1708365886-1.0-Af1oq5AREHT5vpNlMF9EZ+FJVLwLbIEugDZO/lwanG17Geinzsi37I+m8bPxryyerlYxQC9AoYL8Harz0o5/wng=; _ga_CFRN8YJV66=GS1.1.1708365886.2.1.1708365896.0.0.0; ouid=60299031_1734003192; _ym_uid=1708281886412497733; _ym_d=1708281886; _scid=eafb7b8f-21ae-4a77-99ec-d91424da7f0a; amplitude_id_c14fa5162b6e034d1c3b12854f3a26f5cs.money=eyJkZXZpY2VJZCI6IjMwYzc3N2U0LTBmZGMtNDVhMi1hYzM5LTQ1ZDhjOTc3MWU5MVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTcwODM2NTg4Njg5MSwibGFzdEV2ZW50VGltZSI6MTcwODM2NTkwNTA4NSwiZXZlbnRJZCI6MTEsImlkZW50aWZ5SWQiOjIwLCJzZXF1ZW5jZU51bWJlciI6MzF9; _hjSessionUser_2848248=eyJpZCI6IjU1N2EwYmJhLTAzYWItNWJlMy1hNTg2LTNhMTY4NjhiOWZhNyIsImNyZWF0ZWQiOjE3MDgyODE4ODY0ODAsImV4aXN0aW5nIjp0cnVlfQ==; _sctr=1%7C1708203600000; isAnalyticEventsLimit=true; new_language=en; _hjSession_2848248=eyJpZCI6ImU0NDFiMTYyLTBkOTMtNGY1NC1hN2IzLTBkZjE3MzdkMmQ1ZCIsImMiOjE3MDgzNjU4ODcxODcsInMiOjEsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _hjHasCachedUserAttributes=true; _ym_isad=1; _ym_visorc=b; _scid_r=eafb7b8f-21ae-4a77-99ec-d91424da7f0a; _uetsid=c962ac70ce8d11eeb5d901acd8280a1f; _uetvid=ae42a8205d4f11ee829917d87d31b452',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }
    offset = 0
    batch_size = 60
    while True:
        params = {
            'limit': '60',
            'offset': '0',
            'order': 'desc',
            'sort': 'discount',
        }
        hash = []

        for off in range(offset,offset+batch_size,60):
            offset += batch_size
            params['offset'] = off
            print(off)
            response = requests.get('https://cs.money/1.0/market/sell-orders', params=params,headers=headers)
            items = response.json().get('items')

            for item in items:
                print(item.get('pricing').get('discount'))
            time.sleep(1)












if __name__ == '__main__':
    start()
