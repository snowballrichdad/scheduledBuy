import urllib.request
import urllib.error
import settings
import json
import pprint
import sys


def board():
    url = 'http://localhost:' + settings.port + '/kabusapi/board/' + settings.symbol + '@1'
    req = urllib.request.Request(url, method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', settings.token)

    print('###board', end=" ")

    try:
        with urllib.request.urlopen(req) as res:
            content = json.loads(res.read())
            pre_close = content["PreviousClose"]
            print("PreviousClose", end=":")
            print(pre_close, end=" ")
            high_price = content["HighPrice"]
            print("HighPrice", end=":")
            print(high_price)

            # 最高値と前日終値の比較
            # if high_price - pre_close >= 200:
                # 閾値以上上がってたら取引しない
                # sys.exit()

    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
        sys.exit()
    except Exception as e:
        print(e)
        sys.exit()
