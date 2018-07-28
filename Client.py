#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8

from OkSpotAPI import OKSpot
from HuobiSpotAPI import HuobiSpot

ok_coin_api_key = ''
ok_coin_secret_key = ''
ok_coin_url_cn = 'www.okcoin.cn'
ok_coin_url_en = 'www.okcoin.com'

huobi_api_key = ''
huobi_secret_key = ''
huobi_market_url = 'https://api.huobi.pro'
huobi_trade_url = 'https://api.huobi.pro'


# run robot with some model
def robot_run():
    ok_spot = OKSpot(ok_coin_url_cn, ok_coin_api_key, ok_coin_secret_key)
    huobi_spot = HuobiSpot(huobi_trade_url, huobi_market_url, huobi_api_key, huobi_secret_key)

    return


if __name__ == '__main__':
    robot_run()

# print(u' 现货行情 ')
# print(ok_spot.ticker('btc_usd'))

# print(u' 现货深度 ')
# print(ok_spot.depth('btc_usd'))

# print(u' 现货历史交易信息 ')
# print(ok_spot.trades())

# print(u' 用户现货账户信息 ')
# print(ok_spot.user_info())

# print(u' 现货下单 ')
# print(ok_spot.trade('ltc_usd','buy','0.1','0.2'))

# print(u' 现货批量下单 ')
# print(ok_spot.batch_trade('ltc_usd','buy','[{price:0.1,amount:0.2},{price:0.1,amount:0.2}]'))

# print(u' 现货取消订单 ')
# print(ok_spot.cancel_order('ltc_usd','18243073'))

# print(u' 现货订单信息查询 ')
# print(ok_spot.order_info('ltc_usd','18243644'))

# print(u' 现货批量订单信息查询 ')
# print(ok_spot.orders_info('ltc_usd','18243800,18243801,18243644','0'))

# print(u' 现货历史订单信息查询 ')
# print(ok_spot.orderHistory('ltc_usd','0','1','2'))

# print(u' 期货行情信息')
# print(ok_future.future_ticker('ltc_usd','this_week'))

# print(u' 期货市场深度信息')
# print(ok_future.future_depth('btc_usd','this_week','6'))

# print(u'期货交易记录信息')
# print(ok_future.future_trades('ltc_usd','this_week'))

# print(u'期货指数信息')
# print(ok_future.future_index('ltc_usd'))

# print(u'美元人民币汇率')
# print(ok_future.exchange_rate())

# print(u'获取预估交割价')
# print(ok_future.future_estimated_price('ltc_usd'))

# print(u'获取全仓账户信息')
# print(ok_future.future_user_info())

# print(u'获取全仓持仓信息')
# print(ok_future.future_position('ltc_usd','this_week'))

# print(u'期货下单')
# print(ok_future.future_trade('ltc_usd','this_week','0.1','1','1','0','20'))

# print(u'期货批量下单')
# print(ok_future.future_batch_trade('ltc_usd','this_week','[{price:0.1,amount:1,type:1,match_price:0},{price:0.1,amount:3,type:1,match_price:0}]','20'))

# print(u'期货取消订单')
# print(ok_future.future_cancel('ltc_usd','this_week','47231499'))

# print(u'期货获取订单信息')
# print(ok_future.future_order_info('ltc_usd','this_week','47231812','0','1','2'))

# print(u'期货逐仓账户信息')
# print(ok_future.future_user_info_4fix())

# print(u'期货逐仓持仓信息')
# print(ok_future.future_position_4fix('ltc_usd','this_week',1))
