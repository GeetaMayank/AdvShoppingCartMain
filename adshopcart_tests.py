import unittest
import adshopcart_methods as methods
import adshopcart_locators as locators


class AdvantageShoppingCartAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_main_advantage_shopping():
        methods.setUp()
        methods.signUp()
        methods.check_my_account_my_orders()
        methods.log_out()
        methods.log_in(locators.new_username, locators.new_password)
        methods.delete_account()
        methods.login_with_incorrect_username()
        methods.check_homepage()
        methods.contact_us_form()
        methods.tearDown()
