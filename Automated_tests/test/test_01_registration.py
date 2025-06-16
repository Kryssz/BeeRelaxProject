import time

from Automated_tests.BeeRelaxed.page_model_registration import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from Automated_tests.generate_browsers import generate_chrome_driver_headless

URL = 'http://localhost:4200/register'


class TestTC(object):
    def setup_method(self):
        options = Options()
        options.add_argument('--disable-search-engine-choice-screen')
        options.add_experimental_option("detach", True)
        self.driver = generate_chrome_driver_headless()
        self.driver.get(URL)
        self.wait = WebDriverWait(self.driver, 5)


    def teardown_method(self):
        pass #self.driver.quit()

    def test_tc1(self):
        page = LoginPage(self.driver)
        page.input_first_name().send_keys('Test')
        page.input_last_name().send_keys('Registration')
        page.input_phone_number().send_keys('+49123456789')
        page.input_email().send_keys('test@email.com')
        page.input_password().send_keys('TestPW1!')
        page.input_zipcode().send_keys('85055')
        page.input_city().send_keys('Ingolstadt')
        page.input_address().send_keys('Test Strasse, 7')
        page.role_user().click()
        page.button_submit().click()