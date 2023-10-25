from youtube.Resources.elements import Base
from youtube.Resources.locators import HomePageLocators, VideoSuggestionsLocator, VideoPageLocator


class HomePage(Base):
    """home page"""

    def search_video(self, text):
        self.input(HomePageLocators.search_box, text)
        self.click(HomePageLocators.search_button)


class VideoListPage(Base):
    """class for choosing a video from various options"""

    def choose_video(self, video_link):
        video = VideoSuggestionsLocator(video_link).video_chosen
        self.scroll_to_element(video)
        self.click(video)


class VideoPage(Base):
    """cart page class"""

    def check_video(self, video):
        return self.get_text(VideoPageLocator(video).video_chosen)
