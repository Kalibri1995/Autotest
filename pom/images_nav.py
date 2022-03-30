import time
from typing import List, Any, Callable

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager import driver

from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement


class ImagesNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__pictures_icon: str = '//*[@data-id="images"]'
        self.__name_category: str = 'body div.page-layout__content-wrapper.b-page__content > div div.PopularRequestList-Item_pos_0 div.PopularRequestList-SearchText'
        self.__field_category: str = 'PopularRequestList-Item_pos_0'
        self.__category_link: str = 'body > header span.input__box > input'
        self.__table_result_images: str = '/html/body/div[3]/div[2]/div[1]/div[1]/div/div/div/a/img'
        self.__url_open_first_images: str = 'body > div.Modal.Modal_visible.Modal_theme_normal.MMViewerModal.ImagesViewer.Theme.Theme_color_yandex-default.Theme_root_legacy div.MMOrganicSnippet-Text'
        self.__forward_button: str = 'body > div.Modal.Modal_visible.Modal_theme_normal.MMViewerModal.ImagesViewer.Theme.Theme_color_yandex-default.Theme_root_legacy > div.Modal-Wrapper > div > div > div > div.MediaViewer.MediaViewer_theme_fiji.ImagesViewer-Container > div > div.MediaViewer-LayoutMain.MediaViewer_theme_fiji-LayoutMain > div.MediaViewer-LayoutScene.MediaViewer_theme_fiji-LayoutScene > div.CircleButton.CircleButton_type_next.CircleButton_type.MediaViewer-Button.MediaViewer-Button_hovered.MediaViewer_theme_fiji-Button.MediaViewer-ButtonNext.MediaViewer_theme_fiji-ButtonNext > i'
        self.__back_button: str = 'body > div.Modal.Modal_visible.Modal_theme_normal.MMViewerModal.ImagesViewer.Theme.Theme_color_yandex-default.Theme_root_legacy > div.Modal-Wrapper > div > div > div > div.MediaViewer.MediaViewer_theme_fiji.ImagesViewer-Container > div > div.MediaViewer-LayoutMain.MediaViewer_theme_fiji-LayoutMain > div.MediaViewer-LayoutScene.MediaViewer_theme_fiji-LayoutScene > div.CircleButton.CircleButton_type_prev.CircleButton_type.MediaViewer-Button.MediaViewer_theme_fiji-Button.MediaViewer-ButtonPrev.MediaViewer_theme_fiji-ButtonPrev'


    def get_pictures_icon(self) -> WebElement:
        return self.is_visible('xpath', self.__pictures_icon, 'Ищет иконку "Картинки"')

    def open_pictures(self):
        pictures_icon = self.get_pictures_icon()
        pictures_icon.click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)

    def open_first_category_pictures(self):
        category = self.is_present('class_name', self.__field_category, 'Ищет поле категории')
        category.click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)

    def open_first_images(self):
        table_result_images = self.are_present('xpath', self.__table_result_images, 'Ищет таблицу с картинками')
        table_result_images[0].click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)

    def close_all_pages(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def get_pictures_icon_link(self) -> str:
        pictures_icon = self.get_pictures_icon()
        pictures_icon_link_url = pictures_icon.get_attribute('href')
        return pictures_icon_link_url

    def get_pictures_link(self) -> WebElement:
        self.open_pictures()
        url = self.driver.current_url
        return url

    def get_category(self) -> WebElement:
        self.open_first_category_pictures()
        url_01 = self.driver.current_url
        self.close_all_pages()
        return url_01


#test_four
    def get_name_category(self) -> str:
        self.open_pictures()
        name_category = self.is_present('css', self.__name_category, 'Ищет поле c текстом категории')
        name_category_text = name_category.text
        return name_category_text

    def get_category_name_in_search_field(self) -> str:
        self.open_first_category_pictures()
        category_name_in_search_field = self.is_present('css', self.__category_link, 'Ищет поле поиска')
        category_name_in_search_field_text = category_name_in_search_field.get_attribute('value')
        self.close_all_pages()
        return category_name_in_search_field_text


#test_five
    def get_url_images(self) -> str:
        self.open_pictures()
        self.open_first_category_pictures()
        table_result_images = self.are_present('xpath', self.__table_result_images, 'Ищет таблицу с картинками')
        href_first_images = table_result_images[0].get_attribute('alt')
        return href_first_images

    def get_url_open_first_images(self) -> str:
        self.open_first_images()
        open_first_images = self.is_present('css', self.__url_open_first_images, 'Ищет ссыдку картинки')
        url_open_first_images = open_first_images.text
        self.close_all_pages()
        return url_open_first_images


#test_six, test_seven

    def get_href_open_first_images(self) -> str:
        self.open_pictures()
        self.open_first_category_pictures()
        self.open_first_images()
        href = self.driver.current_url
        return href

    def forward_button_test(self) -> WebElement:
        forward_button = self.is_present('css', self.__forward_button, 'Ищет кнопку вперед')
        ActionChains(self.driver).move_to_element(forward_button).perform()
        forward_button.click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        url_open_second_images = self.driver.current_url
        self.close_all_pages()
        return url_open_second_images

    def back_button_test(self) -> WebElement:
        forward_button = self.is_present('css', self.__forward_button, 'Ищет кнопку вперед')
        ActionChains(self.driver).move_to_element(forward_button).perform()
        forward_button.click()
        ActionChains(self.driver).move_to_element(forward_button).perform()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        back_button = self.is_present('css', self.__back_button, 'Ищет кнопку назад')
        ActionChains(self.driver).move_to_element(back_button).perform()
        #action = ActionChains(self.driver)
        #x = 1100
        #y = 700
        #action.w3c_actions.pointer_action.move_to_location(x, y)
        back_button.click()
        time.sleep(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(2)
        url_02 = self.driver.current_url
        self.close_all_pages()
        return url_02








