from bs4 import BeautifulSoup
import requests
import json
from .wiki_urls import urls
import random
import string
from .models import Book
class Extractor:
    attributes = []             
    data = {}
    id_length = 3
    id = ""

    def generate_id(self):
        key = string.ascii_lowercase+string.digits
        
        for letter in range(self.id_length):
            self.id+=random.choice(key)
        
        if Book.objects.filter(id=self.id):
            generate_id()
            
    
    def wikify(self,s):
        if s:
            s = s.replace("//","https://")
            s = s.replace("./", "https://en.wikipedia.org/w/rest.php/v1/page/")
            return s

    def extract_data(self,url):
        r = requests.get(url)
        if r.status_code == 404:
            url = url.replace("w/rest.php/v1/page","wiki")[:-5]
            r = requests.get(url)
        soup = BeautifulSoup(r.content, features="html.parser")
        infocard = soup.find(attrs={"class": "infobox vcard"})
        if infocard:
            try:
                title = infocard.parent.parent.caption.text.strip()
            except:
                title = soup.head.title.text.replace("<i>","").replace("</i>","")
            
            rows = infocard.tbody.find_all("tr", recursive=False)
            self.data.update({"title":title})
            for row in rows:
                
                if row.td:
                    key = ""
                    value = ""
                    if row.td.attrs["class"][0]=="infobox-image":
                        key = "img"
                        value = self.wikify(row.td.find("img").attrs["src"])
                    if row.th:
                        key = row.th.text.replace("\u00a0", " ")
                        value = row.td.text.replace("\u00a0", " ")
                        if key in ["Published","Date of Publication"]:
                            key = "Publication Date"
                            
                        
                        if key in ["Preceded by","Followed by"]:
                            key = key.replace("by","url").lower()
                            try:
                                value = self.wikify(row.td.a["href"])
                            except:
                                continue
                            
                    if key and value:
                        key = key.lower().replace(" ", "_")
                        if key in self.attributes:
                            self.data |= {key: value.strip()}
                    

            film = soup.find(id="Film_adaptation")
            if not film:
                film = soup.find(id="Film")
            
            if film:
                film = film.parent
                self.data.update({
                    "film_url": self.wikify(film.a['href'])
                })
                
    def __init__(self, url, *args, **kwargs):
        if "attributes" in kwargs:
            self.attributes = kwargs["attributes"]
            
        self.extract_data(url)
        self.generate_id()
        
        self.data.update({"id":self.id})
        
if __name__ == "__main__":
    data = {}
    for url in urls:
        wiki_extractor = Extractor(url,attributes = ['img',
                                                         'title', 
                                                         'author', 
                                                         'illustrator', 
                                                         'country', 
                                                         'language', 
                                                         'series',
                                                         'release_number', 
                                                         'genre', 
                                                         'set_in', 
                                                         'publisher', 
                                                         'publication_date', 
                                                         'pages', 'isbn', 'preceded_by', 'preceded_url', 'followed_by', 'followed_url', 'film', 'film_url'])
        data.update({wiki_extractor.id: wiki_extractor.data})