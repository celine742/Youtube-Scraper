from parser import VideoParser

import pytest


class TestVideoParser:

    def test_video_inexistante(self):
        with pytest.raises(Exception, match = r"Vidéo introuvable"):
            v = VideoParser("https://www.youtube.com/watch?v=cettevideonexistepas")

    def test_get_title(self):
        video = VideoParser("CmgyUYCibwA")
        assert(video.get_title() == "L'histoire du projet le plus fou de ma vie - YouTube") is True

    def test_get_channel(self):
        video = VideoParser("CmgyUYCibwA")
        assert(video.get_channel() == "SQUEEZIE") is True
    
    def test_get_description(self):
        video = VideoParser("gfn281bQJ3g")
        assert(video.get_description() == "Un mec con qui chante mal dans un arbrearbre") is True

    def test_get_links(self):
        video = VideoParser
    
    def test_get_likes(self):
        video = VideoParser("gfn281bQJ3g")
        assert(video.get_likes() == 1857) is True