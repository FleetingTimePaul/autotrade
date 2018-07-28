#!/usr/bin/python
# -*- coding: utf-8 -*-
from Util import *


class OKFuture:
    def __init__(self, url, api_key, secret_key):
        self.__url = url
        self.__apikey = api_key
        self.__secretkey = secret_key

    # OKCoin期货行情信息
    def future_ticker(self, symbol, contract_type):
        future_ticker_resource = "/api/v1/future_ticker.do"
        params = ''
        if symbol:
            params += '&symbol=' + symbol if params else 'symbol=' + symbol
        if contract_type:
            params += '&contract_type=' + contract_type if params else 'contract_type=' + symbol
        return http_get_ok_request(self.__url, future_ticker_resource, params)

    # OKCoin期货市场深度信息
    def future_depth(self, symbol, contract_type, size):
        future_depth_resource = "/api/v1/future_depth.do"
        params = ''
        if symbol:
            params += '&symbol=' + symbol if params else 'symbol=' + symbol
        if contract_type:
            params += '&contract_type=' + contract_type if params else 'contract_type=' + symbol
        if size:
            params += '&size=' + size if params else 'size=' + size
        return http_get_ok_request(self.__url, future_depth_resource, params)

    # OKCoin期货交易记录信息
    def future_trades(self, symbol, contract_type):
        future_trades_resource = "/api/v1/future_trades.do"
        params = ''
        if symbol:
            params += '&symbol=' + symbol if params else 'symbol=' + symbol
        if contract_type:
            params += '&contract_type=' + contract_type if params else 'contract_type=' + symbol
        return http_get_ok_request(self.__url, future_trades_resource, params)

    # KCoin期货指数
    def future_index(self, symbol):
        future_index = "/api/v1/future_index.do"
        params = ''
        if symbol:
            params = 'symbol=' + symbol
        return http_get_ok_request(self.__url, future_index, params)

    # 获取美元人民币汇率
    def exchange_rate(self):
        exchage_rate = "/api/v1/exchange_rate.do"
        return http_get_ok_request(self.__url, exchage_rate, '')

    # 获取预估交割价
    def future_estimated_price(self, symbol):
        future_estimated_price = "/api/v1/future_estimated_price.do"
        params = ''
        if symbol:
            params = 'symbol=' + symbol
        return http_get_ok_request(self.__url, future_estimated_price, params)

    # 期货全仓账户信息
    def future_user_info(self):
        future_user_info = "/api/v1/future_userinfo.do?"
        params = {
            'api_key': self.__apikey
        }
        params['sign'] = build_ok_sign(params, self.__secretkey)
        return http_post_ok_request(self.__url, future_user_info, params)

    # 期货全仓持仓信息
    def future_position(self, symbol, contract_type):
        future_position = "/api/v1/future_position.do?"
        params = {
            'api_key': self.__apikey,
            'symbol': symbol,
            'contract_type': contract_type
        }
        params['sign'] = build_ok_sign(params, self.__secretkey)
        return http_post_ok_request(self.__url, future_position, params)

    # 期货下单
    def future_trade(self, symbol, contract_type, price='', amount='', trade_type='', match_price='', lever_rate=''):
        future_trade = "/api/v1/future_trade.do?"
        params = {
            'api_key': self.__apikey,
            'symbol': symbol,
            'contract_type': contract_type,
            'amount': amount,
            'type': trade_type,
            'match_price': match_price,
            'lever_rate': lever_rate
        }
        if price:
            params['price'] = price
        params['sign'] = build_ok_sign(params, self.__secretkey)
        return http_post_ok_request(self.__url, future_trade, params)

    # 期货批量下单
    def future_batch_trade(self, symbol, contract_type, orders_data, lever_rate):
        future_batch_trade = "/api/v1/future_batch_trade.do?"
        params = {
            'api_key': self.__apikey,
            'symbol': symbol,
            'contract_type': contract_type,
            'orders_data': orders_data,
            'lever_rate': lever_rate
        }
        params['sign'] = build_ok_sign(params, self.__secretkey)
        return http_post_ok_request(self.__url, future_batch_trade, params)

    # 期货取消订单
    def future_cancel(self, symbol, contract_type, order_id):
        future_cancel = "/api/v1/future_cancel.do?"
        params = {
            'api_key': self.__apikey,
            'symbol': symbol,
            'contract_type': contract_type,
            'order_id': order_id
        }
        params['sign'] = build_ok_sign(params, self.__secretkey)
        return http_post_ok_request(self.__url, future_cancel, params)

    # 期货获取订单信息
    def future_order_info(self, symbol, contract_type, order_id, status, current_page, page_length):
        future_order_info = "/api/v1/future_order_info.do?"
        params = {
            'api_key': self.__apikey,
            'symbol': symbol,
            'contract_type': contract_type,
            'order_id': order_id,
            'status': status,
            'current_page': current_page,
            'page_length': page_length
        }
        params['sign'] = build_ok_sign(params, self.__secretkey)
        return http_post_ok_request(self.__url, future_order_info, params)

    # 期货逐仓账户信息
    def future_user_info_4fix(self):
        future_info_4_fix = "/api/v1/future_userinfo_4fix.do?"
        params = {'api_key': self.__apikey}
        params['sign'] = build_ok_sign(params, self.__secretkey)
        return http_post_ok_request(self.__url, future_info_4_fix, params)

    # 期货逐仓持仓信息
    def future_position_4fix(self, symbol, contract_type, type1):
        future_position_4_fix = "/api/v1/future_position_4fix.do?"
        params = {
            'api_key': self.__apikey,
            'symbol': symbol,
            'contract_type': contract_type,
            'type': type1
        }
        params['sign'] = build_ok_sign(params, self.__secretkey)
        return http_post_ok_request(self.__url, future_position_4_fix, params)
