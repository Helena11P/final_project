import pytest
import allure
from UI_pages.AuthorizationPage import Authorization
from UI_pages.values import email, expected_url, random_movie_url, nothing_found_text, error_login, error_number
from UI_pages.Search_UI_page import Search

param = pytest.mark.parametrize


@allure.title("Авторизация")
@allure.description("Вводим валидную почту")
@allure.epic("UI тесты")
@allure.story("Авторизация")
@allure.feature("Позитивные тесты")
@allure.severity("blocker")
def test_authorization_possitive(driver):
    auth = Authorization(driver)
    auth.wait_main_page()
    auth.open_authorization()
    auth.enter_login(email)
    auth.click_enter_button()
    auth.wait_page("div.passp-route-forward")
    url = auth.get_current_url()
    with allure.step(f"Проверить, что полученный url начинается с {expected_url}"):
        assert url.startswith(expected_url)


@allure.title("Авторизация c пустым полем Логин")
@allure.epic("UI тесты")
@allure.story("Авторизация")
@allure.feature("Негативные тесты")
@allure.severity("blocker")
def test_authorization_empty_login_negative(driver):
    auth = Authorization(driver)
    auth.wait_main_page()
    auth.open_authorization()
    auth.enter_login("")
    auth.click_enter_button()
    auth.wait_page("div.Textinput-Hint")
    error = auth.error_message()
    with allure.step("Проверить, что текст ошибки такой же, как ожидаемый"):
        assert error == error_login


@allure.title("Авторизация через номер телефона")
@allure.description("Вводим невалидные номера телефонов")
@allure.epic("UI тесты")
@allure.story("Авторизация")
@allure.feature("Негативные тесты")
@allure.severity("blocker")
@param("phone_number", [
    ("+71111111111"),
    ("+7 (912) 345-67-890123"),
    ("+7 (912) 345-67-8")
])
def test_authorization_phone_negative(driver, phone_number):
    auth = Authorization(driver)
    auth.wait_main_page()
    auth.open_authorization()
    auth.click_phone_button()
    auth.enter_phone_number(phone_number)
    auth.click_enter_button()
    auth.wait_page("div.Textinput-Hint")
    error = auth.error_message()
    with allure.step("Проверить, что текст ошибки такой же, как ожидаемый"):
        assert error == error_number


@allure.title("Поиск фильма по названию")
@allure.description("Вводим валидные данные")
@allure.epic("UI тесты")
@allure.story("Поиск")
@allure.feature("Позитивные тесты")
@allure.severity("blocker")
@param("name", [
    ("Хоббит"),
    ("преступление и наказание"),
    ("1+1"),
    ("И снова здравствуйте!")
])
def test_search_possitive(driver, name):
    search = Search(driver)
    search.wait_main_page()
    search.input_name(name)
    search.click_search_button()
    search.wait_result("div.search_results")
    title = search.search_result()
    with allure.step("Сравнить название фильма с полученным"):
        assert name.lower() in title.lower()


@allure.title("Открывает страницу со случайным фильмом")
@allure.epic("UI тесты")
@allure.story("Поиск")
@allure.feature("Позитивные тесты")
@allure.severity("critical")
def test_empty_search_possitive(driver):
    search = Search(driver)
    search.wait_main_page()
    search.click_search_button()
    url = search.get_current_url()
    with allure.step("Сравнить url текущей страницы с ожидаемым"):
        assert url == random_movie_url


@allure.title("Поиск фильма по невалидному названию")
@allure.epic("UI тесты")
@allure.story("Поиск")
@allure.feature("Негативные тесты")
@allure.severity("critical")
@param("name", [
    ("!!!!%"),
    ("синхрофазатрон")
])
def test_search_negative(driver, name):
    search = Search(driver)
    search.wait_main_page()
    search.input_name(name)
    search.click_search_button()
    result = search.nothing_found()
    with allure.step("Проверить, что результат(сообщение об ошибке) совпадает ожидаемым"):
        assert result == nothing_found_text


@allure.title("Открывает список с подсказками")
@allure.epic("UI тесты")
@allure.story("Поиск")
@allure.feature("Позитивные тесты")
@allure.severity("critical")
def test_tips_list(driver):
    search = Search(driver)
    name = "наруто"
    search.wait_main_page()
    search.input_name(name)
    search.wait_result("div[data-tid=e4233b06]")
    result = search.search_tips_list()
    with allure.step("Сравнить название фильма с полученным в списке подсказок"):
        assert name.lower() in result.lower()
