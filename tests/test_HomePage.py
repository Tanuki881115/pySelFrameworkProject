from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage
from TestData.HomePageData import HomePageData
import pytest


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()

        homepage = HomePage(self.driver)

        log.info("first_name is " + getData["first_name"])

        homepage.getName().send_keys(getData["first_name"])
        # homepage.getName().send_keys(getData[0])
        # homepage.getName().send_keys("Tito")
        # driver.find_element_by_css_selector("[name='name']").send_keys("Tito")

        homepage.getEmail().send_keys(getData["last_name"])
        # homepage.getEmail().send_keys(getData[1])
        # homepage.getEmail().send_keys("Novianto")
        # driver.find_element_by_name("email").send_keys("Novianto")

        homepage.getCheckBoxBtn().click()
        # driver.find_element_by_id("exampleCheck1").click()

        self.selectOptionByText(homepage.getGenderSel(), getData["gender"])
        # self.selectOptionByText(homepage.getGenderSel(), getData[2])
        # self.selectOptionByText(homepage.getGenderSel(), "Male")
        # sel = Select(driver.find_element_by_id("exampleFormControlSelect1"))
        # sel.select_by_visible_text("Male")

        homepage.getSubmitBtn().click()
        # driver.find_element_by_xpath("//input[@value='Submit]").click()

        alertText = homepage.getAlertText().text
        # alertText = driver.find_element_by_css_selector("[class*='alert-success']").text

        assert ("Success" in alertText)

        # To solve the below problem, one solution can be as following
        self.driver.refresh()

    # Adding a seperated data input below in a list
    # If the list consist of multiple tuples of data set input
    # The test will be run as many as the data set input provided
    # e.g: 2 tuples input data set will be run twice
    # Rising problem: since it is run in the same browser, the input field will concat
    # e.g.: TitoRahul and NoviantoShetty


    # @pytest.fixture(params=[{"first_name":"Tito", "last_name":"Novianto", "gender":"Male"}, {"first_name":"Rahul", "last_name":"Shetty", "gender":"Male"}])
    # @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    @pytest.fixture(params=HomePageData.test_homePageData)
    def getData(self, request):
        return request.param
