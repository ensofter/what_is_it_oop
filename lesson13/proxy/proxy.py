from abc import ABC, abstractmethod


class YouTubeVideo:
    vid: str = None
    name: str = None
    content: bytearray = None


# default interface from library. we can't change it
class YouTubeLibrary(ABC):

    @abstractmethod
    def download_video(self, vid: str) -> YouTubeVideo:
        pass

    @abstractmethod
    def popular_video(self) -> list[YouTubeVideo]:
        pass

# default implementation from library
# do not use cache
class YouTubeLibraryDefaultImpl(YouTubeLibrary):

    def download_video(self, vid: str) -> YouTubeVideo:
        pass

    def popular_video(self) -> list[YouTubeVideo]:
        pass

# our app that use default implementation library
class OurApp:
    def __init__(self, yt_lib: YouTubeLibrary):
        self.yt_lib = yt_lib

    def work(self, vid: str):
        self.yt_lib.download_video(vid=vid)

    def work2(self):
        self.yt_lib.popular_video()


if __name__ == '__main__':
    my_yt_lib = YouTubeLibraryDefaultImpl()
    app = OurApp(yt_lib=my_yt_lib)
    

