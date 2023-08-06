#!/usr/bin/env python3
# coding = utf8
"""
@ Author : ZeroSeeker
@ e-mail : zeroseeker@foxmail.com
@ GitHub : https://github.com/ZeroSeeker
@ Gitee : https://gitee.com/ZeroSeeker
"""
from lazysdk import lazyrequests


def create_customer_service_message(
        cookie: str,
        app_id,
        app_type,
        distributor_id,
        msg_name: str,
        msg_type: int,
        content: str,
        send_time: str,
        send_target: int
):
    """
    运营配置-客服消息-新建消息
    目前仅支持文字消息
    :param cookie: cookie
    :param app_id: 应用id
    :param app_type: 应用类型：3-公众号
    :param distributor_id:
    :param msg_name: 消息名称
    :param msg_type: 消息类型：1-文字消息,2-图文消息
    :param content: 消息内容
    :param send_time: 发送时间，例如：2022-12-31 17:27:33
    :param send_target: 发送用户，1-全部用户
    """
    url = 'https://www.changdunovel.com/novelsale/distributor/customer_service_message/create/v1/'
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Cookie": cookie,
        "Host": "www.changdunovel.com",
        "Origin": "https://www.changdunovel.com",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:108.0) Gecko/20100101 Firefox/108.0",
        "agw-js-conv": "str",
        "appid": str(app_id),
        "apptype": str(app_type),
        "content-type": "application/json",
        "distributorid": str(distributor_id)
    }
    data = {
        "msg_name": msg_name,
        "msg_type": msg_type,
        "msg_detail": {
            "content": f"<p>{content}</p>"  # 文字消息
        },
        "send_time": send_time,
        "send_target": send_target
    }
    return lazyrequests.lazy_requests(
        method='POST',
        url=url,
        json=data,
        headers=headers,
        return_json=True
    )
