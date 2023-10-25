import pytest
from selenium import webdriver


@pytest.fixture
def mydriver():
    chrome_options = webdriver.ChromeOptions()

    chrome_options.set_capability("browserName", "chrome")
    chrome_options.set_capability("platformName", "mac")

    mydriver = webdriver.Remote(
            command_executor='http://192.168.1.2:4444',
            options=chrome_options
        )
    return mydriver


@pytest.fixture
def website():
    website = 'https://www.youtube.com'
    return website


@pytest.fixture
def text():
    text = "Gauranga"
    return text


@pytest.fixture
def video_link():
    video_link = ("//div//yt-formatted-string[contains(@aria-label, 'Bhaja Gauranga Kaha Gauranga |"
                  " Monks in Mayapur | Navadvip Mandal Parikrama by ISKCON Bangalore')]")
    return video_link


@pytest.fixture
def video():
    return "//div[@id='title']//yt-formatted-string"
