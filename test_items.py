link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"




def test_basket(browser):
    browser.get(link)
    basket=browser.find_element_by_css_selector(".btn.btn-add-to-basket")
    assert basket,"basket not found"

