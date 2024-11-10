import requests
import allure
from API.values_api import token


class Search:
    """
    Класс содержит методы для работы с поиском через API
    """
    def __init__(self, url: str):
        self.url = url
        self.my_headers = {"accept": "application/json"}
        self.my_headers["X-API-KEY"] = token

    @allure.step("Найти фильм по id {id}")
    def search_by_id(self, id: int) -> dict:
        """
        Принимает параметр id, по которому ищет фильм.
        Возвращает json с данными
        """
        movie_by_id = requests.get(
            self.url + "/v1.4/movie/" + str(id), headers=self.my_headers)
        return movie_by_id.json()

    @allure.step("Найти фильм по названию {name}")
    def search_by_name(self, name: str) -> dict:
        """
        Принимает значение name(название фильма), по которому ищет фильм.
        Возвращает информацию о всех подходящих фильмах
        """
        my_params = {
            "query": name
        }
        movie_by_name = requests.get(
            self.url + "/v1.4/movie/search",
            params=my_params, headers=self.my_headers)
        return movie_by_name.json()["docs"]

    @allure.step("Найти случайный фильм")
    def random_movie(self) -> dict:
        """
        Ищет случайный фильм.
        Возвращает json с данными
        """
        random = requests.get(
            self.url + "/v1.4/movie/random", headers=self.my_headers)
        return random.json()
