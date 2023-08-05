import listparser
import requests

class RSSFeed():
    def __init__(self, title:str, url:str):
        self.Title = title 
        self.URL = url
    
    def __str__(self) -> str:
        return f"RSSFeed(Title={self.Title} URl={self.URL})"

def Opml(opmlurl:str) -> list[RSSFeed]:
    res = []
    for i in listparser.parse(requests.get(opmlurl).content)['feeds']:
        res.append(RSSFeed(i["title"], i["url"]))
    
    return res

