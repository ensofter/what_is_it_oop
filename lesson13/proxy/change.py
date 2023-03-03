from lesson13.proxy.proxy import YouTubeLibrary, YouTubeVideo, YouTubeLibraryDefaultImpl


class YouTubeLibraryProxy(YouTubeLibrary):
    cached_videos: dict = {}
    cached_popular_vid: list[YouTubeVideo] = []

    def __init__(self, default_yt_impl: YouTubeLibraryDefaultImpl):
        self.default_impl = default_yt_impl

    def download_video(self, vid: str) -> YouTubeVideo:
        if vid in self.cached_videos:
            return self.cached_videos[vid]
        return self.default_impl.download_video(vid=vid)

    def popular_video(self) -> list[YouTubeVideo]:
        if len(self.cached_popular_vid) > 0:
            return self.cached_popular_vid
        return self.default_impl.popular_video()
