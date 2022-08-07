# для пауз, в образовательных целях
import time

# для генерации случайных регистрационных данных
from faker import Faker
fake = Faker()


# запуск тестов через терминал при помощи команды
# pytest -v --driver Chrome --driver-path chromedriver.exe tests/main_functionalities.py
# для запуска конкретного теста:
# # pytest -v --driver Chrome --driver-path chromedriver.exe tests/main_functionalities::test_reg


class RegisterUser:
    @staticmethod
    def random():  # функция генерирует каждый раз валидные данные
        name = fake.name()
        email = fake.email()
        password = fake.password()
        return name, email, password


# web_browser = selenium, так как это указано в conftest.py

# тестирование регистрации
def test_reg(web_browser):
    # создаем случайные регистрационные данные
    name, email, password = RegisterUser.random()

    # заходим на сайт и нажимаем кнопку регистрации
    web_browser.get('https://petfriends.skillfactory.ru')
    button_nu = web_browser.find_element_by_xpath('//*[text()="Зарегистрироваться"]')
    button_nu.click()
    time.sleep(1)

    # вводим имя
    r_name = web_browser.find_element_by_id('name')
    r_name.clear()
    r_name.send_keys(name)

    # вводим эл.почту
    r_email = web_browser.find_element_by_id('email')
    r_email.clear()
    r_email.send_keys(email)

    # вводим пароль
    r_password = web_browser.find_element_by_id('pass')
    r_password.clear()
    r_password.send_keys(password)

    # посмотрим на данные
    time.sleep(2)

    # нажимаем кнопку зарегистрироваться
    button_reg = web_browser.find_element_by_xpath('//*[text()="Зарегистрироваться"]')
    button_reg.click()

    # посмотрим на результат
    time.sleep(2)

    # проверяем стала ли доступна главная страница после регистрации
    assert web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets', "login error"


# тестирование авторизации
def test_auth(web_browser):
    # добираемся до страницы авторизации
    web_browser.get('https://petfriends.skillfactory.ru')
    button_nu = web_browser.find_element_by_xpath('//*[text()="Зарегистрироваться"]')
    button_nu.click()
    time.sleep(1)
    button_ou = web_browser.find_element_by_xpath('//*[text()="У меня уже есть аккаунт"]')
    button_ou.click()
    time.sleep(2)

    # вводим логин
    email = web_browser.find_element_by_id('email')
    email.clear()
    email.send_keys('p@p.p')
    time.sleep(1)

    # вводим пароль
    password = web_browser.find_element_by_id('pass')
    password.clear()
    password.send_keys('122333')
    time.sleep(2)

    # нажимаем кнопку войти
    button_entrance = web_browser.find_element_by_xpath('//*[text()="Войти"]')
    button_entrance.click()
    time.sleep(2)

    # проверяем стала ли доступна главная страница после авторизации
    assert web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets', "login error"


# тестирования добавления животного с фото
def test_create_pet_with_photo(web_browser):
    # авторизация
    test_auth(web_browser)
    time.sleep(2)

    # открываем вкладку мои животные
    my_pets = web_browser.find_element_by_xpath('//*[@href=\"/my_pets\"]')
    my_pets.click()
    time.sleep(2)

    # нажимаем кнопку добавить питомца
    my_pet = web_browser.find_element_by_xpath('//*[text()="Добавить питомца"]')
    my_pet.click()
    time.sleep(2)

    # загружаем фото
    add_photo = web_browser.find_element_by_xpath('//input[@type="file"]')
    add_photo.send_keys(r"C:\Users\IvanZ\YandexDisk\IT\python_work\AUTOMATION\toGitHub\TestingPetFriendsSelenium\tests\images\P1040103.jpg")

    # возьмем случайное имя
    p_name, _, _ = RegisterUser.random()

    # ввод имени
    pet_name = web_browser.find_element_by_id('name')
    pet_name.clear()
    pet_name.send_keys(p_name)

    # ввод типа
    pet_type = web_browser.find_element_by_id('animal_type')
    pet_type.clear()
    pet_type.send_keys('пес')

    # ввод возраста
    pet_age = web_browser.find_element_by_id('age')
    pet_age.clear()
    pet_age.send_keys('2')
    time.sleep(2)

    # нажимаем кнопку добавить
    add_button = web_browser.find_element_by_xpath('//*[@onclick="add_pet();"]')
    add_button.click()
    time.sleep(2)

    # проверяем есть ли на главной странице созданный питомец по случайно сгенерированному имени
    web_browser.get('https://petfriends.skillfactory.ru/all_pets')
    assert web_browser.find_element_by_xpath(f'//*[text()="{p_name}"]')


# тестирования добавления животного без фото
def test_create_pet_without_photo(web_browser):
    # авторизация
    test_auth(web_browser)
    time.sleep(2)

    # открываем вкладку мои животные
    my_pets = web_browser.find_element_by_xpath('//*[@href=\"/my_pets\"]')
    my_pets.click()
    time.sleep(2)

    # нажимаем кнопку добавить питомца
    my_pet = web_browser.find_element_by_xpath('//*[text()="Добавить питомца"]')
    my_pet.click()
    time.sleep(2)

    # возьмем случайное имя
    p_name, _, _ = RegisterUser.random()

    # ввод имени
    pet_name = web_browser.find_element_by_id('name')
    pet_name.clear()
    pet_name.send_keys(p_name)

    # ввод типа
    pet_type = web_browser.find_element_by_id('animal_type')
    pet_type.clear()
    pet_type.send_keys('пес')

    # ввод возраста
    pet_age = web_browser.find_element_by_id('age')
    pet_age.clear()
    pet_age.send_keys('2')
    time.sleep(2)

    # нажимаем кнопку добавить
    add_button = web_browser.find_element_by_xpath('//*[@onclick="add_pet();"]')
    add_button.click()
    time.sleep(2)

    # проверяем есть ли на главной странице созданный питомец по случайно сгенерированному имени
    web_browser.get('https://petfriends.skillfactory.ru/all_pets')
    assert web_browser.find_element_by_xpath(f'//*[text()="{p_name}"]')


# тестирования удаления животного
def test_delete_pet(web_browser):
    # авторизация
    test_auth(web_browser)
    time.sleep(2)

    # открываем вкладку мои животные
    my_pets = web_browser.find_element_by_xpath('//*[@href=\"/my_pets\"]')
    my_pets.click()
    time.sleep(2)

    # удаление самого верхнего
    delete_last_pet = web_browser.find_element_by_xpath('//a[@title="Удалить питомца"]')
    delete_last_pet.click()
    time.sleep(5)

    # # удаление самого нижнего (количество питомцев = номер последнего питомца)
    # delete_last_pet = web_browser.find_element_by_xpath('(//a[@title="Удалить питомца"])[1295]')
    # delete_last_pet.click()
    # time.sleep(5)

    # попытки проскроллить до элемента
    # web_browser.execute_script("arguments[0].scrollIntoView();", delete_last_pet)
    # delete_last_pet.scroll_to_element(web_browser.find_element_by_xpath('(//a[@title="Удалить питомца"])[1295]'))


# попытки сохранить  cookie
# save cookies of the browser after the login
# with open('my_cookies.txt', 'wb') as cookies:
#     pickle.dump(web_browser.get_cookies(), cookies)
