from seo.browsers import Browser


def test_get_rand_useragent():
    browser = Browser()
    random_browser = browser.get_rand_useragent()
    
    assert random_browser is not None


def test_get_fake_headers():
    browser = Browser()
    headers = browser.get_fake_headers()

    assert headers['Accept'] == 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8' # noqa
    assert headers['Accept-Encoding'] == 'gzip, deflate'
    assert headers['Accept-Language'] == 'en-US,en;q=0.9,ms;q=0.8,te;q=0.7'
    assert headers['Cache-Control'] == 'max-age=0'
    assert headers['Content-Type'] == 'application/x-www-form-urlencoded'
