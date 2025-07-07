import time
import sys

symbols = ['|', '/', '-', '\\', '|', '/', '-', '\\', '|']

for _ in range(20):  # 20 cycles
    for symbol in symbols:
        sys.stdout.write('\r' + symbol)
        sys.stdout.flush()
        time.sleep(0.15)
