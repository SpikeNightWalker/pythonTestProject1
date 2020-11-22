import json

import requests

from common.LoggerUtil import MyLog

log = MyLog.get_log()

class HttpProcesser:

    def request(self, method, url, headers, data, token=None):
        '''
        发送请求
        :param method:
        :param url:
        :param headers:
        :param data:
        :param token:
        :return:
        '''
        headers = self._switch_dict_from_str(headers)
        data = self._switch_dict_from_str(data)
        headers = self._add_token(headers, token)
        log.info("开始发送请求，method:%s，url:%s，headers:%s，data:%s", method, url, headers, data)
        if "GET" == method.upper():
            resp = requests.get(url, headers=headers, json=json.loads(data))
        else:
            resp = requests.post(url, headers=headers, json=data)
        resp_json = resp.json()
        log.info("收到响应:%s", resp_json)
        return resp_json

    def _switch_dict_from_str(self, data):
        '''
        json字符串转dict
        :param data:
        :return:
        '''
        return json.loads(data) if isinstance(data, str) else data

    def _add_token(self, headers, token):
        '''
        如果token存在，则添加token
        :param headers:
        :param token:
        :return:
        '''
        if token:
            headers.update({"Authorization":"Bearer {}".format(token)})
        return headers
