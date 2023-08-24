from selenium.webdriver.common.by import By
from settings import login, invalid_login, password, invalid_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Позитивный случай
def test_auth_valid_login(driver):
    login_field = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    driver.find_element(By.ID, "t-btn-tab-login").click()

    password_field = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.NAME, "login")

    login_field.send_keys(login)
    password_field.send_keys(password)
    submit_button.submit()
    user_lc_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[@class='user-name user-info__name']"))
    )

    assert "b2c.passport.rt.ru/account_b2c/" in driver.current_url
    assert user_lc_name.is_displayed()

#Негативные сценарии
def test_auth_invalid_login(driver):
    login_field = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    driver.find_element(By.ID, "t-btn-tab-login").click()

    password_field = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.NAME, "login")

    login_field.send_keys(invalid_login)
    password_field.send_keys(password)
    submit_button.submit()

    invalid_credentials = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-error='Неверный логин или пароль']"))
    )
    assert invalid_credentials.is_displayed()
    forgot_password = driver.find_element(By.ID, "forgot_password")
    assert "rt-link--muted" not in forgot_password.get_attribute("class")


def test_auth_invalid_password(driver):
    login_field = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    driver.find_element(By.ID, "t-btn-tab-login").click()

    password_field = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.NAME, "login")

    login_field.send_keys(login)
    password_field.send_keys(invalid_password)
    submit_button.submit()

    invalid_credentials = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-error='Неверный логин или пароль']"))
    )
    assert invalid_credentials.is_displayed()
    forgot_password = driver.find_element(By.ID, "forgot_password")
    assert "rt-link--muted" not in forgot_password.get_attribute("class")


def test_auth_invalid_login_and_password(driver):
    login_field = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.ID, "username"))
    )
    driver.find_element(By.ID, "t-btn-tab-login").click()

    password_field = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.NAME, "login")

    login_field.send_keys(invalid_login)
    password_field.send_keys(invalid_password)
    submit_button.submit()

    invalid_credentials = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@data-error='Неверный логин или пароль']"))
    )
    assert invalid_credentials.is_displayed()
    forgot_password = driver.find_element(By.ID, "forgot_password")
    assert "rt-link--muted" not in forgot_password.get_attribute("class")

