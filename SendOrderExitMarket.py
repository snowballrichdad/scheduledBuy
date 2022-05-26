import urllib.request
import urllib.error
import pprint
import json
import sys

import password
import settings


def send_order_exit_market():
    obj = {'Password': password.password,
           'Symbol': settings.symbol,
           'Exchange': 1,
           'SecurityType': 1,
           'Side': 1,
           'CashMargin': 1,
           'DelivType': 0,
           'FundType': '  ',
           'AccountType': 4,
           'Qty': 1,
           'FrontOrderType': 10,
           'Price': 0,
           'ExpireDay': 0}
    json_data = json.dumps(obj).encode('utf-8')

    url = 'http://localhost:' + settings.port + '/kabusapi/sendorder'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', settings.token)

    try:
        print('###sendorder_exit_market')
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
            print()
            content = json.loads(res.read())
            pprint.pprint(content)

            return

    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)

    sys.exit()
