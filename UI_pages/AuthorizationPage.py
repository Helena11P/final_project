from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class Authorization:
    """
    Класс содержит методы для работы со страницей авторизации
    """
    def __init__(self, driver):
        self.driver = driver
        driver.get("https://www.kinopoisk.ru/")

    @allure.step("Подождать открытия главной страницы")
    def wait_main_page(self) -> None:
        """
        Ожидает открытия главной станицы сайта
        """
        waiter = WebDriverWait(self.driver, 50)
        waiter.until_not(
            EC.url_matches(r"https://www\.kinopoisk\.ru/showcaptcha\?.*"))

    @allure.step("Открыть страницу авторизации")
    def open_authorization(self) -> None:
        """
        Открывает страницу авторизации
        """
        div = self.driver.find_element(
            By.CSS_SELECTOR, "div.styles_userContainer__hLiRQ")
        button = div.find_element(
            By.CSS_SELECTOR, "div.styles_root__JgDCj")
        button.find_element(
            By.CSS_SELECTOR, "button.styles_loginButton__LWZQp").click()

    @allure.step("Ввести в поле {login}")
    def enter_login(self, login: str) -> None:
        """
       Принимает логин/почту и вводит его в поле
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "#passp-field-login").send_keys(login)

    @allure.step("Нажать кнопку входа")
    def click_enter_button(self) -> None:
        """
        Нажимает кнопку "Войти" на странице авторизации
        """
        div = self.driver.find_element(
            By.CSS_SELECTOR, "div.passp-sign-in-button")
        div.find_element(
            By.CSS_SELECTOR, "button.Button2").click()

    @allure.step(
            "Подождать открытия страницы (появления элемента на странице)")
    def wait_page(self, locator: str) -> None:
        """
        Ожидает появление элемента на странице.
        Принимает locator, по которому находит элемент на странице
        """
        waiter = WebDriverWait(self.driver, 50)
        waiter.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))

    @allure.step("Посмотреть текущий url")
    def get_current_url(self) -> str:
        """
        Возвращает текущий url
        """
        return self.driver.current_url

    @allure.step("Нажать кнопку Войти через google")
    def click_google_button(self) -> None:
        """
        Нажимает на кнопку "Войти через google"
        """
        button = self.driver.find_element(
            By.CSS_SELECTOR, "div.AuthSocialButton")
        button.find_element(
            By.CSS_SELECTOR, 'button[data-t="button:pseudo:social:auth:gg"]').click()

    @allure.step("Подождать открытия 2 окна")
    def wait_popup_window(self) -> None:
        """
        Ожидает открытия всплывающего окна
        """
        waiter = WebDriverWait(self.driver, 50)
        waiter.until(
            EC.number_of_windows_to_be(2))

    @allure.step("Посмотреть сообщение об ошибке")
    def error_message(self) -> str:
        """
        Находит сообщение об ошибке.
        Возвращает тест сообщения.
        """
        error = self.driver.find_element(
            By.CSS_SELECTOR, "div.Textinput-Hint")
        return error.text

    @allure.step("Открыть вкладку Телефон")
    def click_phone_button(self) -> None:
        """
        Нажимает на вкладку "Телефон"
        """
        div = self.driver.find_elements(
            By.CSS_SELECTOR, "div.AuthLoginInputToggle-type")[1]
        div.find_element(
            By.CSS_SELECTOR, "button.Button2").click()

    @allure.step("Ввести {number} в поле телефона")
    def enter_phone_number(self, number: str) -> None:
        """
        Принимает параметр number, который вводит в поле с номером телефона
        """
        field = self.driver.find_element(
            By.CSS_SELECTOR, "#passp-field-phone")
        field.clear()
        field.send_keys(number)
