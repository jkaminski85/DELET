import xlrd
import time
import unittest
from selenium import webdriver


class RegistrationTest (unittest.TestCase):
    def setUp(self):
        self.book = xlrd.open_workbook("register_test_data.xls")
        self.driver = webdriver.Chrome('/home/janusz/Pobrane/chromedriver')
        self.driver.set_page_load_timeout(10)
        self.driver.get('http://valletta.dro.nask.pl:8001/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_correct_registration_data(self):

        book_sheet = self.book.sheet_by_index(0)

        for i in range(book_sheet.nrows):

            self.preparation()

            login = book_sheet.cell(i, 1)

            username = self.driver.find_element_by_name("username")
            username.clear()
            username.send_keys(login.value)

            email = book_sheet.cell(i, 2)

            email_field = self.driver.find_element_by_name("email")
            email_field.clear()
            email_field.send_keys(email.value)
            repeat_email_field = self.driver.find_element_by_name("emailrepeat")
            repeat_email_field.clear()
            repeat_email_field.send_keys(email.value)

            password = book_sheet.cell(1, 4)

            password_field = self.driver.find_element_by_name("password")
            password_field.clear()
            password_field.send_keys(password.value)
            password_repeat_field = self.driver.find_element_by_name("password_repeat")
            password_repeat_field.clear()
            password_repeat_field.send_keys(password.value)

            date_of_birth = book_sheet.cell(i, 3)

            birth_field = self.driver.find_element_by_id("input_14")
            birth_field.clear()
            birth_field.send_keys(date_of_birth.value)

            register = self.driver.find_element_by_css_selector("form[name=\"RegisterForm\"] > button.btn")
            register.click()

            time.sleep(2)

            element = self.driver.find_element_by_css_selector("div.ng-scope > button.btn")
            self.assertTrue(element.is_displayed())
            print (element.is_displayed())
            element.click()
            time.sleep(2)

    def test_already_used_user_name(self):

        book_sheet = self.book.sheet_by_index(1)

        self.preparation()

        login = book_sheet.cell(1, 1)

        username = self.driver.find_element_by_name("username")
        username.clear()
        username.send_keys(login.value)

        email = book_sheet.cell(1, 2)

        email_field = self.driver.find_element_by_name("email")
        email_field.clear()
        email_field.send_keys(email.value)
        repeat_email_field = self.driver.find_element_by_name("emailrepeat")
        repeat_email_field.clear()
        repeat_email_field.send_keys(email.value)

        password = book_sheet.cell(1, 4)

        password_field = self.driver.find_element_by_name("password")
        password_field.clear()
        password_field.send_keys(password.value)
        password_repeat_field = self.driver.find_element_by_name("password_repeat")
        password_repeat_field.clear()
        password_repeat_field.send_keys(password.value)

        register = self.driver.find_element_by_css_selector("form[name=\"RegisterForm\"] > button.btn")
        register.click()

        message = self.driver.find_element_by_css_selector("ng-binding ng-scope")
        self.assertIn(_("Podana nazwa użytkownika jest już zajęta."), message.text)


    def preparation(self):

        self.driver.find_element_by_link_text("Zaloguj").click()

        time.sleep(2)
        register_button = self.driver.find_element_by_xpath(
            "//md-dialog[@id='dialogContent_6']/div/md-content/div/form/button[2]")
        register_button.click()









    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)


