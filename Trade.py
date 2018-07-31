#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-21 13:57:03
# @Author  : Steven
# @QQ      : 83365885

from OkSpotAPI import OKSpot
from HuobiSpotAPI import HuobiSpot
import Util


class TradeHistory:
    def __init__(self, amount, create_at, canceled_at, order_id, place_price, field_amount, symbol, state, trade_type,
                 field_cash_amount, finished_at, exchange):
        self.id = -1
        self.amount = amount
        self.create_at = create_at
        self.canceled_at = canceled_at
        self.finished_at = finished_at
        self.place_price = place_price
        self.field_amount = field_amount
        self.order_id = order_id
        self.symbol = symbol
        self.state = state
        self.trade_type = trade_type
        self.field_cash_amount = field_cash_amount
        self.exchange = exchange

    def save_to_db(self):
        return

    def get_from_db(self):
        return

    def update_to_db(self):
        return


class Trade:
    def __init__(self):
        self.trade_history = []
        self.trade_unfinished = []

    def place_order(self):
        return

    def cancel_order(self, order_id):
        return

    def filled_order(self, order_id):
        return
