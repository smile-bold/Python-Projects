from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import (
    expected_conditions as EC,
)  # The needed python libraries to use wait functions.

# tells function to wait until a part of the website is developed.
# Explicit wait functions use conditions while implicit wait functions pull the data for a certain amount of time.
# code wont run because of formatting; fix later.
url = "https://www.google.com/earth/"
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 10)
launchEarthButton = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span")
    )
)
launchEarthButton.click()
