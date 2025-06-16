from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def generate_chrome_driver():
    options = ChromeOptions()
    options.add_argument('--disable-search-engine-choice-screen')
    options.add_experimental_option("detach", True)   # works now, since this is ChromeOptions
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome(options=options)

def generate_chrome_driver_headless():
    options = ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument("--window-size=2560,1440")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-search-engine-choice-screen')
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.set_window_size(2560, 1440)
    return driver

def generate_firefox_driver():
    options = FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    return webdriver.Firefox(options=options)