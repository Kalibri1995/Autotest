import time

import pytest
from pom.homepage_nav import HomepageNav
from pom.images_nav import ImagesNav


@pytest.mark.usefixtures('setup')
class TestTwo:

    def test_one(self):
        image_nav = ImagesNav(self.driver)
        pictures_icon = image_nav.get_pictures_icon()
        assert pictures_icon, 'Не нашел иконку "Картинки"'

    def test_two(self):
        image_nav = ImagesNav(self.driver)
        pictures_icon_link_url = image_nav.get_pictures_icon_link()
        current_url = image_nav.get_pictures_link()

        assert current_url == pictures_icon_link_url, 'Не перешли в картинки'

    def test_three(self):
        image_nav = ImagesNav(self.driver)
        current_url = image_nav.get_pictures_link()
        url_01 = image_nav.get_category()

        assert url_01 != current_url, '1 категория не открылась'

    def test_four(self):
        image_nav = ImagesNav(self.driver)
        name_category_text = image_nav.get_name_category()
        category_name_in_search_field_text = image_nav.get_category_name_in_search_field()

        assert name_category_text == category_name_in_search_field_text, 'В поиске не верный текст'

    def test_five(self):
        image_nav = ImagesNav(self.driver)
        href_first_images = image_nav.get_url_images()
        url_open_first_images = image_nav.get_url_open_first_images()

        assert href_first_images == url_open_first_images, 'Не открылась первая картинка'

    def test_six(self):
        image_nav = ImagesNav(self.driver)
        url_open_first_images = image_nav.get_href_open_first_images()
        url_open_second_images = image_nav.forward_button_test()

        assert url_open_first_images != url_open_second_images, 'Следующая картинка не открылась'

    def test_seven(self):
        image_nav = ImagesNav(self.driver)
        url_open_first_images = image_nav.get_href_open_first_images()
        url_02 = image_nav.back_button_test()

        assert url_open_first_images == url_02, 'Не вернула предыдущую картинку'
