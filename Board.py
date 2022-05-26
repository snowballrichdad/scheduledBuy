import urllib.request
import urllib.error
import settings
import json
import pprint
import sys

import variables


def board():
    url = 'http://localhost:' + settings.port + '/kabusapi/board/' + settings.symbol + '@1'
    req = urllib.request.Request(url, method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', settings.token)

    print('###board', end=" ")

    try:
        with urllib.request.urlopen(req) as res:
            content = json.loads(res.read())
            variables.curPrice = content["CurrentPrice"]
            print("CurrentPrice", end=":")
            print(variables.curPrice, end=" ")

            variables.preClose = content["PreviousClose"]
            print("PreviousClose", end=":")
            print(variables.preClose, end=" ")

            variables.highPrice = content["HighPrice"]
            print("HighPrice", end=":")
            print(variables.highPrice, end=" ")

            variables.lowPrice = content["LowPrice"]
            print("LowPrice", end=":")
            print(variables.lowPrice)

    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
        sys.exit()
    except Exception as e:
        print(e)
        sys.exit()
