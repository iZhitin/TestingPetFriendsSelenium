# для округления
import math

# импортируем функционал теста авторизации из соседнего файла
from main_functionalities import test_auth

# импортируем объекты для явного ожидания
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# запуск тестов через терминал при помощи команды
# pytest -v --driver Chrome --driver-path chromedriver.exe tests/testing_my_pets.py
# для запуска конкретного теста:
# pytest -v --driver Chrome --driver-path chromedriver.exe tests/testing_my_pets::test_presence_of_all_my_pets
# или pytest -v --driver Chrome --driver-path chromedriver.exe tests/testing_my_pets.py::test_presence_of_all_my_pets
# web_browser = selenium, так это указано conftest.py


# тестирование присутствия всех добавленных животных в соответствии с указанным числом
def test_presence_of_all_my_pets(web_browser):
    # авторизация
    test_auth(web_browser)

    # открываем вкладку мои животные
    # my_pets = web_browser.find_element_by_xpath('//*[@href=\"/my_pets\"]')
    # применим явное ожидание (ожидание по присутствию элемента)
    my_pets = WebDriverWait(web_browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@href=\"/my_pets\"]')))
    my_pets.click()


    # получаем список с количеством строк (блоков), где содержится информация о конкретном животном
    list_of_pets = web_browser.find_elements_by_xpath('//tbody/tr')

    # получаем текст, содержащий количество животных в левой панели
    left_board = web_browser.find_element_by_xpath('//div[@class=".col-sm-4 left"]')
    parts = left_board.text

    # ожидаем, что цифра с количеством животных в левой панели совпадает с количеством строк (блоков) с животными
    assert str(len(list_of_pets)) in parts, "Количество блоков с животными не равно их количеству из панели"


# проверка, что хотя бы половина питомцев имеют фото
def test_presence_of_photo(web_browser):
    # авторизация
    test_auth(web_browser)

    # открываем вкладку мои животные
    my_pets = web_browser.find_element_by_xpath('//*[@href=\"/my_pets\"]')
    my_pets.click()

    # получаем список с количеством строк (блоков), где содержится информация о конкретном животном
    list_of_pets = web_browser.find_elements_by_xpath('//tbody/tr')

    # обращаемся к тегам, которые должны содержать фото животных
    images = web_browser.find_elements_by_xpath('//th/img[@src]')

    # получаем количество питомцев, у которых нет фото
    count = 0
    for i in range(len(images)):
        # если значение атрибута 'src' пустое, то прибавляем единицу к счетчику
        if images[i].get_attribute('src') != '':
            count += 1

    # ожидаем, что хотя бы половина питомцев имеют фото
    # если количество животных - нечетно, то округляем в большую сторону
    # так как, если округлять в меньшую сторону,
    # то половина от округленного числа будет меньше половины от неокругленного
    assert math.ceil(((len(list_of_pets))/2)) == count or math.ceil(((len(list_of_pets))/2)) < count, "Error"
    # return str(len(list_of_pets)), str(count)


# проверка, что все животные имеют имя, тип и возраст
def test_all_pets_have_data(web_browser):
    # авторизация
    test_auth(web_browser)

    # открываем вкладку мои животные
    my_pets = web_browser.find_element_by_xpath('//*[@href=\"/my_pets\"]')
    my_pets.click()

    # получаем 3 списка с именем, типом и возрастом каждого животного
    names = web_browser.find_elements_by_xpath('//tr/th/following-sibling::td[1]')
    types = web_browser.find_elements_by_xpath('//tr/th/following-sibling::td[2]')
    ages = web_browser.find_elements_by_xpath('//tr/th/following-sibling::td[3]')

    for i in range(len(names)): # длины списков names, types и ages должны быть одинаковыми

        # проверяем, что длина каждого имени больше 0; т.е. имя имеет какое-то значение
        assert len(names[i]) > 0, f"Найдено животное без имени с индексом: {i}"

        # проверяем, что длина каждого типа больше 0; т.е. тип имеет какое-то значение
        assert len(types[i]) > 0,  f"Найдено животное без типа с индексом: {i}"

        # проверяем, что длина возраста больше 0; т.е. возраст имеет какое-то значение
        assert len(ages[i]) > 0,  f"Найдено животное без возраста с индексом: {i}"


# проверка, что все животные имеют уникальные имена
def test_all_pets_have_different_names(web_browser):
    # авторизация
    test_auth(web_browser)

    # открываем вкладку мои животные
    my_pets = web_browser.find_element_by_xpath('//*[@href=\"/my_pets\"]')
    my_pets.click()

    # получаем список с именами животных
    names = web_browser.find_elements_by_xpath('//tr/th/following-sibling::td[1]')

    # проверяем, что длина списка с уникальными именами соответствует длине списка со всеми именами
    assert len(list(set(names))) == len(names), "Есть животные с повторяющимися именами"


# проверка отсутствия животных с одинаковыми данными (фото не в счет)
def test_all_pets_are_unique(web_browser):
    # авторизация
    test_auth(web_browser)

    # открываем вкладку мои животные
    my_pets = web_browser.find_element_by_xpath('//*[@href=\"/my_pets\"]')
    my_pets.click()

    # получаем 3 списка с именем, типом и возрастом каждого животного
    names = web_browser.find_elements_by_xpath('//tr/th/following-sibling::td[1]')
    types = web_browser.find_elements_by_xpath('//tr/th/following-sibling::td[2]')
    ages = web_browser.find_elements_by_xpath('//tr/th/following-sibling::td[3]')

    # создаем пустые списки
    parts = []
    pets_info = []

    for i in range(len(names)): # длины списков names, types и ages должны быть одинаковыми
        # проверка на то, что каждый элемент содержит какое-то значение была в test_all_pets_have_data
        # поэтому следующие проверки не требуются:
        # assert names[i].text != ''
        # assert types[i].text != ''
        # assert ages[i].text != ''

        # в список parts добавляем последовательно имя, тип и возраст
        parts.append(names[i].text)
        parts.append(types[i].text)
        parts.append(ages[i].text)

        # получившийся список добавляем в основной список в качестве одного элемента и так на каждой итерации
        pets_info.append(parts)

    # проверяем, что ничего не потерялось
    assert len(pets_info) == len(names), "Что-то потерялось"

    # так как к спискам внутри списка нельзя применить set(),
    # поэтому сравним каждый элемент с каждым в основном списке,
    # тем самым проверим уникальность животных
    # установим метку со значением True
    flag = True
    for i in range(len(pets_info)):
        for j in range(len(pets_info)):
            # если индекс элемента не равен самому себе...
            if i != j:
                # ...сравним элементы с разными индексами
                if pets_info[i] == pets_info[j]:
                    # метка получает значение False, если найдены не уникальные элементы
                    flag = False

    assert flag, "Есть повторяющиеся животные"