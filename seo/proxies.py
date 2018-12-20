import random
import itertools


class Proxy:

    def __init__(self, proxies):
        self.proxies = proxies
        self.proxy_count = len(self.proxies)
        self._rotating_proxy = itertools.cycle(proxies)

    def get_random(self):
        index = random.randint(0, self.proxy_count)

        return self.proxies[index]

    def get_next(self):
        return next(self._rotating_proxy)
