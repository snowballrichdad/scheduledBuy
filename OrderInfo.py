import urllib.request
import urllib.parse
import urllib.error
import json
import pprint
import settings
import variables
import sys


def orders_info(orderId):
    url = 'http://localhost:' + settings.port + '/kabusapi/orders'
    params = {'product': 0, 'id': orderId}
    req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)), method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', settings.token)

    try:
        print('###order_info')
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
            print()
            res_json = res.read()
            content = json.loads(res_json)
            pprint.pprint(content)

            first_order = content[len(content) - 1]

            # 注文状態を取得
            print(first_order['State'])
            state = first_order['State']
            # 全約定じゃない場合はFalse
            if state != 5:
                return False

            # 注文情報を取得
            print(first_order['Details'])
            order_details = first_order['Details']

            for orderDetail in order_details:
                hold_id = orderDetail['ExecutionID']
                if hold_id is None:
                    continue

                # エントリ値で最も低い値をエントリ値にする
                if variables.orderPrice is None or orderDetail['Price'] < variables.orderPrice:
                    variables.orderPrice = orderDetail['Price']

            return True

    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)

    sys.exit()


# if __name__ == "__main__":
#     import sys
#
#     tradeP = TradeC.TradeC("test")
#     orders_info(tradeP)
