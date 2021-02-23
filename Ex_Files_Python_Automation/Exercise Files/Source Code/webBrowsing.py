from selenium import webdriver  # use webdriver package

driver = webdriver.Chrome()  # declare driver variable as certain driver.
driver.get(
    "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
)  # find webpage to automate
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')  #
messageField.send_keys("Hello World")
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()
additionField1 = driver.find_element_by_xpath("")
additionField1.send_keys("10")
additionField2 = driver.find_element_by_xpath("")
additionField2.send_keys("11")
