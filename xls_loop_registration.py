# - *- coding: utf- 8 - *-
import xlrd
import os
import time
import unittest
from selenium import webdriver


class RegistrationTest (unittest.TestCase):
    def setUp(self):
        self.book = xlrd.open_workbook("register_test_data.xls")
        driver_path = os.path.dirname(os.path.abspath(__file__)) + "/chromedriver"  # if you want run tests on Chrome
        self.driver = webdriver.Chrome(driver_path)  # if you want run tests on Chrome
        # self.driver = webdriver.Firefox() # if you want to run tests on FF
        self.driver.set_page_load_timeout(10)
        self.driver.get('http://valletta.dro.nask.pl:8001/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.book_sheet = self.book.sheet_by_index(0)

    def preparation(self):

        self.driver.find_element_by_link_text("Zaloguj").click()

        time.sleep(2)
        register_button = self.driver.find_element_by_xpath(
            "//md-dialog[@id='dialogContent_6']/div/md-content/div/form/button[2]")
        register_button.click()

    def test_correct_registration_data(self):

        for i in range(self.book_sheet.nrows):

            self.preparation()

            login = self.book_sheet.cell(i, 1)

            username = self.driver.find_element_by_name("username")
            username.clear()
            username.send_keys(login.value)

            email = self.book_sheet.cell(i, 2)

            email_field = self.driver.find_element_by_name("email")
            email_field.clear()
            email_field.send_keys(email.value)
            repeat_email_field = self.driver.find_element_by_name("emailrepeat")
            repeat_email_field.clear()
            repeat_email_field.send_keys(email.value)

            password = self.book_sheet.cell(1, 4)

            password_field = self.driver.find_element_by_name("password")
            password_field.clear()
            password_field.send_keys(password.value)
            password_repeat_field = self.driver.find_element_by_name("password_repeat")
            password_repeat_field.clear()
            password_repeat_field.send_keys(password.value)

            register = self.driver.find_element_by_css_selector("form[name=\"RegisterForm\"] > button.btn")
            register.click()

            time.sleep(2)

            element = self.driver.find_element_by_css_selector("div.ng-scope > button.btn")
            self.assertTrue(element.is_displayed())
            element.click()
            time.sleep(2)

    def test_already_used_user_name(self):

        self.preparation()

        login = self.book_sheet.cell(0, 1)

        username = self.driver.find_element_by_name("username")
        username.clear()
        username.send_keys(login.value)

        email = "random2@emali.com"

        email_field = self.driver.find_element_by_name("email")
        email_field.clear()
        email_field.send_keys(email)
        repeat_email_field = self.driver.find_element_by_name("emailrepeat")
        repeat_email_field.clear()
        repeat_email_field.send_keys(email)

        password = self.book_sheet.cell(1, 4)

        password_field = self.driver.find_element_by_name("password")
        password_field.clear()
        password_field.send_keys(password.value)
        password_repeat_field = self.driver.find_element_by_name("password_repeat")
        password_repeat_field.clear()
        password_repeat_field.send_keys(password.value)

        register = self.driver.find_element_by_css_selector("form[name=\"RegisterForm\"] > button.btn")
        register.click()

        time.sleep(2)

        message = self.driver.find_element_by_class_name("ng-scope")
        self.assertIn(u"Podana nazwa użytkownika jest już zajęta.", message.text)

    def test_already_used_email(self):

        self.preparation()

        login = "some_user_name_2"

        username = self.driver.find_element_by_name("username")
        username.clear()
        username.send_keys(login)

        email = self.book_sheet.cell(1, 2)

        email_field = self.driver.find_element_by_name("email")
        email_field.clear()
        email_field.send_keys(email.value)
        repeat_email_field = self.driver.find_element_by_name("emailrepeat")
        repeat_email_field.clear()
        repeat_email_field.send_keys(email.value)

        password = self.book_sheet.cell(1, 4)

        password_field = self.driver.find_element_by_name("password")
        password_field.clear()
        password_field.send_keys(password.value)
        password_repeat_field = self.driver.find_element_by_name("password_repeat")
        password_repeat_field.clear()
        password_repeat_field.send_keys(password.value)

        register = self.driver.find_element_by_css_selector("form[name=\"RegisterForm\"] > button.btn")
        register.click()

        time.sleep(2)

        message = self.driver.find_element_by_class_name("ng-scope")
        self.assertIn(u"Z tym emailem jest już powiązane konto.", message.text)

    def test_different_emails(self):

        self.preparation()

        email = "some@email.com"

        email_field = self.driver.find_element_by_name("email")
        email_field.clear()
        email_field.send_keys(email)

        repeat_email = "diffrent@email.com"

        repeat_email_field = self.driver.find_element_by_name("emailrepeat")
        repeat_email_field.clear()
        repeat_email_field.send_keys(repeat_email)

        register = self.driver.find_element_by_css_selector("form[name=\"RegisterForm\"] > button.btn")
        register.click()

        message = self.driver.find_element_by_class_name("ng-scope")
        self.assertIn(u"Wprowadzone adresy różnią się od siebie", message.text)

    def test_different_passwords(self):

        self.preparation()

        password = "SomePassword1"

        password_field = self.driver.find_element_by_name("password")
        password_field.clear()
        password_field.send_keys(password)

        password_repeat = "DifferentPassword1"

        password_repeat_field = self.driver.find_element_by_name("password_repeat")
        password_repeat_field.clear()
        password_repeat_field.send_keys(password_repeat)

        register = self.driver.find_element_by_css_selector("form[name=\"RegisterForm\"] > button.btn")
        register.click()

        message = self.driver.find_element_by_class_name("ng-scope")
        self.assertIn(u"Hasła różnią się od siebie.", message.text)

    def test_correct_birth_date(self):

        birth_date = ['1800', '1985', '2017']

        for birth_date in birth_date:

            self.preparation()

            time.sleep(1)

            birth_date_field = self.driver.find_element_by_name("birthYear")

            birth_date_field.clear()
            birth_date_field.send_keys(birth_date)

            register = self.driver.find_element_by_css_selector("form[name=\"RegisterForm\"] > button.btn")
            register.click()

            message = self.driver.find_element_by_class_name("ng-scope")
            self.assertNotIn(u"Rok urodzenia musi składać się z 4 cyfr.", message.text)
            self.assertNotIn(u"Nieprawidłowy rok urodzenia", message.text)

            self.driver.find_element_by_css_selector("md-icon").click()

            time.sleep(2)

    def test_incorrect_birth_date(self):

        birth_date = ['1799', '2018', '3900']

        for birth_date in birth_date:

            self.preparation()

            time.sleep(1)

            birth_date_field = self.driver.find_element_by_name("birthYear")

            birth_date_field.clear()
            birth_date_field.send_keys(birth_date)

            register = self.driver.find_element_by_css_selector("form[name=\"RegisterForm\"] > button.btn")
            register.click()

            message = self.driver.find_element_by_class_name("ng-scope")
            self.assertIn(u"Nieprawidłowy rok urodzenia", message.text)

            self.driver.find_element_by_css_selector("md-icon").click()

            time.sleep(2)

        birth_date = ['1', '22', '390', 'aa', 'a11', '!@@#', ')ii2', ' 1975']

        for birth_date in birth_date:

            self.preparation()

            time.sleep(1)

            birth_date_field = self.driver.find_element_by_name("birthYear")

            birth_date_field.clear()
            birth_date_field.send_keys(birth_date)

            register = self.driver.find_element_by_css_selector("form[name=\"RegisterForm\"] > button.btn")
            register.click()

            message = self.driver.find_element_by_class_name("ng-scope")
            self.assertIn(u"Rok urodzenia musi składać się z 4 cyfr.", message.text)

            self.driver.find_element_by_css_selector("md-icon").click()

            time.sleep(2)

    def tearDown(self):
        self.driver.close()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(RegistrationTest("test_correct_registration_data"))
    suite.addTest(RegistrationTest("test_already_used_user_name"))
    suite.addTest(RegistrationTest("test_already_used_email"))
    suite.addTest(RegistrationTest("test_different_emails"))
    suite.addTest(RegistrationTest("test_different_passwords"))
    suite.addTest(RegistrationTest("test_correct_birth_date"))
    suite.addTest(RegistrationTest("test_incorrect_birth_date"))
    return suite

if __name__ == '__main__':
    unittest.main(verbosity=3, defaultTest="suite")


