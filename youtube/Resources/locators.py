from selenium.webdriver.common.by import By


class HomePageLocators(object):
    """A class for locators on home page"""

    search_box = (By.XPATH, '//input[@id="search"]')
    search_button = (By.ID, "search-icon-legacy")


class VideoSuggestionsLocator(object):
    """A class for locator for choosing video"""

    def __init__(self, video_chosen):
        self.video_chosen = (By.XPATH, video_chosen)


class VideoPageLocator(object):
    """A class for locators on video page"""

    def __init__(self, video_chosen):
        self.video_chosen = (By.XPATH, video_chosen)
