from Automated_tests.generate_browsers import generate_chrome_driver
from Automated_tests.BeeRelaxed.page_model_user import LoginPage


class TestPassword(object):
    def __init__(self):
        self.login_page = None

    def setup_method(self):
        driver = generate_chrome_driver()
        self.login_page = LoginPage(driver)
        self.login_page.get()

    def teardown_method(self):
        self.login_page.quit()


    def test_user_registration(self):
        page = LoginPage(self.driver)
        page.bar_button_login().click()
        page.input_username().send_keys('test@email.com')
        page.input_password().send_keys('TestPW1!')
        page.button_login_page().click()
        assert page.bar_button_logout().is_displayed()