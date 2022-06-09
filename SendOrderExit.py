import urllib.request
import urllib.error
import pprint
import json
import sys

import password
import settings
import variables


def send_order_exit():
    obj = {'Password': password.password,
           'Symbol': settings.symbol,
           'Exchange': 1,
           'SecurityType': 1,
           'Side': 1,
           'CashMargin': 3,
           'MarginTradeType': 3,
           'DelivType': 2,
           'AccountType': 4,
           'Qty': settings.qty,
           'ClosePositionOrder': 0,
           'Price': 0,
           'ExpireDay': 0,
           'FrontOrderType': 30,
           'ReverseLimitOrder': {
               'TriggerSec': 1,
               'TriggerPrice': variables.orderPrice - 200,
               'UnderOver': 1,
               'AfterHitOrderType': 1,
               'AfterHitPrice': 0
           }}
    json_data = json.dumps(obj).encode('utf-8')

    url = 'http://localhost:' + settings.port + '/kabusapi/sendorder'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', settings.token)

    try:
        print('###sendorder_exit')
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
            print()
            content = json.loads(res.read())
            pprint.pprint(content)

            # エントリ注文の注文IDを保存
            variables.exitOrderID = content['OrderId']

            return

    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)

    sys.exit()
