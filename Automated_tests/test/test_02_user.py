from Automated_tests.generate_browsers import generate_chrome_driver_headless
from Automated_tests.BeeRelaxed.page_model_user import LoginPage


class TestUserLogin(object):

    def setup_method(self):
        driver = generate_chrome_driver_headless()
        self.login_page = LoginPage(driver)
        self.login_page.get()

    def teardown_method(self):
        self.login_page.quit()


    def test_user_registration(self):
        self.login_page.bar_button_login().click()
        self.login_page.input_username().send_keys('test@email.com')
        self.login_page.input_password().send_keys('TestPW1!')
        self.login_page.button_login_page().click()
        assert self.login_page.bar_button_logout().is_displayed()