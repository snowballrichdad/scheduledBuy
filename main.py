import time
from datetime import datetime as dt

import Board
import SendOrderEntry
import OrderInfo
import SendOrderExit
import CanselOrder
import SendOrderExitMarket
import settings
import variables

while True:
    now_time = dt.now()
    if now_time > settings.entry_time:
        break
    time.sleep(10)

# 価格情報取得
Board.board()

# 最高値が前日終値を300円以上上回っているか
if variables.highPrice - variables.preClose < 300:
    # 上回っていなければ買いエントリ

    # 最安値が前日終値を300円以上下回っているか
    if variables.preClose - variables.lowPrice > 300:
        # 現在地が前日終値を200円以上下回っているか
        if variables.preClose - variables.curPrice > 200:
            # 建玉を増やす
            settings.qty = 10

    variables.side = 2
    variables.exitSide = 1
    # 指値で必ず約定できるようにエントリ価格を現在値 + 1000円に
    variables.entryPrice = variables.curPrice + 1000
else:
    # 上回っていれば売りエントリ

    # 現在地が前日終値を200円以上上回っているか
    if variables.curPrice - variables.preClose > 200:
        # 建玉を増やす
        settings.qty = 1

    variables.side = 1
    variables.exitSide = 2
    # 指値で必ず約定できるようにエントリ価格を現在値 - 1000円に
    variables.entryPrice = variables.curPrice - 1000

# エントリ
SendOrderEntry.send_order_entry()

while True:
    # 全約定するまで待つ
    if OrderInfo.orders_info(variables.entryOrderID):
        break
    time.sleep(1)

# 逆指値算出
if variables.side == 2:
    variables.triggerPrice = variables.orderPrice - 300
    variables.underOver = 1
else:
    variables.triggerPrice = variables.orderPrice + 300
    variables.underOver = 2

# 逆指値売り注文
SendOrderExit.send_order_exit()

while True:
    now_time = dt.now()
    if now_time > settings.exit_time:
        break
    time.sleep(10)

# 逆指値売り注文キャンセル
CanselOrder.cancel_order()

while True:
    # 全約定するまで待つ
    if OrderInfo.orders_info(variables.cancelOrderID):
        break
    time.sleep(1)

# 成行売り注文
SendOrderExitMarket.send_order_exit_market()
