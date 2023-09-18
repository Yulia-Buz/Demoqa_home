from conftest import browser
from pages.swag_labs import Labs

def test_icon_exist(browser):
    demoqa_home_page = Labs(browser)
    demoqa_home_page.visit()
    assert demoqa_home_page.username()
    assert demoqa_home_page.password()
    assert demoqa_home_page.exist_icon()
