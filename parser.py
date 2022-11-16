from bs4 import BeautifulSoup
import requests
import re
import json
from typing import List


class VideoParser:
    id: str
    url: str
    title: str
    channel: str
    description: str
    links: list
    likes: int
    soup: BeautifulSoup

    def __init__(self, id):
        self.id = id
        self.url = f"https://www.youtube.com/watch?v={self.id}"
        self.title = None
        self.channel = None
        self.description = None
        self.links = None
        self.likes = None
        response = requests.get(self.url).text
        self.soup = BeautifulSoup(response, 'lxml')
        if(self.soup.find("meta", itemprop="name") is None):
            raise Exception("Vidéo introuvable")

    def get_title(self) -> str:
        self.title = self.soup.title.get_text()
        return self.title

    def get_channel(self)-> str:
        self.channel = self.soup.find("span", itemprop="author").next.next['content']
        return self.channel

    def get_description(self) -> str:
        pattern = re.compile('(?<=shortDescription":").*(?=","isCrawlable)')
        self.description = pattern.findall(str(self.soup))[0].replace('\\n','\n')
        return self.description

    def get_links(self) -> List[str]:
        self.links = re.findall(r'(https?://[^\s]+)', self.description)
        self.links += re.findall(r"[0-9]+:[0-9]{2}", self.description)
        return self.links
    
    def get_likes(self)-> int:
        data = re.search(r"var ytInitialData = ({.*?});", self.soup.prettify()).group(1)  
        data_json = json.loads(data)  
        videoPrimaryInfoRenderer = data_json['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']
        likes_label = videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label'] 
        self.likes = int(re.sub(r'[^0-9]', '', likes_label))
        return self.likes

    def get_dict(self) -> dict:
        d = {
            "Titre de la video": self.get_title(),
            "URL de la video": self.url,
            "Nom de la chaine": self.get_channel(),
            "Description": self.get_description(),
            "Liens de la description": self.get_links(),
            "Nombre de likes": self.get_likes(),
        }
        return d