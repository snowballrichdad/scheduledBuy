import time
from datetime import datetime as dt

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

SendOrderEntry.send_order_entry()

while True:
    # 全約定するまで待つ
    if OrderInfo.orders_info(variables.entryOrderID):
        break
    time.sleep(1)

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
