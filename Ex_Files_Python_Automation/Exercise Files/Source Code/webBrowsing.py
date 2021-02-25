from selenium import webdriver  # use webdriver package

driver = webdriver.Chrome()  # declare driver variable as certain driver.
driver.get(
    "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
)  # find webpage to automate
messageField = driver.find_element_by_xpath(
    '//*[@id="user-message"]'
)  # find html element path
messageField.send_keys("Hello World")  # input message through keys
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
showMessageButton.click()
additionField1 = driver.find_element_by_xpath('//*[@id="sum1"]')
additionField1.send_keys("10")
additionField2 = driver.find_element_by_xpath('//*[@id="sum2"]')
additionField2.send_keys("11")
getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
getTotalButton.click()  # automate click method
