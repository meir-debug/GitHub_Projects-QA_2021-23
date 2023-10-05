from selenium import webdriver
import requests
from selenium.common.exceptions import TimeoutException as TE
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Helpers as Hp
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
# import AllureReports
# import HtmlTestRunner


class LogIn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_search(self):
        driver = self.driver
        # workflow over "elem" and "wait" variable to better code length
        elem = driver.find_element
        wait = WebDriverWait(driver, 5)
        driver.get(Hp.url_Test)

        # API testing from Selenium
        print("AliceBlue Florist Url has", requests.get(Hp.url_Test).status_code,
              "as status Code")
        code = requests.get(Hp.url_Test).status_code

        print("API response code is OK") if code == 200 else print("API response code is not 200")

        if Hp.Title not in driver.title:
            raise Exception("AliceBlue Florist - page has wrong Title!")
        Hp.delay()
        # Check that an element is present on the DOM of a page and visible.
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "ALICEBLUE FLORIST")))
            print("First Page is ready!")
        except TE:
            print("Loading took too much time!")
            driver.get_screenshot_as_file(Hp.error_png)
            driver.save_screenshot(Hp.error_png)

        # Checking page title
        self.assertIn(Hp.Title, driver.title)
        print("Page has", driver.title + " as Page title")
        Hp.delay()
        elem(By.XPATH, Hp.logIn).click()
        try:
            wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h1[@data-testid='signUp.headline']")))
            print("Second Page is ready!")
        except TE:
            print("Loading took too much time!")
            driver.get_screenshot_as_file(Hp.error_png)
            driver.save_screenshot(Hp.error_png)
        Hp.delay()
        elem(By.XPATH, Hp.sUp_withEmail).click()
        elem(By.XPATH, Hp.input_em).clear()
        elem(By.XPATH, Hp.input_em).send_keys(Hp.fake.email())
        elem(By.XPATH, Hp.input_pas).clear()
        elem(By.XPATH, Hp.input_pas).send_keys(Hp.fake.ean(length=8))
        Hp.delay()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     unittest.main(
#         testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))

# if __name__ == '__main__':
#   unittest.main(AllureReports)

# py.test --alluredir=./AllureReports ./unittest4.py
