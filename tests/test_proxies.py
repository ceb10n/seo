from seo.proxies import Proxy


def test_next_proxy():
    proxy = Proxy([
        '111.111.1.1',
        '111.111.1.2',
        '111.111.1.3',
        '111.111.1.4'])

    for i in range(10):
        assert proxy.get_next() is not None


def test_get_random():
    proxy = Proxy([
        '111.111.1.1',
        '111.111.1.2',
        '111.111.1.3',
        '111.111.1.4'])

    assert proxy.get_random() is not None
