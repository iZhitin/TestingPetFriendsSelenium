import pytest
from selenium import webdriver

# в данном случае pytest.driver эквивалентно pytest_driver
@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome(r"C:\Users\IvanZ\YandexDisk\IT\python_work\AUTOMATION\toGitHub\TestingPetFriendsSelenium\chromedriver.exe")
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('vasya@mail.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('12345')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

def test_check_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('vasya@mail.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('12345')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')

   for i in range(len(names)):
      # assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      # проверяем наличие запятой между типом и возрастом
      assert ', ' in descriptions[i]
      # создаем список по запятой из двух элементов
      parts = descriptions[i].text.split(", ")
      # проверяем, что длина типа больше 0
      assert len(parts[0]) > 0
      # проверяем, что длина возраста больше 0
      assert len(parts[1]) > 0