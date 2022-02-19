#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File         : kanxue_sign.py
# @Project      : scripts
# @Created Date : 2022-02-10 10:24:42
# @Last Modified: 2022-02-10 10:24:42
# @Author       : Hootigger
# @Cron         : 
# @Desc         : 
# @Copyright (c) 2022 Hootigger

# -*- coding:utf-8 -*-
"""
cron: 50 7 * * *
new Env('看雪签到');
"""

import json
import logging
import os
import sys
import traceback

import requests

logger = logging.getLogger(name=None)  # 创建一个日志对象
logging.Formatter("%(message)s")  # 日志内容格式化
logger.setLevel(logging.INFO)  # 设置日志等级
logger.addHandler(logging.StreamHandler())  # 添加控制台日志
# logger.addHandler(logging.FileHandler(filename="text.log", mode="w"))  # 添加文件日志


ck = os.getenv("kanxue_cookie")
if not ck:
    logger.info(
        "未找到ck, 请export kanxue_cookie=''"
    )
    exit(-1)

headers = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36",
    "Cookie": ck,
    'Connection': 'keep-alive',
    'Accept': '*/*'
}


def load_send() -> None:
    logger.info("加载推送功能中...")
    global send
    send = None
    cur_path = os.path.abspath(os.path.dirname(__file__))
    sys.path.append(cur_path)
    if os.path.exists(cur_path + "/notify.py"):
        try:
            from notify import send
        except Exception:
            send = None
            logger.info(f"❌加载通知服务失败!!!\n{traceback.format_exc()}")


def signin():
    url = f"https://bbs.pediy.com/user-signin.htm"
    response = requests.post(url=url, headers=headers)
    datas = json.loads(response.content.decode("utf-8"))
    print(datas)
    send("看雪签到", f'获得 {datas.get("message")} 雪币.')


if __name__ == "__main__":
    logger.info("===> 看雪签到开始 <===")
    load_send()
    signin()
    logger.info("===> 看雪签到结束 <===")
