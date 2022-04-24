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
from tkinter.messagebox import NO
import traceback
import requests

"""
cron: */8 9-20 * * *
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
    print('开始查询首页数据!')
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

def shooping_cart_data():
    url = 'https://maicai.api.ddxq.mobi/order/getMultiReserveTime'
    headers = {
        'Accept-Encoding' : 'gzip, deflate, br',
        'ddmc-city-number' : '0101',
        'nars' : 'hXu0e19b54c60c90beaaf86aed480823aa2623a09128d0dda9ff9dce9dfc0',
        'Host' : 'maicai.api.ddxq.mobi',
        'ddmc-locale-identifier' : 'zh_CN',
        'ddmc-os-version' : '15.4.1',
        'ddmc-api-version' : '9.50.1',
        'Connection' : 'keep-alive',
        'Accept-Language' : 'zh-Hans-CN;q=1, en-CN;q=0.9',
        'ddmc-build-version' : '1229',
        'User-Agent' : 'neighborhood/9.50.1 (iPhone; iOS 15.4.1; Scale/3.00)',
        'ddmc-idfa' : '',
        'ddmc-longitude' : '121.524199',
        'sesi' : '3951606e6cb72228bbefb42f018491136c98acb97cc89CGePL0',
        'ddmc-app-client-id' : '1',
        'ddmc-latitude' : '31.180359',
        'sign' : 'b28407462a3b4fb1327fdc87b552da34',
        'ddmc-uid' : '5bc9a942efe2cd0f41852d49',
        'ddmc-device-name' : 'iPhone 12',
        'Content-Type' : 'application/x-www-form-urlencoded',
        'ddmc-device-model' : 'iPhone13,2',
        'ddmc-channel' : 'App Store',
        'Accept' : '*/*',
        'ddmc-country-code' : 'CN',
        'ddmc-device-id' : '94c36cae133abf394f545f1c71e5936835a59321',
        'Cookie' : 'DDXQSESSID=77811h9g200v548vgdd90y715uhg0u50ystxv469d186v4xr7w544q3tgvihig32',
        'ddmc-ip' : '',
        'ddmc-station-id' : '5bc5a7d4716de1a94f8b6fb6',
        'ddmc-language-code' : 'zh',
        'Time' : '1650800065,e8c816961f55008425056b87242b2ee6'
    }
    data = 'ab_config=%7B%22ETA_time_default_selection%22%3A%22B1.2%22%7D&address_id=5d7b6cadc7316f2ea9299e6a&api_version=9.50.1&app_client_id=1&app_type=&buildVersion=1229&channel=App%20Store&city_number=0101&countryCode=CN&device_id=94c36cae133abf394f545f1c71e5936835a59321&device_model=iPhone13%2C2&device_name=iPhone%2012&idfa=&ip=&languageCode=zh&latitude=31.180359&localeIdentifier=zh_CN&longitude=121.524199&os_version=15.4.1&products=%5B%22%5B%7B%5C%22sale_batches%5C%22%3A%7B%5C%22batch_type%5C%22%3A-1%7D%2C%5C%22is_coupon_gift%5C%22%3A0%2C%5C%22id%5C%22%3A%5C%225f55fd49f06606002c49a513%5C%22%2C%5C%22price%5C%22%3A%5C%22468.00%5C%22%2C%5C%22is_booking%5C%22%3A0%2C%5C%22count%5C%22%3A1%2C%5C%22small_image%5C%22%3A%5C%22https%3A%5C%5C%5C/%5C%5C%5C/img.ddimg.mobi%5C%5C%5C/product%5C%5C%5C/98e1b4b5c95561599811743193.jpg%21deliver.product.list%5C%22%2C%5C%22type%5C%22%3A1%2C%5C%22origin_price%5C%22%3A%5C%22468.00%5C%22%2C%5C%22product_type%5C%22%3A0%2C%5C%22product_name%5C%22%3A%5C%22%E5%89%91%E5%8D%97%E6%98%A552%E5%BA%A6%E7%99%BD%E9%85%92%20500ml%5C%5C%5C/%E7%93%B6%5C%22%7D%5D%22%5D&seqid=2123790951&sign=b28407462a3b4fb1327fdc87b552da34&station_id=5bc5a7d4716de1a94f8b6fb6&time=1650800065&uid=5bc9a942efe2cd0f41852d49'
    print('开始确认 订单 可提交时间!')
    response = requests.post(url=url, headers=headers, data=data)
    resp_str = response.content.decode("utf-8")
    datas = json.loads(resp_str)
    try:
        for item in datas['data']:
            for time in item['time']:
                for t in time['times']:
                    if t['disableMsg'].find('已约满') != -1:
                        continue
                    print(f'time_info = {t}]\n')
                    return t['textMsg']
        print(f'未找到合适配送时间!\n reps = {datas}')
        return None
    except Exception as e:
        print(f'Error: {e}, data = {datas}')
        return -1

def check_home_data():
    data = home_data()
    if data:
        if data.find('本站当前可预约') != -1:
            load_send()
            send("叮咚买菜运力监控", f'赶快去看看 叮咚买菜 吧,现在已经有运力!\n {data}')
            print(data)
        else:
            print(f'当前无法下单: {data}')

def check_shopping_cart():
    data = shooping_cart_data()
    if data:
        if data == -1:
            print('订单确认失败,继续查询首页信息!')
            check_home_data()
            return None
        load_send()
        send("叮咚买菜运力监控", f'赶快去看看 叮咚买菜 吧,现在已经有运力!\n {data}')
        print(data)

if __name__ == '__main__':
    check_shopping_cart()
    # check_home_data()

    