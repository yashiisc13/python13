from youtube.Pages.pages import HomePage, VideoListPage, VideoPage
from mylog import logs


class TestWebsite(object):
    """"test class"""

    def test_main(self, mydriver, website, text, video_link, video):
        log = logs()

        driver = mydriver
        driver.get(website)
        log.info(website)

        HomePage(driver).search_video(text)
        log.info(text)

        VideoListPage(driver).choose_video(video_link)

        title = VideoPage(driver).check_video(video)
        log.info(title)

        assert title == "Bhaja Gauranga Kaha Gauranga | Monks in Mayapur | Navadvip Mandal Parikrama"

        driver.quit()
