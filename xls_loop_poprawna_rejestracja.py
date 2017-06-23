import xlrd
import time
from selenium import webdriver

book = xlrd.open_workbook("correct_register_test_data.xls")

driver = webdriver.Chrome('/home/janusz/Pobrane/chromedriver')
driver.set_page_load_timeout(10)
driver.get('http://valletta.dro.nask.pl:8001/')
driver.maximize_window()
driver.implicitly_wait(10)

for i in range(book.sheet_by_index(0).nrows):

    driver.find_element_by_link_text("Zaloguj").click()

    time.sleep(2)

    driver.find_element_by_xpath("//md-dialog[@id='dialogContent_6']/div/md-content/div/form/button[2]").click()

    login = book.sheet_by_index(0).cell(i, 1)

    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(login.value)

    email = book.sheet_by_index(0).cell(i, 2)

    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys(email.value)

    driver.find_element_by_name("emailrepeat").clear()
    driver.find_element_by_name("emailrepeat").send_keys(email.value)

    password = book.sheet_by_index(0).cell(1, 4)

    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password.value)

    driver.find_element_by_name("password_repeat").clear()
    driver.find_element_by_name("password_repeat").send_keys(password.value)

    register = driver.find_element_by_css_selector("form[name=\"RegisterForm\"] > button.btn")
    register.click()

    time.sleep(2)

    element = driver.find_element_by_css_selector("div.ng-scope > button.btn")

    print (element.is_displayed())

    element.click()

    time.sleep(2)


driver.close()


