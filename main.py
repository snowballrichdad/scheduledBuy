import time

import Board
import SendOrderEntry
import OrderInfo
import SendOrderExit
import CanselOrder
import SendOrderExitMarket
import variables

Board.board()
SendOrderEntry.send_order_entry()

while True:
    # 全約定するまで待つ
    if OrderInfo.orders_info(variables.entryOrderID):
        break
    time.sleep(1)

# 逆指値売り注文
SendOrderExit.send_order_exit()

# 引けまでsleep
time.sleep(16200)

# 逆指値売り注文キャンセル
CanselOrder.cancel_order()

while True:
    # 全約定するまで待つ
    if OrderInfo.orders_info(variables.cancelOrderID):
        break
    time.sleep(1)

# 成行売り注文
SendOrderExitMarket.send_order_exit_market()

