import time
import sys
from datetime import datetime as dt

import Board
import SendOrderEntry
import SendOrderEntryCredit
import OrderInfo
import SendOrderExit
import SendOrderExitCredit
import CanselOrder
import SendOrderExitMarket
import SendOrderExitMarketCredit
import variables


# if variables.highPrice - variables.lowPrice <= 200:
#     SendOrderEntry.send_order_entry()
#
#     while True:
#         # 全約定するまで待つ
#         if OrderInfo.orders_info(variables.entryOrderID):
#             break
#         time.sleep(1)
#
#     # 逆指値売り注文
#     SendOrderExit.send_order_exit()
#
# 　　　# 引けまでsleep
# 　　　for i in range(270):
# 　　    time.sleep(60)
#
#     # 逆指値売り注文キャンセル
#     CanselOrder.cancel_order()
#
#     while True:
#         # 全約定するまで待つ
#         if OrderInfo.orders_info(variables.cancelOrderID):
#             break
#         time.sleep(1)
#
#     # 成行売り注文
#     SendOrderExitMarket.send_order_exit_market()
#
# else:

now_time = dt.now()
entry_time = now_time.replace(hour=10, minute=00)
exit_time = now_time.replace(hour=11, minute=20)

while True:
    now_time = dt.now()
    if now_time > entry_time:
        break
    time.sleep(10)

while variables.curPrice == 0:
    Board.board()

# 最高値が前日終値を300円以上上がっているか
if variables.highPrice - variables.preClose <= 300:
    sys.exit()

# 現在値が前日終値を上回っているか
if variables.curPrice < variables.preClose:
    sys.exit()

SendOrderEntryCredit.send_order_entry()

while True:
    # 全約定するまで待つ
    if OrderInfo.orders_info(variables.entryOrderID):
        break
    time.sleep(1)

# 逆指値買い注文
SendOrderExitCredit.send_order_exit()


while True:
    now_time = dt.now()
    if now_time > exit_time:
        break
    time.sleep(10)

# 逆指値買い注文キャンセル
CanselOrder.cancel_order()

while True:
    # 全約定するまで待つ
    if OrderInfo.orders_info(variables.cancelOrderID):
        break
    time.sleep(1)

# 成行買い注文
SendOrderExitMarketCredit.send_order_exit_market()
