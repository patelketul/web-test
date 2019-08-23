from PageObject.HomePage import HomePage
from PageObject.Search_results_Page import SearchResultPage
from selenium import webdriver
import json
from utils.delayed_assert import expect, assert_expectations

class TestLocus():

    def setup_method(self):
        self.browser = webdriver.Chrome(executable_path="../Drivers/chromedriver")
        self.testData = json.loads(open("../TestData/data.json").read())
        self.browser.set_window_size(1600,1200)
        self.home_page = HomePage()
        self.search_result_page = SearchResultPage()
        self.home_page.go_to_url(self.browser,self.testData["homePageUrl"])

    #Load the home page and see if elements are displayed or not
    def test_verify_homepage(self):
        #check all header menus
        expect(self.home_page.is_flights_link_present(self.browser),"Flights link is not present")
        expect(self.home_page.is_flights_link_selected(self.browser), "Flights link is not selected by default")
        expect(self.home_page.is_hotels_link_present(self.browser), "Hotels link is not present")
        expect(self.home_page.is_go_stay_link_present(self.browser), "Go stay link is not present")
        expect(self.home_page.is_bus_link_present(self.browser), "Bus link is not present")
        expect(self.home_page.is_irctc_trains_link_present(self.browser), "IRCTC Trains link is not present")
        expect(self.home_page.is_cabs_link_present(self.browser), "Cabs link is not present")
        expect(self.home_page.is_more_link_present(self.browser), "More link is not present")
        expect(self.home_page.is_avail_gocash_link_present(self.browser), "Avail Go Cash link is not present")
        expect(self.home_page.is_earn_credit_link_present(self.browser), "Earn credit link is not present")
        expect(self.home_page.is_user_widget_link_present(self.browser), "User widget link is not present")
        expect(self.home_page.is_one_way_trip_button_present(self.browser),"One way trip button is not present")
        expect(self.home_page.is_one_way_trip_button_selected(self.browser), "One way trip button is not selected by default")
        expect(self.home_page.is_round_trip_button_present(self.browser), "Round trip button is not present")
        expect(self.home_page.is_multi_city_button_present(self.browser), "Multi city button is not present")
        expect(self.home_page.is_from_textbox_present(self.browser), "From textbox is not present")
        expect(self.home_page.is_destination_textbox_present(self.browser), "Destination textbox is not present")
        expect(self.home_page.is_departure_date_selector_present(self.browser), "Departure date selector is not present")
        expect(self.home_page.is_return_date_selector_present(self.browser), "Return date selector is not present")
        expect(self.home_page.is_class_count_selector_present(self.browser), "Class count selector is not present")
        expect(self.home_page.is_search_button_present(self.browser), "Search button is not present")
        expect(self.home_page.is_student_fare_button_present(self.browser), "Student fare button is not present")
        assert_expectations()

    #Check if search page is loaded with results and check is results are sorted by price low to high
    def test_search_one_way_flights(self):
        self.home_page.enter_from_city(self.browser, self.testData["from_city"])
        self.home_page.enter_destination_city(self.browser, self.testData["destination_city"])
        self.home_page.select_departure_date(self.browser)
        self.home_page.select_month_date(self.browser,self.testData["month"], self.testData["date"])
        self.home_page.click_search_button(self.browser)
        expect(self.search_result_page.are_search_result_present(self.browser), "Search results are not present on the page")
        expect(self.search_result_page.are_results_ordered_by_price_low_to_high(self.browser), "Search results are not sorted")
        self.search_result_page.select_non_stop(self.browser)
        print("Third cheapest flight is ",self.search_result_page.get_third_cheapest_flight(self.browser,5))
        assert_expectations()

    def teardown_method(self):
        self.browser.quit()

