from selenium.webdriver.common.by import By
from PageObject.BasePage import BasePage

class HomePage(BasePage):

    basePage = BasePage()

    #ELEMENTS FROM PAGE HEADER
    FLIGHTS_LINK_CSS = (By.CSS_SELECTOR,"a[href='/flights/']")
    FLIGHTS_ACTIVE_LINK_CSS = (By.CSS_SELECTOR,"li.active a[href='/flights/']")
    HOTELS_LINK_CSS = (By.CSS_SELECTOR, "a[href='/hotels/']")
    GO_STAY_HOTELS_LINK_CSS = (By.CSS_SELECTOR, "a[href='/gostays/']")
    BUS_LINK_CSS = (By.CSS_SELECTOR, "a[href='/bus/']")
    IRCTC_TRAINS_LINK_CSS = (By.CSS_SELECTOR, "a[href='/trains/']")
    CABS_LINK_CSS = (By.CSS_SELECTOR, "a[href='/cars/']")
    MORE_LINK_CSS = (By.CSS_SELECTOR,"li.hdrMoreLink")

    AVAIL_GO_CASH_LINK_CSS = (By.CSS_SELECTOR,"span.availGocash")
    EARN_CREDIT_LINK_CSS =(By.CSS_SELECTOR,"a.hdrgoCash span.posRel")
    USER_WIDGET_ID = (By.ID,"hd_user_widdget")

    #FLIGHT TICKET BOOKING ELEMENTS
    ONE_WAY_BUTTON_CSS = (By.XPATH,"//div[contains(@class,'fltSwitchOpt')]/span[.='One way' and @class='curPointFlt switchAct']")
    ONE_WAY_BUTTON_SELECTED_CSS = (By.XPATH,"//div[contains(@class,'fltSwitchOpt')]/span[.='One way']")
    ROUND_TRIP_BUTTON_CSS = (By.XPATH, "//div[contains(@class,'fltSwitchOpt')]/span[.='Round trip']")
    MULTI_CITY_BUTTON_CSS = (By.XPATH, "//div[contains(@class,'fltSwitchOpt')]/span[.='Multicity']")

    SUGGESTION_CSS = (By.CSS_SELECTOR,".autoSuggestBoxList li")
    FROM_TEXTBOX_ID = (By.ID,"gosuggest_inputSrc")
    DESTINATION_TEXTBOX_ID = (By.ID,"gosuggest_inputDest")
    DEPARTURE_DATE_SELECTOR_CSS = (By.CSS_SELECTOR,"input[placeholder='Departure']")
    TODAYS_DATE_CSS = (By.CSS_SELECTOR,"div.DayPicker-Day--today")
    RETURN_DATE_SELECTOR_CSS = (By.CSS_SELECTOR,"input[placeholder='Return']")
    CLASS_COUNT_SELECTOR_ID = (By.ID,"pax_link_common")
    SEARCH_BUTTON_ID = (By.ID,"gi_search_btn")
    STUDENT_FARE_BUTTON_ID = (By.ID,"student_fare_check")

    NEXT_MONTH_BUTTON_CSS = (By.CSS_SELECTOR, ".DayPicker-NavButton.DayPicker-NavButton--next")
    MONTH_NAME_LABEL_CSS = (By.CSS_SELECTOR, ".DayPicker-Caption")
    DATE_PICKER_XPATH = (By.XPATH, "//div[@class='DayPicker-Day' and contains(@aria-label,'{}')]")


    def is_flights_link_present(self, browser):
        return self.basePage.is_visible(self.FLIGHTS_LINK_CSS,browser)

    #check is flights link is selected
    def is_flights_link_selected(self,browser):
        return self.basePage.is_visible(self.FLIGHTS_ACTIVE_LINK_CSS,browser)

    def is_hotels_link_present(self, browser):
        return self.basePage.is_visible(self.HOTELS_LINK_CSS, browser)

    def is_go_stay_link_present(self, browser):
        return self.basePage.is_visible(self.GO_STAY_HOTELS_LINK_CSS, browser)

    def is_bus_link_present(self, browser):
        return self.basePage.is_visible(self.BUS_LINK_CSS, browser)

    def is_irctc_trains_link_present(self, browser):
        return self.basePage.is_visible(self.IRCTC_TRAINS_LINK_CSS, browser)

    def is_cabs_link_present(self, browser):
        return self.basePage.is_visible(self.CABS_LINK_CSS, browser)

    def is_more_link_present(self, browser):
        return self.basePage.is_visible(self.MORE_LINK_CSS, browser)

    def is_avail_gocash_link_present(self,browser):
        return self.basePage.is_visible(self.AVAIL_GO_CASH_LINK_CSS, browser)

    def is_earn_credit_link_present(self,browser):
        return self.basePage.is_visible(self.EARN_CREDIT_LINK_CSS, browser)

    def is_user_widget_link_present(self,browser):
        return self.basePage.is_visible(self.USER_WIDGET_ID,browser)

    def is_one_way_trip_button_present(self, browser):
        return self.basePage.is_visible(self.ONE_WAY_BUTTON_CSS, browser)

    def is_one_way_trip_button_selected(self, browser):
        return self.basePage.is_visible(self.ONE_WAY_BUTTON_SELECTED_CSS, browser)

    def is_round_trip_button_present(self, browser):
        return self.basePage.is_visible(self.ROUND_TRIP_BUTTON_CSS, browser)

    def is_multi_city_button_present(self, browser):
        return self.basePage.is_visible(self.MULTI_CITY_BUTTON_CSS, browser)

    def is_from_textbox_present(self, browser):
        return self.basePage.is_visible(self.FROM_TEXTBOX_ID, browser)

    def is_destination_textbox_present(self, browser):
        return self.basePage.is_visible(self.DESTINATION_TEXTBOX_ID, browser)

    def is_departure_date_selector_present(self, browser):
        return self.basePage.is_visible(self.DEPARTURE_DATE_SELECTOR_CSS, browser)

    def is_return_date_selector_present(self, browser):
        return self.basePage.is_visible(self.RETURN_DATE_SELECTOR_CSS, browser)

    def is_class_count_selector_present(self, browser):
        return self.basePage.is_visible(self.CLASS_COUNT_SELECTOR_ID, browser)

    def is_search_button_present(self, browser):
        return self.basePage.is_visible(self.SEARCH_BUTTON_ID, browser)

    def is_student_fare_button_present(self, browser):
        return self.basePage.is_visible(self.STUDENT_FARE_BUTTON_ID, browser)

    def enter_from_city(self,browser,from_city):
        self.basePage.wait_and_type(self.FROM_TEXTBOX_ID, browser, from_city)
        self.basePage.wait_and_click(self.SUGGESTION_CSS,browser)

    def enter_destination_city(self,browser,desti_city):
        self.basePage.wait_and_type(self.DESTINATION_TEXTBOX_ID, browser, desti_city)
        self.basePage.wait_and_click(self.SUGGESTION_CSS,browser)

    def select_departure_date(self,browser):
        self.basePage.wait_and_click(self.DEPARTURE_DATE_SELECTOR_CSS, browser)
        self.basePage.wait_and_click(self.TODAYS_DATE_CSS, browser)

    def click_search_button(self,browser):
        self.basePage.wait_and_click(self.SEARCH_BUTTON_ID, browser)

    def click_next_month_button(self,browser):
        self.basePage.wait_and_click(self.NEXT_MONTH_BUTTON_CSS,browser)

    def get_month_label(self,browser):
        self.basePage.get_element_text(self.MONTH_NAME_LABEL_CSS, browser)

    def select_month_date(self,browser,month, date):
        self.basePage.wait_and_click(self.DEPARTURE_DATE_SELECTOR_CSS, browser)
        while not month in self.basePage.get_element_text(self.MONTH_NAME_LABEL_CSS,browser):
            self.basePage.wait_and_click(self.NEXT_MONTH_BUTTON_CSS,browser)

        test_list = list(self.DATE_PICKER_XPATH)
        test_list[1] = test_list[1].format(date)
        tup = tuple(test_list)
        self.basePage.wait_and_click(tup,browser)













