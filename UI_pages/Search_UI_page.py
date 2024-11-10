from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Search:
    """
    Класс содержит методы для работы с поиском
    """

    def __init__(self, driver):
        self.driver = driver
        driver.get("https://www.kinopoisk.ru/")

    @allure.step("Подождать открытия главной страницы сайта")
    def wait_main_page(self) -> None:
        """
        Ожидает открытия главной станицы сайта
        """
        waiter = WebDriverWait(self.driver, 150)
        waiter.until_not(
            EC.url_matches(r"https://www\.kinopoisk\.ru/showcaptcha\?.*"))

    @allure.step("Ввести {name} в поле поиска")
    def input_name(self, name: str) -> None:
        """
        Принимает параметр name и вводит его в поле поиска
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "input[name=kp_query]").send_keys(name)

    @allure.step("Нажать кнопку поиска")
    def click_search_button(self) -> None:
        """
        Нажимает на кнопку поиска
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "button.styles_root__CUh_v").click()

    @allure.step("Подождать результатов поиска")
    def wait_result(self, locator: str) -> None:
        """
        Ожидает появления элемента на странице.
        Принимает locator, по которому находит необходимый элемент
        """
        waiter = WebDriverWait(self.driver, 50)
        waiter.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))

    @allure.step("Посмотреть результат поиска")
    def search_result(self) -> str:
        """
        В открывшемся списке поиска находит первый результат и возвращает его название
        """
        div = self.driver.find_element(By.CSS_SELECTOR, "div.info")
        title = div.find_element(By.CSS_SELECTOR, "p.name")
        return title.text

    @allure.step("Прочитать сообщение об ошибке")
    def nothing_found(self) -> str:
        """
        Находит сообщение об отсутствии результата поиска и возвращает его текст
        """
        div = self.driver.find_element(
            By.CSS_SELECTOR, "h2.textorangebig")
        return div.text

    @allure.step("Посмотреть подсказку в списке")
    def search_tips_list(self) -> str:
        """
        Находит 1 результат выпадающего списка подсказок и возвращает его название
        """
        title = self.driver.find_element(
            By.CSS_SELECTOR, "a.styles_mainLink__A4Xkh")
        return title.text

    @allure.step("Посмотреть текущий url")
    def get_current_url(self) -> str:
        """
        Возвращает текущий url
        """
        return self.driver.current_url
