import time
from typing import List, Any, Callable

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement


class HomepageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__search_field: str = '//*[@id="text"]'
        self.__hint_table: str = 'mini-suggest__popup-content'
        self.__tensor_links: str = '#search-result > .serp-item div.Path a.link > b'

        #self.__pictures_icon: str = '//a[contains(@href,"https://yandex.ru/images/")]'
        self.__pictures_icon: str = '//*[@data-id="images"]'
        self.__name_category: str = 'body div.page-layout__content-wrapper.b-page__content > div div.PopularRequestList-Item_pos_0 div.PopularRequestList-SearchText'
        self.__field_category: str = '//*[@id="tabs-navigation-placeholder"]/div/a[6]'
        #self.__field_category: str = '//*[@class="PopularRequestList-Item PopularRequestList-Item_pos_0"]/a '
        self.__category_link: str = 'body > header span.input__box > input'
        self.PICTURES_LINKS: str = 'https://yandex.ru/images/'

    def get_search_field(self) -> WebElement:
        return self.is_visible('xpath', self.__search_field, 'Ищет поле поиска')

    def get_hint_table(self) -> WebElement:
        search_field = self.get_search_field()
        search_field.send_keys('Тензор')

        return self.is_visible('class_name', self.__hint_table, 'Ищет поле с подсказками')

    def get_tensor_links(self) -> list[WebElement]:
        search_field = self.get_search_field()
        search_field.send_keys('Тензор')
        search_field.send_keys(Keys.ENTER)

        return self.are_present('css', self.__tensor_links, 'Ищет ссылку')

    def get_tensor_links_text(self) -> list:
        tensor_links = self.get_tensor_links()
        tensor_links_text = [tensor_link.text for tensor_link in tensor_links[:5]]
        return tensor_links_text






    #
    """
    def get_nav_links(self) -> list[WebElement]:
        input_field = self.is_visible('XPATH', self.__search_list, 'Ischit poisk')
        input_field.send_keys('Тензор')
        input_field.send_keys(Keys.ENTER)
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = [link.text for link in nav_links[:5]]
        return ",".join(nav_links_text)
    """
    #
