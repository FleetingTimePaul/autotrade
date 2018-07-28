#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-21 13:57:03
# @Author  : Steven
# @QQ      : 83365885


class MultiDayLine:
    def __init__(self, five, ten, twenty, sixty, ts, exchange):
        self.five_days_line = five
        self.ten_days_line = ten
        self.twenty_days_line = twenty
        self.sixty_days_line = sixty
        self.time_stamp = ts
        self.exchange = exchange

    def save_to_db(self):
        return

    def get_from_db(self, ts=0):
        return


class MultiDayLines:
    def __init__(self):
        self.ok_multi_days_line = []
        self.huobi_multi_days_line = []

    def batch_save_to_ok_db(self):
        return

    def batch_save_to_huobi_db(self):
        return

    def fetch_from_exchange(self):
        return
