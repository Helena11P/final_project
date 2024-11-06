import allure
from API.Search_API_page import Search
from API.values_api import my_id, id_error_message
from conftest import param


@allure.title("Поиск фильма по id")
@allure.description("Вводим валидный id")
@allure.epic("API тесты")
@allure.story("Поиск")
@allure.feature("Позитивные тесты")
@allure.severity("blocker")
def test_search_by_id_possitive(api: Search):
    new_id = api.search_by_id(my_id)["id"]
    with allure.step("Сравить введенный id с полученным"):
        assert new_id == my_id


@allure.title("Поиск фильма по названию")
@allure.description("Вводим валидные данные на кириллице")
@allure.epic("API тесты")
@allure.story("Поиск")
@allure.feature("Позитивные тесты")
@allure.severity("blocker")
@param("my_name", [
    ("Дракула"),
    ("преступление и наказание"),
    ("1+1"),
    ("И снова здравствуйте!")
    ]
)
def test_search_by_name_possitive(api: Search, my_name):
    new_name = api.search_by_name(my_name)[0]["name"]
    with allure.step("Сравить введенное название фильма с полученным"):
        assert new_name.lower() == my_name.lower()


@allure.title("Поиск фильма по названию на английском")
@allure.description("Вводим валидные данные на латинице")
@allure.epic("API тесты")
@allure.story("Поиск")
@allure.feature("Позитивные тесты")
@allure.severity("blocker")
@param("my_english_name", [
    ("Drive"),
    ("catch me if you can"),
    ("Schitt$ Creek")
    ]
)
def test_search_by_alternative_name_possitive(api: Search, my_english_name):
    new_name = api.search_by_name(my_english_name)[0]["alternativeName"]
    with allure.step("Сравить введенное название фильма с полученным"):
        assert new_name.lower() == my_english_name.lower()


@allure.title("Поиск случайного фильма")
@allure.epic("API тесты")
@allure.story("Поиск")
@allure.feature("Позитивные тесты")
@allure.severity("critical")
def test_random_film_possitive(api: Search):
    random_film = api.random_movie()
    with allure.step("Получить id"):
        random_film_id = random_film["id"]
    with allure.step("Получить название"):
        random_film_name = random_film["name"]
    with allure.step("Проверить, что у фильма есть id"):
        assert int(random_film_id) > 0
    with allure.step("Проверить, что у фильма есть название"):
        assert str(random_film_name) != ""


@allure.title("Поиск фильма по невалидному названию")
@allure.epic("API тесты")
@allure.story("Поиск")
@allure.feature("Негативные тесты")
@allure.severity("critical")
def test_search_by_name_negative(api: Search):
    film = api.search_by_name("синхрофазатрон")
    with allure.step("Проверить, что фильм не найден"):
        assert len(film) == 0


@allure.title("Поиск фильма по невалидному id")
@allure.epic("API тесты")
@allure.story("Поиск")
@allure.feature("Негативные тесты")
@allure.severity("critical")
def test_search_by_invalid_id_negative(api: Search):
    error = api.search_by_id("0")
    with allure.step("Посмотреть сообщение об ошибке"):
        message = error["message"][0]
    with allure.step("Посмотреть статус-код"):
        status_code = error["statusCode"]
    with allure.step("Сравнить сообщение об ошибке с ожидаемым"):
        assert message == id_error_message
    with allure.step("Проверить, что статус-код: 400"):
        assert status_code == 400
