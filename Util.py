#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-21 13:57:03
# @Author  : Steven
# @QQ      : 83365885

import json
import urllib
import urllib.parse
import urllib.request
import http.client
import hmac
import base64
import hashlib


def build_huobi_sign(params, method, host_url, request_path, secret_key):
    sorted_params = sorted(params.items(), key=lambda d: d[0], reverse=False)
    encode_params = urllib.parse.urlencode(sorted_params)
    payload = [method, host_url, request_path, encode_params]
    payload = '\n'.join(payload)
    payload = payload.encode(encoding='UTF8')
    secret_key = secret_key.encode(encoding='UTF8')
    digest = hmac.new(secret_key, payload, digestmod=hashlib.sha256).digest()
    signature = base64.b64encode(digest)
    signature = signature.decode()
    return signature


def http_get_huobi_request(url, resource, params):
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    }
    get_data = urllib.parse.urlencode(params)
    conn = http.client.HTTPSConnection(url, timeout=150)
    conn.request("GET", resource + '?' + get_data, headers=headers)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    return json.loads(data)


def http_post_huobi_request(url, resource, params):
    headers = {
        "Accept": "application/json",
        'Content-Type': 'application/json'
    }
    conn = http.client.HTTPSConnection(url, timeout=150)
    temp_params = urllib.parse.urlencode(params)
    conn.request("POST", resource, temp_params, headers)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    params.clear()
    conn.close()
    return data


def build_ok_sign(params, secret_key):
    sign = ''
    for key in sorted(params.keys()):
        sign += key + '=' + str(params[key]) + '&'
    data = sign + 'secret_key=' + secret_key
    return hashlib.md5(data.encode("utf8")).hexdigest().upper()


def http_get_ok_request(url, resource, params=''):
    conn = http.client.HTTPSConnection(url, timeout=10)
    conn.request("GET", resource + '?' + params)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    return json.loads(data)


def http_post_ok_request(url, resource, params):
    headers = {
            "Content-type": "application/x-www-form-urlencoded",
    }
    conn = http.client.HTTPSConnection(url, timeout=10)
    temp_params = urllib.parse.urlencode(params)
    conn.request("POST", resource, temp_params, headers)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    params.clear()
    conn.close()
    return data


def http_get(url, params, add_to_headers=None):
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    }
    if add_to_headers:
        headers.update(add_to_headers)
    post_data = urllib.parse.urlencode(params)
    response = requests.get(url, post_data, headers=headers, timeout=150)
    try:
        if response.status_code == 200:
            return response.json()
        else:
            return
    except BaseException as e:
        print("http_get failed, detail is:%s,%s" % (response.text, e))
        return


def http_post(url, params, add_to_headers=None):
    headers = {
        "Accept": "application/json",
        'Content-Type': 'application/json'
    }
    if add_to_headers:
        headers.update(add_to_headers)
    post_data = json.dumps(params)
    s = requests.session()
    s.keep_alive = False
    response = requests.post(url, post_data, headers=headers, timeout=150)
    try:

        if response.status_code == 200:
            return response.json()
        else:
            return
    except BaseException as e:
        print("httpPost failed, detail is:%s,%s" % (response.text, e))
        return
