import time
from time import sleep
from settings import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse


#Проверка на соответствие внешнего вида сайтам требованиям заказчика
def test_vision_auth_page(driver):
    driver.get('https://b2c.passport.rt.ru')
    driver.maximize_window()
    time.sleep(10)
    driver.save_screenshot('screenshot_auth_page.png')
#Проверка работы кнопки "ЗАбыли пароль"
def test_forget_password(driver):
    driver.get('https://b2c.passport.rt.ru')

    driver.maximize_window()
    time.sleep(10)
    button_forgot_password = driver.find_element(By.ID, "forgot_password")
    button_forgot_password.click()
    time.sleep(10)
    reset_pass = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')
    assert reset_pass.text == 'Восстановление пароля'
#Проверка работы кнопки "Зарегистрироваться"
def test_register_page(driver):
    driver.get('https://b2c.passport.rt.ru')

    driver.maximize_window()
    time.sleep(10)
    # клик по надписи "Зарегистрироваться"
    button_reg = driver.find_element(By.ID, 'kc-register')
    button_reg.click()
    sleep(5)
    reset_pass = driver.find_element(By.XPATH, '//*[@id="page-right"]/div/div/h1')

    assert reset_pass.text == 'Регистрация'
#Проверки работы кнопок с иконками социальных сетей и перехода по ссылкам для идентификации
def test_auth_from_vk (driver):
    driver.get('https://b2c.passport.rt.ru')

    driver.maximize_window()
    time.sleep(10)
    button_vk = driver.find_element(By.ID, "oidc_vk")
    button_vk.click()
    sleep(3)
    url = urlparse(driver.current_url)
    #print(url.hostname)

    assert url.hostname == 'id.vk.com'

def test_auth_from_ok (driver):
    driver.get('https://b2c.passport.rt.ru')

    driver.maximize_window()
    time.sleep(10)
    button_ok = driver.find_element(By.ID, "oidc_ok")
    button_ok.click()
    sleep(3)
    url = urlparse(driver.current_url)
    #print(url.hostname)

    assert url.hostname == 'connect.ok.ru'

def test_auth_from_mailru (driver):
    driver.get('https://b2c.passport.rt.ru')

    driver.maximize_window()
    time.sleep(10)
    button_mailru = driver.find_element(By.ID, "oidc_mail")
    button_mailru.click()
    sleep(3)
    url = urlparse(driver.current_url)
    #print(url.hostname)

    assert url.hostname == 'connect.mail.ru'

def test_auth_from_yandex (driver):
    driver.get('https://b2c.passport.rt.ru')

    driver.maximize_window()
    time.sleep(5)
    button_yandex = driver.find_element(By.ID, "oidc_ya")
    button_yandex.click()
    sleep(3)
    url = urlparse(driver.current_url)
    print(url.hostname)

    assert url.hostname == 'oauth.yandex.ru'

