import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_the_basket(browser):
    browser.get(link)
    btn = browser.find_element_by_css_selector('.btn-add-to-basket')
    #time.sleep(30)
    assert btn.is_displayed()
