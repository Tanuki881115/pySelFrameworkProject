from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass
from pageObject.HomePage import HomePage
from pageObject.CheckoutPage import CheckOutPage
from pageObject.ConfirmPage import ConfirmPage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()

        homePage = HomePage(self.driver)

        # Below is removed to homePage.py
        # homePage.shopItems().click()
        # self.driver.find_element_by_css_selector("a[href*='shop']").click()

        # The name of the Object "checkOutPage" below must be the same as the name we return in the HomePage class, shopItems method
        checkOutPage = homePage.shopItems()
        # checkOutPage is moved to homePage.py
        # checkOutPage = CheckOutPage(self.driver)

        log.info("Getting all the card titles")

        cards = checkOutPage.getCardTitles()
        # cards = self.driver.find_elements_by_css_selector(".card-title a")
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                # self.driver.find_elements_by_css_selector(".card-footer button")[i].click()
                checkOutPage.getCardFooter()[i].click()

        checkOutPage.getCheckOutBtn().click()
        # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()


        # Below is removed to checkOutPage.py
        # checkOutPage.checkOutItems().click()
        # self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

        confirmPage = checkOutPage.checkOutItems()
        # checkOutPage is moved to checkOutPage.py
        # confirmPage = ConfirmPage(self.driver)

        log.info("Entering country name as ind")

        confirmPage.getCountry().send_keys("ind")
        # self.driver.find_element_by_id("country").send_keys("ind")

        self.verifyLinkPresence("India")
        # Below is removed to BaseClass.py
        # element = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.LINK_TEXT, "India"))
        # )

        confirmPage.getCountryConfirmed().click()
        # self.driver.find_element_by_link_text("India").click()

        confirmPage.getCheckBox().click()
        # self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

        confirmPage.getSubmitBtn().click()
        # self.driver.find_element_by_css_selector("[type='submit']").click()

        textMatch = confirmPage.getSuccessText().text
        # textMatch = self.driver.find_element_by_css_selector("[class*='alert-success']").text

        log.info("Text received from application is "+textMatch)

        assert ("Success! Thank you!" in textMatch)
