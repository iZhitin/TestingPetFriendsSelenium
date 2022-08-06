import time
from selenium import webdriver
# возможность запуска тестов без терминала, нужно использовать драйвер внутри теста
def test_VK():
    email = '...'
    password = '...'

    driver = webdriver.Chrome(r"C:\Users\IvanZ\YandexDisk\IT\python_work\AUTOMATION\toGitHub\TestingPetFriendsSelenium\chromedriver.exe")

    # Open base page:
    driver.get("https://vk.com/")
    driver.maximize_window()  # полный экран
    time.sleep(3)

    # add email
    field_email = driver.find_element_by_xpath('//input[@placeholder="Телефон или почта"]')
    field_email.clear()
    field_email.send_keys(email)
    time.sleep(2)

    # Нажать на кнопку Войти
    driver.find_element_by_xpath('//span[contains(text(), "Войти")]').click()
    time.sleep(2)

    # add password
    field_pass = driver.find_element_by_xpath('//input[@placeholder="Введите пароль"]')
    field_pass.clear()
    field_pass.send_keys(password)
    time.sleep(2)

    # Нажать на кнопку Продолжить
    driver.find_element_by_xpath('//span[contains(text(), "Продолжить")]').click()
    time.sleep(2)
    driver.quit()