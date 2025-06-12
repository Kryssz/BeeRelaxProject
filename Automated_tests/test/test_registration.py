import shutil
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from Automated_tests.BeeRelaxed.page_model_registration import LoginPage
from Automated_tests.generate_browsers import generate_chrome_driver_headless

URL = 'http://localhost:4200/register'


class TestTC(object):
    def setup_method(self):
        options = Options()
        options.add_argument('--disable-search-engine-choice-screen')
        options.add_experimental_option("detach", True)
        self.driver, self.profile_dir  = generate_chrome_driver_headless()
        self.driver.get(URL)
        self.wait = WebDriverWait(self.driver, 5)

    def teardown_method(self):
        self.driver.quit()
        shutil.rmtree(self.profile_dir, ignore_errors=True)

    def test_tc1(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//button/a[text()="Register"]'))).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//select/option[@value="ROLE_BEEFAMILY"]'))).click()