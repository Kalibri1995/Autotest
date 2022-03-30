import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from pom.homepage_nav import HomepageNav


@pytest.mark.usefixtures('setup')
class TestOne:

    def test_one(self):
        homepage_nav = HomepageNav(self.driver)
        search_field = homepage_nav.get_search_field()

        assert search_field, 'Не нашел поле поиска'

    def test_two(self):
        homepage_nav = HomepageNav(self.driver)
        hint_table = homepage_nav.get_hint_table()

        assert hint_table, 'Не нашел поле с подсказками'

    def test_three(self):
        homepage_nav = HomepageNav(self.driver)
        links = homepage_nav.get_tensor_links_text()
        for link in links:
            assert "tensor.ru" == link, 'Сайта Тензор нет в первых 5 пунктах'






        #actual_search_href = homepage_nav.get_search_href_text()






        #driver = webdriver.Chrome(ChromeDriverManager().install())
        #wait = WebDriverWait(driver, 15)
        #element = wait.until(ec.visibility_of_element_located(By.CSS_SELECTOR, '#text'))
        #element.send_keys('Тензор')
        #element1 = wait.until(ec.visibility_of_al(By.CSS_SELECTOR, '#suggest-item-j43xo3boutf-0'))

        # driver.implicitly_wait(10)
        # driver.find_element(By.CSS_SELECTOR, '#suggest-item-j43xo3boutf-0')

        # wait = WebDriverWait(driver, 15, 0.3)  # 15 секунд проверяет с переодичность в 0.3 секунды
        # element = wait.until(ec.visibility_of_element_located(By.CSS_SELECTOR, '#suggest-item-j43xo3boutf-0'))
