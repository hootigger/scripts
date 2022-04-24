#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File         : dd_monitor.py
# @Project      : scripts
# @Created Date : 2022-04-24 11:57:05
# @Last Modified: 2022-04-24 11:57:05
# @Author       : Hootigger
# @Cron         : 
# @Desc         : 
# @Copyright (c) 2022 Hootigger

import json
import os
import sys
import traceback
import requests

"""
cron: */10 9-20 * * *
new Env('叮咚买菜运力监控');
"""

def load_send() -> None:
    print("加载推送功能中...")
    global send
    send = None
    cur_path = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(cur_path)
    if os.path.exists(cur_path + "/notify.py"):
        try:
            from notify import send
        except Exception:
            send = None
            print(f"❌加载通知服务失败!!!\n{traceback.format_exc()}")

def home_data():
    url = 'https://maicai.api.ddxq.mobi/homeApi/newDetails?api_version=9.50.1&app_client_id=1&app_type=&buildVersion=1229&channel=App%20Store&city_number=0101&countryCode=CN&device_id=94c36cae133abf394f545f1c71e5936835a59321&device_model=iPhone13%2C2&device_name=iPhone%2012&idfa=&ip=&languageCode=zh&latitude=31.180359&localeIdentifier=zh_CN&longitude=121.524199&os_version=15.4.1&pageId=homePage&seqid=2123790948&sign=ae95ba7f038f1753b8f563e46ee5e92a&station_id=5bc5a7d4716de1a94f8b6fb6&time=1650770528&uid=5bc9a942efe2cd0f41852d49'
    headers = {
        'Host': 'maicai.api.ddxq.mobi',
        'nars': 'yUN790e3a153f4516bbc3e8ed83ccd122cdd678ded5cdc5fc4adf45bf14e8',
        'Time': '1650770528,50bdd16bc75be29408b2af277ae986fb',
        'ddmc-locale-identifier': 'zh_CN',
        'User-Agent': 'neighborhood/9.50.1 (iPhone; iOS 15.4.1; Scale/3.00)',
        'Cookie': 'DDXQSESSID=77811h9g200v548vgdd90y715uhg0u50ystxv469d186v4xr7w544q3tgvihig32',
        'ddmc-city-number': '0101',
        'ddmc-api-version': '9.50.1',
        'ddmc-build-version': '1229',
        'ddmc-idfa': '',
        'ddmc-longitude': '121.524199',
        'ddmc-latitude': '31.180359',
        'sesi': 'd84c`ab62d8e629c10d9c6471c33c0e3ed7b9e2d9daa8oQmVi4',
        'ddmc-app-client-id': '1',
        'sign': 'ae95ba7f038f1753b8f563e46ee5e92a',
        'Connection': 'keep-alive',
        'ddmc-device-name': 'iPhone 12',
        'ddmc-uid': '5bc9a942efe2cd0f41852d49',
        'Accept-Language': 'zh-Hans-CN;q=1, en-CN;q=0.9',
        'ddmc-device-model': 'iPhone13,2',
        'ddmc-channel': 'App Store',
        'ddmc-country-code': 'CN',
        'ddmc-device-id': '94c36cae133abf394f545f1c71e5936835a59321',
        'ddmc-ip': '',
        'ddmc-station-id': '5bc5a7d4716de1a94f8b6fb6',
        'ddmc-language-code': 'zh',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'ddmc-os-version': '15.4.1'
    }
    response = requests.get(url=url, headers=headers)
    resp_str = response.content.decode("utf-8")
    datas = json.loads(resp_str)
    try:
        for item in datas['data']['list']:
            if (item['type'] == 5):
                print(f'bill_info = {item}]\n')
                return item['new_bill_board']['materials'][0]['content']
        print('首页数据未包含运力信息!')
        return None
    except Exception as e:
        print(f'Error: {e}, data = {datas}')
        return None


if __name__ == '__main__':
    data = home_data()
    if data:
        if data.find('本站当前可预约') != -1:
            load_send()
            send("叮咚买菜运力监控", f'赶快去看看 叮咚买菜 吧,现在已经有运力!\n {data}')
            print(data)
        else:
            print(f'当前无法下单: {data}')

    