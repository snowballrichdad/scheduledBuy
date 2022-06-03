import sys
# import MySQLdb
from datetime import datetime as dt

port = "18080"

# token読み込み
f = open(r'..\morningScal\token.txt', 'r')
token = f.read()
f.close()

symbol = "1570"
qty = 50
qty2 = 1

now_time = dt.now()

entry_time = now_time.replace(hour=10, minute=0)
exit_time = now_time.replace(hour=11, minute=20)

entry_time2 = now_time.replace(hour=10, minute=15)
exit_time2 = now_time.replace(hour=14, minute=50)

now_time = dt.now()

# 標準出力をファイルに
tstr = now_time.strftime('%Y%m%d%H%M%S')


class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("c:\\data\\" + tstr + ".log", "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        self.log.flush()

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass


sys.stdout = Logger()
sys.stderr = Logger()
