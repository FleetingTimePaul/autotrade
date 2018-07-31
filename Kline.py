#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-21 13:57:03
# @Author  : Steven
# @QQ      : 83365885

from OkSpotAPI import OKSpot
from HuobiSpotAPI import HuobiSpot
import Util


class Kline:
    def __init__(self, exchange=0, amount=0, open=0.0, close=0.0, high=0.0, low=0.0, ts=0):
        self.id = -1
        self.amount = amount
        self.open = open
        self.close = close
        self.high = high
        self.low = low
        self.ts = ts
        self.exchange = exchange

    def insert_to_db(self):
        return

    def select_from_db(self, ts=0):
        return

    def update_to_db(self):
        return


class Klines:
    def __init__(self):
        self.ok_klines = []
        self.huobi_klines = []

    def batch_insert_to_huobi_db(self):
        return

    def batch_insert_to_ok_db(self):
        return

    def fetch_from_exchange(self):
        return
