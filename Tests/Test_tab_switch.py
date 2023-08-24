from selenium.webdriver.common.by import By
from settings import phone, email, login
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time

def test_switch_tabs(driver):
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    password_field = driver.find_element(By.ID, "password")
    login_field = driver.find_element(By.ID, "username")
    phone_tab = driver.find_element(By.ID, "t-btn-tab-phone")
    mail_tab = driver.find_element(By.ID, "t-btn-tab-mail")
    login_tab = driver.find_element(By.ID, "t-btn-tab-login")


    login_field.send_keys(phone)
    time.sleep(3)
    assert "rt-tab--active" in phone_tab.get_attribute("class")
    assert "rt-tab--active" not in mail_tab.get_attribute("class")
    assert "rt-tab--active" not in login_tab.get_attribute("class")


    for _ in range(22):
        login_field.send_keys(Keys.BACK_SPACE)
    login_field.send_keys(email)
    password_field.click()
    time.sleep(3)
    assert "rt-tab--active" in mail_tab.get_attribute("class")
    assert "rt-tab--active" not in phone_tab.get_attribute("class")
    assert "rt-tab--active" not in login_tab.get_attribute("class")


    for _ in range(22):
        login_field.send_keys(Keys.BACK_SPACE)
    login_field.send_keys(login)
    password_field.click()
    time.sleep(3)
    assert "rt-tab--active" in login_tab.get_attribute("class")
    assert "rt-tab--active" not in phone_tab.get_attribute("class")
    assert "rt-tab--active" not in mail_tab.get_attribute("class")
