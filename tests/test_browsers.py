from seo import browsers


def test_get_browser():
    random_browser = browsers.browser()
    assert random_browser is not None
