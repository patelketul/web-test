from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class BasePage():

    def find_element(self,locator,browser):
        try:
            wait = WebDriverWait(browser,30)
            locator = wait.until(EC.visibility_of_element_located(locator))
            return locator
        except TimeoutException:
            raise TimeoutException("Element is not clickable with locator" + locator.__str__())

    def find_element_count(self,locator,browser):
        self.find_element(locator,browser)
        elements = browser.find_elements(*locator)
        return len(elements)

    def wait_and_click(self, locator, browser):
        try:
            wait = WebDriverWait(browser, 30)
            locator = wait.until(EC.element_to_be_clickable(locator))
            locator.click()
        except TimeoutException:
            raise TimeoutException("Element is not clickable with locator" + locator.__str__())

    def wait_and_type(self, locator, browser, text):
        try:
            wait = WebDriverWait(browser, 30)
            locator = wait.until(EC.visibility_of_element_located(locator))
            locator.clear()
            locator.send_keys(text)
        except TimeoutException:
            raise TimeoutException("Element is not clickable with locator" + locator.__str__())

    def get_element_text(self,locator,browser):
        locator = self.find_element(locator,browser)
        return locator.text

    def find_all_elements_by_locator(self,locator,browser):
        return browser.find_elements(*locator)

    def find_text_of_all_elements(self,locator,browser):
        elements = self.find_all_elements_by_locator(locator,browser)
        text = []
        for ele in elements:
            text.append(int((ele.text).replace(',', '')))
        return text

    def go_to_url(self,browser,url):
        browser.get(url)

    def is_visible(self,locator,browser):
        try:
            wait = WebDriverWait(browser, 30)
            wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def scrollToBottom(self, browser):
        last_height = browser.execute_script("return document.body.scrollHeight")

        while True:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            new_height = browser.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        browser.execute_script("document.documentElement.scrollTop = 0")


