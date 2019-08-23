from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage

class SearchResultPage(BasePage):

    basePage = BasePage()
    SEARCH_RESULT_CARD_CSS = (By.CSS_SELECTOR, ".cardContainer .card")
    TICKET_PRICE_CSS = (By.CSS_SELECTOR,".fltPrice .ico22")

    STOP_FILTER_ID = (By.ID,"stopsFilter")
    NON_STOP_CHECKBOX_ID = (By.XPATH,"//*[@id='stop_0']")

    #check if search results are displayed
    def are_search_result_present(self,browser):
        return self.basePage.is_visible(self.SEARCH_RESULT_CARD_CSS,browser)

    #check all search results are sorted by price low to high
    def are_results_ordered_by_price_low_to_high(self, browser):
        self.basePage.scrollToBottom(browser)
        price_list = self.basePage.find_text_of_all_elements(self.TICKET_PRICE_CSS,browser)
        sorted_list = price_list
        sorted_list.sort()
        return True if price_list == sorted_list else False

    def select_non_stop(self,browser):
        ActionChains(browser).move_to_element(self.basePage.find_element(self.STOP_FILTER_ID,browser)).perform()
        browser.execute_script("document.getElementById('stop_0').click()")
        #self.basePage.wait_and_click(self.NON_STOP_CHECKBOX_ID,browser)

    def get_third_cheapest_flight(self,browser,index):
        self.basePage.scrollToBottom(browser)
        price_list = self.basePage.find_text_of_all_elements(self.TICKET_PRICE_CSS, browser)
        price_list=sorted(set(price_list))
        if len(price_list) < index:
            return price_list[-1]
        else:
            price_list = price_list[0:index]
            return price_list[index-1]



















