import pytest
from pom.homepage_nav import HomepageNav
import time


@pytest.mark.usefixtures('setup')
class TestHomepage:
    
    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        expexted_links = homepage_nav.NAV_LINK_TEXT
        assert expexted_links == actual_links, 'Validating Nav links'
        for indx in range(8):
            homepage_nav.get_nav_links()[indx].click()
            homepage_nav.driver.delete_all_cookies()
            time.sleep(3)
