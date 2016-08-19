from functools import wraps

from gevent_timer import set_interval
from gevent.queue import Queue
import gevent


class Ticker:
    thread = None

    def __init__(self, times, period=1):
        self.times = times
        self.period = period

        self.queue = Queue(times)

    def _tick(self):
        if self.thread:
            left = self.times - self.queue.qsize()
            for _ in range(left):
                self.queue.put(None)

    def next_tick(self):
        self.queue.get()

    def start(self):
        if not self.thread:
            self.thread = gevent.spawn(set_interval, self._tick, self.period)
            self._tick()

    def stop(self):
        if self.thread:
            self.thread.kill()
            self.thread = None


def ticker(times, period=None):
    loop = Ticker(times, period)
    loop.start()

    def decorator(func):
        @wraps(func)
        def func_wrapper(*args, **kwargs):
            loop.next_tick()
            result = func(*args, **kwargs)
            return result

        return func_wrapper

    return decorator
