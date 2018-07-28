#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-21 13:57:03
# @Author  : Steven
# @QQ      : 83365885

from OkSpotAPI import OKSpot
from HuobiSpotAPI import HuobiSpot


class Kline:
    def __init__(self, exchange=0, amount=0, open=0.0, close=0.0, high=0.0, low=0.0, ts=0):
        self.amount = amount
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.ts = ts
        self.exchange = exchange

    def save_to_db(self):
        return

    def get_from_db(self, ts=0):
        return


class Klines:
    def __init__(self):
        self.ok_klines = []
        self.huobi_klines = []

    def batch_save_to_huobi_db(self):
        return

    def batch_save_to_ok_db(self):
        return

    def fetch_from_exchange(self):
        return
