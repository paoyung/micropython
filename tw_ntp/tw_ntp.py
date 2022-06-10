# name: tw_ntp.py
# version: 0.1.0
# author: paoyung.chang@gmail.com

import time
import ntptime

def tw_ntp(host='clock.stdtime.gov.tw', must=False):
  """
  host: 台灣可用的 ntp server 如下可任選，未指定預設為 clock.stdtime.gov.tw
    tock.stdtime.gov.tw
    watch.stdtime.gov.tw
    time.stdtime.gov.tw
    clock.stdtime.gov.tw  
    tick.stdtime.gov.tw
  must: 是否非對到不可
  """
  ntptime.NTP_DELTA = 3155644800 # UTC+8 的 magic number
  ntptime.host = host
  count = 1
  if must:
    count = 100
  for _ in  range(count):
    try:
      ntptime.settime()
    except:
      time.sleep(1)
      continue
    else:
      return True
  return False

"""
example:
tw_ntp()              # 使用預設值
tw_ntp(must=True)     # 非對到時不可
tw_ntp(must=1)        # 同上
tw_ntp('tick.stdtime.gov.tw', 1) # 指定server，並強制對時
"""
