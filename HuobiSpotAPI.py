#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-21 13:57:03
# @Author  : Steven
# @QQ      : 83365885

from Util import *
import datetime


class HuobiSpot:
    def __init__(self, trade_base_url, market_base_url, api_key, secret_key):
        self.trade_base_url = trade_base_url
        self.market_base_url = market_base_url
        self.api_key = api_key
        self.secret_key = secret_key
        try:
            accounts = self.get_accounts()
            self.account_id = accounts['data'][0]['id']
            print(self.account_id)
        except BaseException as e:
            print('get account_id error.%s' % e)
            self.account_id = None

    # 获取KLine
    def get_kline(self, symbol, period, size=150):
        params = {'symbol': symbol,
                  'period': period,
                  'size': size}
        url = self.market_base_url + '/market/history/kline'
        return http_get_huobi_request(url, params)

    # 获取market_depth
    def get_depth(self, symbol, _type):
        params = {'symbol': symbol,
                  'type': _type}
        url = self.market_base_url + '/market/depth'
        return http_get_huobi_request(url, params)

    # 获取trade_detail
    def get_trade(self, symbol):
        params = {'symbol': symbol}
        url = self.market_base_url + '/market/trade'
        return http_get_huobi_request(url, params)

    # 获取merge ticker
    def get_ticker(self, symbol):
        params = {'symbol': symbol}
        url = self.market_base_url + '/market/detail/merged'
        return http_get_huobi_request(url, params)

    # 获取 Market Detail 24小时成交量数据
    def get_detail(self, symbol):
        params = {'symbol': symbol}
        url = self.market_base_url + '/market/detail'
        return http_get_huobi_request(url, params)

    # 获取支持的交易对
    def get_symbols(self, long_polling=None):
        params = {}
        if long_polling:
            params['long-polling'] = long_polling
        path = '/v1/common/symbols'
        return self.api_key_get(params, path)

    def get_accounts(self):
        path = "/v1/account/accounts"
        params = {}
        return self.api_key_get(params, path)

    # 获取当前账户资产
    def get_balance(self):
        if not self.account_id:
            accounts = self.get_accounts()
            self.account_id = accounts['data'][0]['id']
        url = "/v1/account/accounts/{0}/balance".format(self.account_id)
        params = {"account-id": self.account_id}
        return self.api_key_get(params, url)

    # 创建并执行订单
    def send_order(self, amount, source, symbol, _type, price=0):
        if not self.account_id:
            try:
                accounts = self.get_accounts()
                self.account_id = accounts['data'][0]['id']
            except BaseException as e:
                print('get acct_id error.%s' % e)
                self.account_id = None
        params = {"account-id": self.account_id,
                  "amount": amount,
                  "symbol": symbol,
                  "type": _type,
                  "source": source}
        if price:
            params["price"] = price
        url = '/v1/order/orders/place'
        return self.api_key_post(params, url)

    # 撤销订单
    def cancel_order(self, order_id):
        params = {}
        url = "/v1/order/orders/{0}/submitcancel".format(order_id)
        return self.api_key_post(params, url)

    # 查询某个订单
    def order_info(self, order_id):
        params = {}
        url = "/v1/order/orders/{0}".format(order_id)
        return self.api_key_get(params, url)

    # 查询某个订单的成交明细
    def order_match_results(self, order_id):
        params = {}
        url = "/v1/order/orders/{0}/matchresults".format(order_id)
        return self.api_key_get(params, url)

    # 查询当前委托、历史委托
    def orders_list(self, symbol, states, types=None, start_date=None, end_date=None, _from=None, direct=None, size=None):
        params = {'symbol': symbol,
                  'states': states}
        if types:
            params['types'] = types
        if start_date:
            params['start-date'] = start_date
        if end_date:
            params['end-date'] = end_date
        if _from:
            params['from'] = _from
        if direct:
            params['direct'] = direct
        if size:
            params['size'] = size
        url = '/v1/order/orders'
        return self.api_key_get(params, url)

    # 查询当前成交、历史成交
    def orders_match_results(self, symbol, types=None, start_date=None, end_date=None, _from=None, direct=None, size=None):
        params = {'symbol': symbol}
        if types:
            params[types] = types
        if start_date:
            params['start-date'] = start_date
        if end_date:
            params['end-date'] = end_date
        if _from:
            params['from'] = _from
        if direct:
            params['direct'] = direct
        if size:
            params['size'] = size
        url = '/v1/order/matchresults'
        return self.api_key_get(params, url)

    # 申请提现虚拟币
    def withdraw(self, address, amount, currency, fee=0, addr_tag=""):
        params = {'address': address,
                  'amount': amount,
                  "currency": currency,
                  "fee": fee,
                  "addr-tag": addr_tag}
        url = '/v1/dw/withdraw/api/create'
        return self.api_key_post(params, url)

    # 申请取消提现虚拟币
    def cancel_withdraw(self, address_id):
        params = {}
        url = '/v1/dw/withdraw-virtual/{0}/cancel'.format(address_id)
        return self.api_key_post(params, url)

    # 创建并执行借贷订单
    def send_margin_order(self, amount, symbol, _type, price=0):
        try:
            accounts = self.get_accounts()
            self.account_id = accounts['data'][0]['id']
        except BaseException as e:
            print('get acct_id error.%s' % e)
            self.account_id = None
        params = {"account-id": self.account_id,
                  "amount": amount,
                  "symbol": symbol,
                  "type": _type,
                  "source": 'margin-api'}
        if price:
            params["price"] = price
        url = '/v1/order/orders/place'
        return self.api_key_post(params, url)

    # 现货账户划入至借贷账户
    def exchange_to_margin(self, symbol, currency, amount):
        params = {"symbol": symbol,
                  "currency": currency,
                  "amount": amount}
        url = "/v1/dw/transfer-in/margin"
        return self.api_key_post(params, url)

    # 借贷账户划出至现货账户
    def margin_to_exchange(self, symbol, currency, amount):
        params = {"symbol": symbol,
                  "currency": currency,
                  "amount": amount}
        url = "/v1/dw/transfer-out/margin"
        return self.api_key_post(params, url)

    # 申请借贷
    def get_margin(self, symbol, currency, amount):
        params = {"symbol": symbol,
                  "currency": currency,
                  "amount": amount}
        url = "/v1/margin/orders"
        return self.api_key_post(params, url)

    # 归还借贷
    def repay_margin(self, order_id, amount):
        params = {"order-id": order_id,
                  "amount": amount}
        url = "/v1/margin/orders/{0}/repay".format(order_id)
        return self.api_key_post(params, url)

    # 借贷订单
    def loan_orders(self, symbol, currency, start_date="", end_date="", start="", direct="", size=""):
        params = {"symbol": symbol,
                  "currency": currency}
        if start_date:
            params["start-date"] = start_date
        if end_date:
            params["end-date"] = end_date
        if start:
            params["from"] = start
        if direct and direct in ["prev", "next"]:
            params["direct"] = direct
        if size:
            params["size"] = size
        url = "/v1/margin/loan-orders"
        return self.api_key_get(params, url)

    # 借贷账户详情,支持查询单个币种
    def margin_balance(self, symbol):
        params = {}
        url = "/v1/margin/accounts/balance"
        if symbol:
            params['symbol'] = symbol
        return self.api_key_get(params, url)

    def api_key_get(self, params, request_path):
        method = 'GET'
        timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
        params.update({'AccessKeyId': self.api_key,
                       'SignatureMethod': 'HmacSHA256',
                       'SignatureVersion': '2',
                       'Timestamp': timestamp})
        host_url = self.trade_base_url
        host_name = urllib.parse.urlparse(host_url).hostname
        host_name = host_name.lower()
        params['Signature'] = build_huobi_sign(params, method, host_name, request_path, self.secret_key)
        return http_get_huobi_request(host_name, request_path, params)

    def api_key_post(self, params, request_path):
        method = 'POST'
        timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S')
        params_to_sign = {'AccessKeyId': self.api_key,
                          'SignatureMethod': 'HmacSHA256',
                          'SignatureVersion': '2',
                          'Timestamp': timestamp}
        host_url = self.trade_base_url
        host_name = urllib.parse.urlparse(host_url).hostname
        host_name = host_name.lower()
        params_to_sign['Signature'] = build_huobi_sign(params_to_sign, method, host_name, request_path, self.secret_key)
        return http_post_huobi_request(host_name, request_path + '?' + urllib.parse.urlencode(params_to_sign), params)
