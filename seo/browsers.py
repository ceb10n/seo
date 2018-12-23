# -*- coding: utf-8 -*-
"""The browsers module contains browser related utils .
"""
import random


class Browser:

    def __init__(self):
        self.browsers = []
        
        self._load_browsers()
        self._browser_count = len(self.browsers)

    def _load_browsers(self):
        self.browsers = [
            ['Chrome 70.0.3538.77', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'], # noqa
            ['Chrome 44.0.2403.155', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36'], # noqa
            ['Chrome 41.0.2228.0', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'], # noqa
            ['Chrome 41.0.2227.1', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36'],  # noqa
            ['Firefox 64.0', 'Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0'], # noqa
            ['Firefox 64.0', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0'], # noqa
            ['Firefox 63.0', 'Mozilla/5.0 (X11; Linux i586; rv:63.0) Gecko/20100101 Firefox/63.0'], # noqa
            ['Firefox 63.0', 'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0'], # noqa
            ['Firefox 62.0', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:62.0) Gecko/20100101 Firefox/62.0'], # noqa
            ['Firefox 60.0', 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.13; ko; rv:1.9.1b2) Gecko/20081201 Firefox/60.0'], # noqa
            ['Firefox 58.0.1', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/58.0.1'], # noqa
            ['Firefox 58.0', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/58.0'], # noqa
            ['Edge 14.14931', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14931'], # noqa
            ['Edge 14.14393', 'Chrome (AppleWebKit/537.1; Chrome50.0; Windows NT 6.3) AppleWebKit/537.36 (KHTML like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393'], # noqa
            ['Edge 13.9200', 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.9200'], # noqa
            ['Edge 13.10586', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'], # noqa
            ['Edge 12.246', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'], # noqa
            ['Opera 12.16', 'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16'], # noqa
            ['Opera 12.16', 'Opera/9.80 (Macintosh; Intel Mac OS X 10.14.1) Presto/2.12.388 Version/12.16'], # noqa
            ['Opera 12.14', 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14'], # noqa
            ['Opera 12.14', 'Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14'], # noqa
            ['Opera 12.14', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14'], # noqa
            ['Opera 12.02', 'Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02'], # noqa
            ['Opera 12.00', 'Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00'], # noqa
            ['Opera 12.00', 'Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00'], # noqa
            ['Opera 12.00', 'Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00'], # noqa
            ['Opera 12.00', 'Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00'], # noqa
            ['Opera 12.00', 'Mozilla/5.0 (Windows NT 5.1) Gecko/20100101 Firefox/14.0 Opera/12.0'], # noqa
            ['Opera 11.62', 'Opera/9.80 (Windows NT 6.1; WOW64; U; pt) Presto/2.10.229 Version/11.62'], # noqa
            ['Opera 11.62', 'Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.10.229 Version/11.62'], # noqa
            ['Safari 7.0.3', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'], # noqa
            ['Safari 6.0', 'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25'], # noqa
            ['Safari 5.1.7', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.13+ (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2'], # noqa
            ['Safari 5.1.3', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'], # noqa
            ['Safari 5.1', 'Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko ) Version/5.1 Mobile/9B176 Safari/7534.48.3'] # noqa
        ]

    def get_rand_useragent(self):
        """Return a string with a random useragent.

        Example::
            browser = Browser()
            useragent = browser.get_rand_useragent()
            useragent
            'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16'

        """
        index = random.randint(0, self._browser_count)

        return self.browsers[index][1]


    def get_fake_headers(self, useragent=None):
        """Return a dict containing header informations.

        If a useragent is not informed, it will use a random one
        returned by get_rand_useragent.

        Example::
            browser = Browser()
            headers = browsers.get_fake_headers()
            headers
            {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9,ms;q=0.8,te;q=0.7",
                "Cache-Control": "max-age=0",
                "Content-Type": "application/x-www-form-urlencoded",
                'User-Agent': "Mozilla/5.0 (X11; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0"}

        Args:
            useragent (str): The user-agent header used in request

        Returns:
            A dict containing:
                * Accept
                * Accept-Encoding
                * Accept-Language
                * Cache-Control
                * Content-Type
                * User-Agent
        """

        if not useragent:
            # get a random useragent to return in fake headers
            useragent = self.get_rand_useragent()

        return {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", # noqa
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9,ms;q=0.8,te;q=0.7",
            "Cache-Control": "max-age=0",
            "Content-Type": "application/x-www-form-urlencoded",
            'User-Agent': useragent}