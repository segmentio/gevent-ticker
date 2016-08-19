# gevent-ticker

pip install gevent_ticker

inspired by [Golang's tickers](https://golang.org/pkg/time/#Ticker)

# usage

```python
from gevent_ticker import ticker, Ticker
import requests


# decorator
@ticker(times=20, period=100) # Max 100 requests every 20 seconds
def make_request(i):
  res = requests.get(...)
  return res.json()


# or DIY
loop = Ticker(20, 100)

for i in range(100):
  loop.next_tick()
  res = make_request()

  if res['done']:
    loop.stop()
    break
```
