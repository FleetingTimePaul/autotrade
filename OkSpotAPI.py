#!/usr/bin/python
# -*- coding: utf-8 -*-
from Util import *


class OKSpot:
    def __init__(self, url, api_key, secret_key):
        self.__url = url
        self.__apikey = api_key
        self.__secretkey = secret_key

    # 获取OKCoin现货行情信息
    def ticker(self, symbol=''):
        ticker_resource = "/api/v1/ticker.do"
        params = ''
        if symbol:
            params = 'symbol=%(symbol)s' % {'symbol': symbol}
        return http_get(self.__url, ticker_resource, params)

    # 获取OKCoin现货市场深度信息
    def depth(self, symbol=''):
        depth_resource = "/api/v1/depth.do"
        params = ''
        if symbol:
            params = 'symbol=%(symbol)s' % {'symbol': symbol}
        return http_get(self.__url, depth_resource, params)

    # 获取OKCoin现货历史交易信息
    def trades(self, symbol=''):
        trades_resource = "/api/v1/trades.do"
        params = ''
        if symbol:
            params = 'symbol=%(symbol)s' % {'symbol': symbol}
        return http_get(self.__url, trades_resource, params)

    # 获取用户现货账户信息
    def user_info(self):
        user_info_resource = "/api/v1/userinfo.do"
        params = {
            'api_key': self.__apikey
        }
        params['sign'] = build_ok_sign(params, self.__secretkey)
        return http_post(self.__url, user_info_resource, params)

    # 现货交易
    def trade(self, symbol, trade_type, price='', amount=''):
        reade_resource = "/api/v1/trade.do"
        params = {
            'api_key': self.__apikey,
            'symbol': symbol,
            'type': trade_type
        }
        if price:
            params['price'] = price
        if amount:
            params['amount'] = amount
            
        params['sign'] = build_ok_sign(params, self.__secretkey)
        return http_post(self.__url, reade_resource, params)

    # 现货批量下单
    def batch_trade(self, symbol, trade_type, orders_data):
        batch_trade_resource = "/api/v1/batch_trade.do"
        params = {
            'api_key': self.__apikey,
            'symbol': symbol,
            'type': trade_type,
            'orders_data': orders_data
        }
        params['sign'] = build_my_sign(params, self.__secretkey)
        return http_post(self.__url, batch_trade_resource, params)

    # 现货取消订单
    def cancel_order(self, symbol, order_id):
        cancel_order_resource = "/api/v1/cancel_order.do"
        params = {
             'api_key': self.__apikey,
             'symbol': symbol,
             'order_id': order_id
        }
        params['sign'] = build_ok_sign(params, self.__secretkey)
        return http_post(self.__url, cancel_order_resource, params)

    # 现货订单信息查询
    def order_info(self, symbol, order_id):
        order_info_resource = "/api/v1/order_info.do"
        params = {
             'api_key': self.__apikey,
             'symbol': symbol,
             'order_id': order_id
        }
        params['sign'] = build_ok_sign(params, self.__secretkey)
        return http_post(self.__url, order_info_resource, params)

    # 现货批量订单信息查询
    def orders_info(self, symbol, order_id, trade_type):
        orders_info_resource = "/api/v1/orders_info.do"
        params = {
             'api_key': self.__apikey,
             'symbol': symbol,
             'order_id': order_id,
             'type': trade_type
        }
        params['sign'] = build_ok_sign(params, self.__secretkey)
        return http_post(self.__url, orders_info_resource, params)

    # 现货获得历史订单信息
    def order_history(self, symbol, status, current_page, page_length):
        order_history_resource = "/api/v1/order_history.do"
        params = {
              'api_key': self.__apikey,
              'symbol': symbol,
              'status': status,
              'current_page': current_page,
              'page_length': page_length
        }
        params['sign'] = build_ok_sign(params, self.__secretkey)
        return http_post(self.__url, order_history_resource, params)
